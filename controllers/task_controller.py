from database.conecctions import SingletonConnection
from sqlalchemy import MetaData
import logging
import json
from models.task_model import Task


class TaskManagement:
    def __init__(self):
        self.connection = SingletonConnection()
        self.session = self.connection.get_session()
        self.metadata = MetaData()
        self.logger = logging.getLogger(__name__)

    def create_tasks(self, params):
        try:
            task = Task(name=params.get("name"), description=params.get(
                "description"), priority=params.get("priority"), status=params.get("priority"))
            self.session.add(task)
            self.session.commit()
        except Exception as error:
            self.logger.info("Error - %s", str(error))

        return f"created task success!!"

    def update_task(self):
        pass

    def update_status_task(self):
        pass

    def get_tasks(self):
        pass
