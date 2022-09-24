import pandas as pd
import logging

from pathlib import Path
from pandas_schema import Column, Schema
from pandas_schema.validation import InRangeValidation, InListValidation

BasePath = Path(__file__).resolve().parent
logger = logging.getLogger(__name__)
FIX_MAX = 0.1

schema = Schema(
    [
        Column("sepal_length", [InRangeValidation(4.3, 7.9 + FIX_MAX)]),
        Column("sepal_width", [InRangeValidation(2.0, 4.4 + FIX_MAX)]),
        Column("petal_length", [InRangeValidation(1.0, 6.9 + FIX_MAX)]),
        Column("petal_width", [InRangeValidation(0.1, 2.5 + FIX_MAX)]),
        Column("classEncoder", [InRangeValidation(0, 2 + FIX_MAX)]),
        Column(
            "class",
            [InListValidation(["Iris-setosa", "Iris-versicolor", "Iris-virginica"])],
        ),
    ]
)


if __name__ == "__main__":

    data = pd.read_parquet(f"{BasePath}/iris-valid.parquet")

    errors = schema.validate(data)
    if len(errors) > 0:
        for error in errors:
            logger.error(error)

        raise SystemError("Dataset not valid")

    logger.info("Dataset valid")
