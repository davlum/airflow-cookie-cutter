from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

dag = DAG(
    dag_id='my_first_dag',
    schedule_interval='@daily',
    start_date=datetime(2020, 9, 1),
    end_date=datetime(2020, 9, 15),
)


def greeter(exec_date):
    print("Hello from Airflow! The execution date is {}.".format(exec_date))


with dag:
    greet = PythonOperator(
        task_id='greet',
        python_callable=greeter,
        op_args=["{{ ts }}"],
    )

    first_this = DummyOperator(task_id='first_this')
    then_this = DummyOperator(task_id='then_this')
    and_this = DummyOperator(task_id='and_this')

    first_this >> [then_this, and_this] >> greet
