from airflow import DAG
from airflow.providers.amazon.aws.transfers.local_to_s3 import LocalFilesystemToS3Operator
from datetime import datetime

# CONFIGURAÇÕES
LOCAL_FILE = "/opt/airflow/files/wc_top_scorers.csv"
S3_BUCKET = "learning-aws-etl-bruna-novais-2026"
S3_KEY = "uploads/wc_top_scorers.csv"

with DAG(
    dag_id="upload_local_para_s3",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["s3", "upload"],
) as dag:

    upload_file = LocalFilesystemToS3Operator(
        task_id="upload_arquivo_s3",
        filename=LOCAL_FILE,
        dest_key=S3_KEY,
        dest_bucket=S3_BUCKET,
        aws_conn_id="AWSConnection",
        replace=True,
    )

    upload_file