import unittest
from airflow.models import DagBag


class TestMySampleDAG(unittest.TestCase):
    """Check MyDAG expectation"""

    def setUp(self):
        self.dagbag = DagBag()

    def test_task_count(self):
        """Check task count of MyDAG"""
        dag_id = 'simple-airflow'
        dag = self.dagbag.get_dag(dag_id)
        self.assertEqual(len(dag.tasks), 2)

    def test_contain_tasks(self):
        """Check task contains in MyDAG"""
        dag_id = 'simple-airflow'
        dag = self.dagbag.get_dag(dag_id)
        tasks = dag.tasks
        task_ids = list(map(lambda task: task.task_id, tasks))
        self.assertListEqual(task_ids, ['hello_task1', 'dummy_task1'])

    def test_dependencies_of_dummy_task1(self):
        """Check the task dependencies of dummy_task in MyDAG"""
        dag_id = 'simple-airflow'
        dag = self.dagbag.get_dag(dag_id)
        dummy_task = dag.get_task('dummy_task1')

        upstream_task_ids = list(map(lambda task: task.task_id, dummy_task.upstream_list))
        self.assertListEqual(upstream_task_ids, [])
        downstream_task_ids = list(map(lambda task: task.task_id, dummy_task.downstream_list))
        self.assertListEqual(downstream_task_ids, ['hello_task1'])

    def test_dependencies_of_hello_task1(self):
        """Check the task dependencies of hello_task in MyDAG"""
        dag_id = 'simple-airflow'
        dag = self.dagbag.get_dag(dag_id)
        hello_task = dag.get_task('hello_task1')

        upstream_task_ids = list(map(lambda task: task.task_id, hello_task.upstream_list))
        self.assertListEqual(upstream_task_ids, ['dummy_task1'])
        downstream_task_ids = list(map(lambda task: task.task_id, hello_task.downstream_list))
        self.assertListEqual(downstream_task_ids, [])
