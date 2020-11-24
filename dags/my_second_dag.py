from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
from util.funcs import extract_from_postgres_to_s3

dag = DAG(
    dag_id='my_second_dag',
    schedule_interval='@daily',
    start_date=datetime(2020, 9, 1),
    end_date=datetime(2020, 9, 15),
)

PythonOperator(
    task_id='extract_from_postgres_to_s3',
    dag=dag,
    python_callable=extract_from_postgres_to_s3,
    op_kwargs={
        'exec_date': '{{ ds }}',
        'pg_hook': PostgresHook('postgres_conn'),
    },
)
