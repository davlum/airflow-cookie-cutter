import io
from airflow.hooks.postgres_hook import PostgresHook


def greet():
    print("HULLO")


def on_failure():
    print(":(")


def extract_from_postgres_to_s3(exec_date: str, pg_hook: PostgresHook):
    df = pg_hook.get_pandas_df("SELECT * FROM example_data WHERE date(inserted_at) = %s", parameters=(exec_date,))
    buf = io.StringIO()
    df.to_json(buf, orient='records')
    print("Data is...")
    print(buf.getvalue())
