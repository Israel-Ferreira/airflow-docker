from airflow.models import DAG

from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator

import pendulum


start_date =  pendulum.today().add(days=-1)

with DAG(dag_id="dag_qualquer", schedule_interval="@daily", start_date=start_date):

    teste_docker_op_task = DockerOperator(
        task_id="teste_docker_op_task",
        image="hello-world",
        container_name="teste-docker-operator-container",
        docker_url="tcp://docker-socket-proxy:2375",
        auto_remove=True,
        tty=True,
        xcom_all=False,
    )





