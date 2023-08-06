"""Access to Octopus APi see """
from enum import Enum
import logging
import os
from typing import Any, Dict
import requests

from . import tool
from . import resource


class StateChoices(Enum):
    CANCELED = 'Canceled'
    CANCELLING = 'Cancelling'
    COMPLETED = 'Completed'
    EXECUTING = 'Executing'
    FAILED = 'Failed'
    INCOMPLETE = 'Incomplete'
    QUEUED = 'Queued'
    RUNNING = 'Running'
    SUCCESS = 'Success'
    TIMEDOUT = 'TimedOut'
    UNSUCCESSFUL = 'Unsuccessful'


class API():
    """Class for interacting with the Octopus Deployments"""
    logger = logging.getLogger(__name__)

    def __init__(self, octopus_url: str, api_key: str):
        """Grants access to the Octopus API.

        Args:
            octopus_url (str): URL to reach your Octopus instance
            api_key (str): API key used to access the Octopus Deploy REST API
        """
        self.octopus_url = octopus_url
        self.session = requests.Session()
        self.session.headers.update({'X-Octopus-ApiKey': api_key})

    def get_deployments(self, parameters: dict=None) -> tool.Pages:
        """Lists all of the deployments from projects,
        releases and environments accessible by the current user.
        The results will be sorted from most recent to least recent deployment.

        Args:
            parameters (dict, optional): Parameters used to query for deployments. Defaults to None.

        Returns:
            tool.Pages: Generator for Deployment objects
        """
        url = '/'.join([
            self.octopus_url,
            'api',
            'deployments'])

        pages = tool.Pages(
            connection=tool.Connection(
                session=self.session,
                url_base=self.octopus_url),
            url=url,
            parameters=parameters,
            resource=resource.Deployment)

        return pages

    def get_deployment(self, deployment_id: str) -> resource.Deployment:
        url = '/'.join([
            self.octopus_url,
            'api',
            'deployments',
            deployment_id])

        response = self.session.get(url)
        response.raise_for_status()

        deployment = resource.Deployment(
            connection=tool.Connection(
                session=self.session,
                url_base=self.octopus_url),
            **response.json())

        return deployment

    def get_environments(self, parameters: dict=None) -> tool.Pages:
        """Lists all of the environments accessible to the user.
        The results will be sorted by the SortOrder field on each environment.

        Args:
            parameters (dict, optional): Parameters used to query for environments. Defaults to None.

        Returns:
            tool.Pages: Generator for Environment objects
        """
        url = '/'.join([
            self.octopus_url,
            'api',
            'environments'])

        pages = tool.Pages(
            connection=tool.Connection(
                session=self.session,
                url_base=self.octopus_url),
            url=url,
            parameters=parameters,
            resource=resource.Environment)

        return pages

    def get_environment(self, id: str) -> resource.Environment:
        url = '/'.join([
            self.octopus_url,
            'api',
            'deployments',
            id])

        response = self.session.get(url)
        response.raise_for_status()

        environment = resource.Environment(
            connection=tool.Connection(
                session=self.session,
                url_base=self.octopus_url),
            **response.json())

        return environment

    def get_library_variable_sets(self, parameters: dict=None) -> tool.Pages:
        """Lists all of the environments accessible to the user.
        The results will be sorted by the SortOrder field on each environment.

        Args:
            parameters (dict, optional): Parameters used to query for environments. Defaults to None.

        Returns:
            tool.Pages: Generator for Environment objects
        """
        url = '/'.join([
            self.octopus_url,
            'api',
            'libraryvariablesets'])

        pages = tool.Pages(
            connection=tool.Connection(
                session=self.session,
                url_base=self.octopus_url),
            url=url,
            parameters=parameters,
            resource=resource.LibraryVariableSet)

        return pages

    def get_library_variable_set(self, id: str) -> resource.LibraryVariableSet:
        url = '/'.join([
            self.octopus_url,
            'api',
            'libraryvariablesets',
            id])

        response = self.session.get(url)
        response.raise_for_status()

        environment = resource.LibraryVariableSet(
            connection=tool.Connection(
                session=self.session,
                url_base=self.octopus_url),
            **response.json())

        return environment

    def create_library_variable_set(self, library_variable_set_dict) -> resource.LibraryVariableSet:
        url = '/'.join([
            self.octopus_url,
            'api',
            'libraryvariablesets'])

        response = self.session.post(url, json=library_variable_set_dict)
        response.raise_for_status()

        environment = resource.LibraryVariableSet(
            connection=tool.Connection(
                session=self.session,
                url_base=self.octopus_url),
            **response.json())

        return environment

    def get_projects(self, parameters: dict=None) -> tool.Pages:
        """Lists all of the environments accessible to the user.
        Lists all of the projects in the supplied Octopus Deploy Space, from all project groups.
        The results will be sorted alphabetically by name.

        Args:
            parameters (dict, optional): Parameters used to query for projects. Defaults to None.

        Returns:
            tool.Pages: Generator for Project objects
        """
        url = '/'.join([
            self.octopus_url,
            'api',
            'projects'])

        pages = tool.Pages(
            connection=tool.Connection(
                session=self.session,
                url_base=self.octopus_url),
            url=url,
            parameters=parameters,
            resource=resource.Project)

        return pages

    def get_project(self, project_id: str) -> resource.Project:
        url = '/'.join([
            self.octopus_url,
            'api',
            'projects',
            project_id])

        response = self.session.get(url)
        response.raise_for_status()


        project = resource.Project(
            connection=tool.Connection(
                session=self.session,
                url_base=self.octopus_url),
            **response.json())

        return project

    def get_releases(self, parameters: dict=None) -> tool.Pages:
        """Lists all of the releases in the supplied Octopus Deploy Space,
        from all projects.
        The results will be sorted from most recent to least recent release.

        Args:
            parameters (dict, optional): Parameters used to query for releases. Defaults to None.

        Returns:
            tool.Pages: Generator for Release objects
        """
        url = '/'.join([
            self.octopus_url,
            'api',
            'releases'])

        pages = tool.Pages(
            connection=tool.Connection(
                session=self.session,
                url_base=self.octopus_url),
            url=url,
            parameters=parameters,
            resource=resource.Release)

        return pages

    def get_release(self, release_id: str) -> resource.Release:
        url = '/'.join([
            self.octopus_url,
            'api',
            'releases',
            release_id])

        response = self.session.get(url)
        response.raise_for_status()

        release = resource.Release(
            connection=tool.Connection(
                session=self.session,
                url_base=self.octopus_url),
            **response.json())

        return release

    def get_tasks(self, parameters: dict=None) -> tool.Pages:
        """Lists all of the tasks in the supplied Octopus Deploy Space.
        The results will be sorted from newest to oldest.

        Args:
            parameters (dict, optional): Parameters used to query for tasks. Defaults to None.

        Returns:
            tool.Pages: Generator for Task objects
        """
        url = '/'.join([
            self.octopus_url,
            'api',
            'tasks'])

        pages = tool.Pages(
            connection=tool.Connection(
                session=self.session,
                url_base=self.octopus_url),
            url=url,
            parameters=parameters,
            resource=resource.Task)

        return pages

    def get_task(self, task_id: str) -> resource.Task:
        url = '/'.join([
            self.octopus_url,
            'api',
            'task',
            task_id])

        response = self.session.get(url)
        response.raise_for_status()

        release = resource.Task(
            connection=tool.Connection(
                session=self.session,
                url_base=self.octopus_url),
            **response.json())

        return release

    def get_users(self, parameters: dict=None) -> tool.Pages:
        """Lists all of the users in the current Octopus Deploy instance,
        from all teams.
        The results will be sorted alphabetically by username..

        Args:
            parameters (dict, optional): Parameters used to query for users. Defaults to None.

        Returns:
            tool.Pages: Generator for User objects
        """
        url = '/'.join([
            self.octopus_url,
            'api',
            'users'])

        pages = tool.Pages(
            connection=tool.Connection(
                session=self.session,
                url_base=self.octopus_url),
            url=url,
            parameters=parameters,
            resource=resource.User)

        return pages

    def get_user(self, release_id: str) -> resource.User:
        url = '/'.join([
            self.octopus_url,
            'api',
            'users',
            release_id])

        response = self.session.get(url)
        response.raise_for_status()

        release = resource.User(
            connection=tool.Connection(
                session=self.session,
                url_base=self.octopus_url),
            **response.json())

        return release
