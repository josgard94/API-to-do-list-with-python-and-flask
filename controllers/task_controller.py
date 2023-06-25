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
        status = 200
        try:
            task = Task(name=params.get("name"), description=params.get(
                "description"), priority=params.get("priority"), status=params.get("status"))
            self.session.add(task)
            self.session.commit()
            message = f"created task success!!"
        except Exception as error:
            self.logger.info("Error - %s", str(error))
            message = f"Error to created task !!"
            status = 500

        return message, status

    def update_task(self, data):
        message = "task updated success!!"
        status = 200
        item = self.session.query(Task).get(data.get("id"))
        if item is None:
            return "task don't exists!!", 404

        try:
            fields = ["name", "description", "priority", "status"]
            for field in fields:
                if field in data:
                    setattr(item, field, data.get(field))
            self.session.commit()

        except Exception as error:
            self.session.rollback()
            self.logger.error(str(error))
            message = "Internal server error"
            status = 500
        return message, status

    def get_tasks(self):
        pass
