# Apache Airflow
Apache Airflow (or simply Airflow) is a platform to programmatically author, schedule, and monitor workflows. 
When workflows are defined as code, they become more maintainable, versionable, testable, and collaborative.
Use Airflow to author workflows as directed acyclic graphs (DAGs) of tasks. The Airflow scheduler executes your tasks on an array of workers while following the specified dependencies. Rich command line utilities make performing complex surgeries on DAGs a snap. The rich user interface makes it easy to visualize pipelines running in production, monitor progress, and troubleshoot issues when needed.

# Airflow Structure
we will set airflow_home=/Airflow/src/main, Now under airflow_home

airflow_home
├── airflow.cfg
├── airflow.db
├── dags
│   └── dag1.py            <- First DAG definition file
│   └── dag2.py            <- Second DAG definition file
├── plugins
│   └── my_operators.py    <- Plugin file
└── unittests.cfg
