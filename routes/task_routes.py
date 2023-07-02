from flask import Blueprint, request
from controllers.task_controller import TaskManagement


task_routes = Blueprint('routes', __name__)


class TaskRoutes:

    def __init__(self) -> None:
        self.controller = TaskManagement()

    def create(self):
        params = request.get_json()
        return self.controller.create_tasks(params)

    def list_task(self):
        return self.controller.get_tasks()

    def update_task(self):
        params = request.get_json()
        return self.controller.update_task(params)

    def delete_task(self):
        params = request.get_json()
        return self.controller.delete_task(params)

task_routes.add_url_rule(
    '/create', view_func=TaskRoutes().create, methods=['GET'])
task_routes.add_url_rule(
    '/list', view_func=TaskRoutes().list_task, methods=['GET'])
task_routes.add_url_rule(
    '/update', view_func=TaskRoutes().update_task, methods=['PUT'])
task_routes.add_url_rule(
    '/delete', view_func=TaskRoutes().delete_task, methods=['PUT'])
