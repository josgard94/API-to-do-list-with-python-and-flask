from flask import Blueprint, request
from controllers.task_controller import TaskManagement


task_routes = Blueprint('routes', __name__)
class TaskRoutes:

    def __init__(self) -> None:
        self.controller = TaskManagement()

    def create(self):
        
        return self.controller.create_tasks()

    def list_task(self):
        return self.controller.get_tasks()

    def update_task(self):
        return self.controller.update_task()

    def update_status_status(self):
        return self.controller.update_status_task()

task_routes.add_url_rule('/create', view_func=TaskRoutes().create, methods=['GET'])
task_routes.add_url_rule('/list', view_func=TaskRoutes().list_task, methods=['GET'])
task_routes.add_url_rule('/update', view_func=TaskRoutes().update_task, methods=['PUT'])
task_routes.add_url_rule('/update/status', view_func=TaskRoutes().update_status_status, methods=['PUT'])