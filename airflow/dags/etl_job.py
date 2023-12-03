from airflow import DAG
from airflow.operators.http_operator import SimpleHttpOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'spark_submit_dag',
    default_args=default_args,
    description='DAG to submit Spark job from Airflow',
    schedule_interval=None,  # Set the schedule interval as per your requirements
)

submit_spark_job_task = SimpleHttpOperator(
    task_id='submit_spark_job',
    method='GET',
    http_conn_id='spark_api',  # Connection ID for Spark API
    endpoint='submit_spark_job',
    headers={"Content-Type": "application/json"},
    dag=dag,
)
submit_spark_job_task
