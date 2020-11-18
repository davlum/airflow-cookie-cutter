import io
from airflow.hooks.postgres_hook import PostgresHook
from airflow.hooks.S3_hook import S3Hook


def greet():
    print("HULLO")


def on_failure():
    print(":(")


def extract_from_postgres_to_s3(exec_date: str, pg_hook: PostgresHook, s3_hook: S3Hook):
    df = pg_hook.get_pandas_df("SELECT * FROM example_data WHERE date(inserted_at) = %s", parameters=(exec_date,))
    buf = io.StringIO()
    df.to_json(buf, orient='records')
    data = buf.getvalue()
    s3_path = f's3://example-data-json/{exec_date}/out.json'
    print(f"Uploading to {s3_path}:")
    print(data)
    s3_hook.load_string(buf.getvalue(), s3_path, replace=True)
