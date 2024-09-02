from airflow.models import DAG

from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator

import pendulum


start_date =  pendulum.today().add(days=-1)


def print_msg():
    print("Iniciando o DAG")


with DAG(dag_id="magalu_dag", schedule_interval="@daily", start_date=start_date):

    print_tsk = PythonOperator(
        task_id="print_tsk",
        python_callable=print_msg
    )



    webscrapping_container_tsk = DockerOperator(
        task_id="crawler_mglu_task",
        image="hello-world",
        container_name="crawler-magalu-container",
        docker_url="tcp://docker-socket-proxy:2375",
        auto_remove=False,
        tty=True,
        xcom_all=False,
    )



    print_tsk >> webscrapping_container_tsk