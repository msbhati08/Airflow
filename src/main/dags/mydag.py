from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def cap_func():
    print ("hello Manjeet")
    return "hello Manjeet"   

dag = DAG('simple-airflow', description='To test simple airflow',
          schedule_interval='0 12 * * *',
          start_date=datetime(2019, 3, 13), catchup=False)

task1 = DummyOperator(task_id='dummy_task1', retries=3, dag=dag)

task2 = PythonOperator(task_id='hello_task1', python_callable=cap_func, dag=dag)

task1 >> task2
