from flask import Flask
from routes.task_routes import task_routes
import logging

app = Flask(__name__)
app.register_blueprint(task_routes, url_prefix='/tasks')
logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    app.run(debug=True, port=3001)