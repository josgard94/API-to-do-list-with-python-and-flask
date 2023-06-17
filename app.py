from flask import Flask
from routes.task_routes import task_routes
import logging
from database.conecctions import SingletonConnection
from models.task_model import Task, Base

app = Flask(__name__)
app.register_blueprint(task_routes, url_prefix='/tasks')
logging.basicConfig(level=logging.DEBUG)

db = SingletonConnection()
engine = db.get_engine()

Base.metadata.create_all(bind=engine)
if __name__ == '__main__':
    app.run(debug=True, port=3001)