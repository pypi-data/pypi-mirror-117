"""Classes representing Octopus resources"""
import copy
from datetime import datetime
from types import SimpleNamespace
from typing import Optional
import re

from  . import tool

url_without_bad_params = re.compile('(?P<before_params>.+)\{\?')

@property
def deployment_user(self) -> "User":
    response = self.connection.session.get(f"{self.connection.url_base}/api/users/{self.DeployedById}")

    return User(self.connection, **response.json())

@property
def deployments_from_link(self) -> tool.Pages:
    url = url_without_bad_params.search(
        f"{self.connection.url_base}{self.Links['Deployments']}").group(
            'before_params')

    pages = tool.Pages(
        connection=self.connection,
        url=url,
        resource=Deployment)

    return pages

@property
def environment_from_link(self) -> "Environment":
    response = self.connection.session.get(f"{self.connection.url_base}{self.Links['Environment']}")

    return Environment(self.connection, **response.json())

@property
def interruptions_from_link(self) -> tool.Pages:
    pages = tool.Pages(
        connection=self.connection,
        url=f"{self.connection.url_base}{self.Links['Interruptions']}",
        resource=Interruption)

    return pages

@property
def project_from_link(self) -> "Project":
    response = self.connection.session.get(f"{self.connection.url_base}{self.Links['Project']}")

    return Project(self.connection, **response.json())

@property
def release_from_link(self) -> "Release":
    response = self.connection.session.get(f"{self.connection.url_base}{self.Links['Release']}")

    return Release(self.connection, **response.json())

@property
def start_time(self) -> Optional[datetime]:
    """Helper for generating python datatime object from StartTime

    Returns:
        Optional[datetime]: datetime object describing StartTime
    """
    date = None
    if self.StartTime:
        date =  datetime.strptime(self.StartTime, '%Y-%m-%dT%H:%M:%S.%f%z')

    return date

@property
def task_from_link(self) -> "Task":
    response = self.connection.session.get(f"{self.connection.url_base}{self.Links['Task']}")

    return Task(self.connection, **response.json())

@property
def time_completed(self) -> Optional[datetime]:
    """Helper for generating python datatime object from CompletedTime

    Returns:
        Optional[datetime]: datetime object describing CompletedTime
    """
    date = None
    if self.CompletedTime:
        date = datetime.strptime(self.CompletedTime, '%Y-%m-%dT%H:%M:%S.%f%z')

    return date

@property
def time_expiry(self) -> Optional[datetime]:
    """Helper for generating python datatime object from QueueTimeExpiry

    Returns:
        Optional[datetime]: datetime object describing QueueTimeExpiry
    """
    date = None
    if self.QueueTimeExpiry:
        date = datetime.strptime(self.QueueTimeExpiry, '%Y-%m-%dT%H:%M:%S.%f%z')

    return date

@property
def time_last_updated(self) -> Optional[datetime]:
    """Helper for generating python datatime object from LastUpdatedTime

    Returns:
        Optional[datetime]: datetime object describing LastUpdatedTime
    """
    date = None
    if self.LastUpdatedTime:
        date = datetime.strptime(self.LastUpdatedTime, '%Y-%m-%dT%H:%M:%S.%f%z')

    return date

@property
def time_queue(self) -> Optional[datetime]:
    """Helper for generating python datatime object from QueueTime

    Returns:
        Optional[datetime]: datetime object describing QueueTime
    """
    date = None
    if self.QueueTime:
        date = datetime.strptime(self.QueueTime, '%Y-%m-%dT%H:%M:%S.%f%z')

    return date

@property
def variable_set_from_link(self) -> "VariableSet":
    url = f"{self.connection.url_base}{self.Links['Variables']}"

    if match := url_without_bad_params.search(
            f"{self.connection.url_base}{self.Links['Variables']}"):
        url = match.group('before_params')

    response = self.connection.session.get(url)

    return VariableSet(self.connection, **response.json())


class Base(SimpleNamespace):
    def __init__(self, connection: tool.Connection, **kwargs) -> None:
        super().__init__(**kwargs)

        self.connection = connection

    def save(self):
        url = f"{self.connection.url_base}{self.Links['Self']}"

        parameters = copy.deepcopy(self.__dict__)
        del(parameters['connection'])

        response = self.connection.session.put(url, json=parameters)
        response.raise_for_status()

        self.__dict__.update(**response.json())


class Interruption(Base):
    """Helper class for Interruptions"""


class Deployment(Base):
    """Helper class for Deployments"""

    deployment_user = deployment_user
    environment = environment_from_link
    interruptions = interruptions_from_link
    project = project_from_link
    release = release_from_link
    task = task_from_link


class Environment(Base):
    """Helper class for Environments"""


class LibraryVariableSet(Base):
    """Helper class for LibraryVariableSet"""

    variable_set = variable_set_from_link


class Project(Base):
    """Helper class for Projects"""


class Release(Base):
    """Helper class for Release"""

    deployments = deployments_from_link
    project = project_from_link


class Task(Base):
    """Helper class for Tasks"""

    interruptions = interruptions_from_link
    start_time = start_time
    time_queue = time_queue
    time_expiry = time_expiry
    time_last_updated = time_last_updated
    time_completed = time_completed


class User(Base):
    """Helper class for User"""


class VariableSet(Base):
    """Helper class for VariableSets"""

