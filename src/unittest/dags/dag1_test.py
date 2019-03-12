import unittest
from airflow.models import DagBag


class TestMySampleDAG(unittest.TestCase):
    """Check MySampleDAG expectation"""

    def setUp(self):
        self.dagbag = DagBag()

    def test_task_count(self):
        """Check task count of my_sample dag"""
        dag_id = 'my_sample'
        dag = self.dagbag.get_dag(dag_id)
        self.assertEqual(len(dag.tasks), 4)

    def test_contain_tasks(self):
        """Check task contains in my_sample dag"""
        dag_id = 'my_sample'
        dag = self.dagbag.get_dag(dag_id)
        tasks = dag.tasks
        task_ids = list(map(lambda task: task.task_id, tasks))
        self.assertListEqual(task_ids, ['print_date_task', 'python_hello_task', 'dataflow_invoke_task', 'my_operator_task'])

    def test_dependencies_of_print_date_task(self):
        """Check the task dependencies of print_date_task in my_sample dag"""
        dag_id = 'my_sample'
        dag = self.dagbag.get_dag(dag_id)
        print_date_task = dag.get_task('print_date_task')

        upstream_task_ids = list(map(lambda task: task.task_id, dummy_task.upstream_list))
        self.assertListEqual(upstream_task_ids, [])
        downstream_task_ids = list(map(lambda task: task.task_id, dummy_task.downstream_list))
        self.assertListEqual(downstream_task_ids, ['python_hello_task', 'dataflow_invoke_task', 'my_operator_task'])

    def test_dependencies_of_python_hello_task(self):
        """Check the task dependencies of python_hello_task in my_sample dag"""
        dag_id = 'my_sample'
        dag = self.dagbag.get_dag(dag_id)
        python_hello_task = dag.get_task('python_hello_task')

        upstream_task_ids = list(map(lambda task: task.task_id, hello_task.upstream_list))
        self.assertListEqual(upstream_task_ids, ['print_date_task'])
        downstream_task_ids = list(map(lambda task: task.task_id, hello_task.downstream_list))
        self.assertListEqual(downstream_task_ids, ['dataflow_invoke_task', 'my_operator_task'])

    def test_dependencies_of_python_hello_task(self):
        """Check the task dependencies of dataflow_invoke_task in my_sample dag"""
        dag_id = 'my_sample'
        dag = self.dagbag.get_dag(dag_id)
        dataflow_invoke_task = dag.get_task('dataflow_invoke_task')

        upstream_task_ids = list(map(lambda task: task.task_id, hello_task.upstream_list))
        self.assertListEqual(upstream_task_ids, ['print_date_task', 'python_hello_task'])
        downstream_task_ids = list(map(lambda task: task.task_id, hello_task.downstream_list))
        self.assertListEqual(downstream_task_ids, ['my_operator_task'])
     def test_dependencies_of_python_hello_task(self):
        """Check the task dependencies of my_operator_task in my_sample dag"""
        dag_id = 'my_sample'
        dag = self.dagbag.get_dag(dag_id)
        my_operator_task = dag.get_task('my_operator_task')

        upstream_task_ids = list(map(lambda task: task.task_id, hello_task.upstream_list))
        self.assertListEqual(upstream_task_ids, ['print_date_task', 'python_hello_task', 'dataflow_invoke_task'])
        downstream_task_ids = list(map(lambda task: task.task_id, hello_task.downstream_list))
        self.assertListEqual(downstream_task_ids, [])
