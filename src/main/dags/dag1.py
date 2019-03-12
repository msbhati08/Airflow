from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.dataflow_operator import DataFlowJavaOperator
from airflow.operators import MyOperator
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

dag = DAG('my_sample', description='To test the airflow using various operators',
          schedule_interval='@daily',
          start_date=datetime(2019, 3, 13), catchup=False, default_args=default_args)
task1 = BashOperator(task_id="print_date", bash_command="date", dag=dag)

task2 = PythonOperator(task_id='python_hello_task', python_callable=hello_func, dag=dag)

task3 = DataFlowJavaOperator(
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

task4 = MyOperator(my_operator_param='This is my operator.',
                                task_id='my_first_operator_task', dag=dag)
task1 >> task2 
task2 >> task3
task3 >> task4
