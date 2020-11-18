from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from util.funcs import greet, on_failure

DEFAULT_ARGS = {
    'retries': 3,
    'retry_exponential_backoff': True,
    'on_failure_callback': on_failure,
}


dag = DAG(
    dag_id='example_dag',
    default_args=DEFAULT_ARGS,
    schedule_interval='@hourly',
    start_date=datetime(2020, 9, 1),
    end_date=datetime(2020, 9, 1, 15),
    max_active_runs=3,
)

task1 = DummyOperator(
    dag=dag,
    task_id='task1',
)


task2 = PythonOperator(
    dag=dag,
    task_id='task2',
    python_callable=greet,
)

task1 >> task2
