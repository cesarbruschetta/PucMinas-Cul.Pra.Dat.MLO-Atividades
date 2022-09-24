from airflow import DAG
from datetime import datetime, timedelta
from pathlib import Path

from airflow.operators.dummy import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.utils.task_group import TaskGroup

BasePath = Path(__file__).resolve().parent

pathScript = "~/airflow/dags/etl_scripts"


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2022, 9, 1),
    "retries": 1,
}

with DAG(
    "dag-pipeline-iris-atividade-v1",
    schedule_interval=timedelta(minutes=10),
    catchup=False,
    default_args=default_args,
) as dag:

    start = DummyOperator(task_id="start")

    validate = BashOperator(
        task_id="ValidateSchema",
        bash_command=f"python {BasePath}/etl_scripts/validate_schema.py",
    )

    with TaskGroup("build-model", tooltip="BuildModel") as model:

        model_1 = BashOperator(
            dag=dag,
            task_id="Model_LinReg",
            bash_command=f"python {BasePath}/etl_scripts/model_linear_model.py",
        )

        model_2 = BashOperator(
            dag=dag,
            task_id="Model_Neighbors",
            bash_command=f"python {BasePath}/etl_scripts/model_neighbors.py",
        )

        [model_1, model_2]

    end = DummyOperator(task_id="end")

    start >> validate >> model >> end
