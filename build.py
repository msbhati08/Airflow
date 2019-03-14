from pybuilder.core import use_plugin, init, task, depends, before
from pybuilder.errors import BuildFailedException
from pybuilder.pluginhelper.external_command import ExternalCommandBuilder
from pybuilder.utils import assert_can_execute, read_file
import sys,os

@init
def initialize(project):
    project.set_property("run_unit_tests_propagate_stdout", True)
    project.set_property("run_unit_tests_propagate_stderr", True)
    project.depends_on("apache-airflow", "==1.9.0")
    project.depends_on("cryptography", "==2.2.1")
    project.depends_on("requests", "==2.21.0")
    project.set_property('verbose', True)
    buildfilepath = os.path.dirname(os.path.abspath(__file__))
    basesrcdir = os.path.join(buildfilepath, 'src/main/python')
    for basepath, subdirs, files in os.walk(basesrcdir):
       if(files.__contains__("__init__.py")):
          sys.path.append(basepath)

use_plugin("exec")
use_plugin("python.core")
use_plugin("python.unittest")
use_plugin('python.install_dependencies')
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "airflow-sample"
version = "1.0"
summary = "Python airflow sample"
default_task = ["clean","install_dependencies","analyze","publish"]
