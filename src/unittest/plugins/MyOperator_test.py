import unittest
from datetime import datetime
from airflow import DAG
from airflow.models import TaskInstance
from airflow.operators import MyOperator


class TestMyOperator(unittest.TestCase):

    def test_execute(self):
        dag = DAG(dag_id='anydag', start_date=datetime.now())
        task = MyOperator(my_operator_param=10, dag=dag, task_id='anytask')
        ti = TaskInstance(task=task, execution_date=datetime.now())
        result = task.execute(ti.get_template_context())
        self.assertEqual(result, 20)
