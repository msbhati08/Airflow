from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.dataflow_operator import DataFlowJavaOperator
from google.cloud import storage

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'dataflow_default_options': {
        'project': 'hello',
        'zone': 'asia-south1-a',
        'stagingLocation': 'gs://sample-fixed',
    }
}

dag = DAG('airflow-dataflow-invoke', description='To invoke the Dataflow',
          schedule_interval='@daily',
          start_date=datetime(2019, 3, 4), catchup=False, default_args=default_args)

task1 = PythonOperator(task_id='python_hello_task', python_callable=hello_func, dag=dag)

task2 = DataFlowJavaOperator(
    task_id='dataflow_invoke_task',
    gcp_conn_id='google_cloud_default',
    jar='gs://dataflow-java-demo/jars/Main.jar',
    options={
        'autoscalingAlgorithm': 'BASIC',
        'maxNumWorkers': '50',
        'start': '{{ds}}',
        'partitionType': 'DAY'  

    },
    dag=dag)
task1 >> task2 
