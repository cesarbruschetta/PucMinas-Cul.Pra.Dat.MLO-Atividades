import warnings
import pandas as pd
import numpy as np
import logging
import mlflow

from pathlib import Path
from urllib.parse import urlparse

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


BasePath = Path(__file__).resolve().parent
logger = logging.getLogger(__name__)


def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

    # Read the iris-quality parquet file
    data = pd.read_parquet(f"{BasePath}/iris-valid.parquet")

    # Split the data into training and test sets. (0.75, 0.25) split.
    train, test = train_test_split(data)

    # The predicted column is "classEncoder" which is a scalar from [0, 2]
    train_x = train.drop(["class"], axis=1)
    test_x = test.drop(["class"], axis=1)
    train_y = train[["classEncoder"]]
    test_y = test[["classEncoder"]]

    with mlflow.start_run(experiment_id=2):
        knn = KNeighborsClassifier(n_neighbors=42)
        knn.fit(train_x, train_y)

        predicted_qualities = knn.predict(test_x)

        (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)
        mlflow.log_metric("mae", mae)

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # Model registry does not work with file store
        if tracking_url_type_store != "file":

            # Register the model
            # There are other ways to use the Model Registry, which depends on the use case,
            # please refer to the doc for more information:
            # https://mlflow.org/docs/latest/model-registry.html#api-workflow
            mlflow.sklearn.log_model(
                knn, "model", registered_model_name="KNeighborsClassifier"
            )
        else:
            mlflow.sklearn.log_model(knn, "model")
