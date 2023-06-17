from sqlalchemy import create_engine
from config.credentials import credentials
import logging
class SingletonConnection:
    _instance = None
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def __new__(cls):
        if not cls._instance:
            engine = create_engine("mysql+pymysql://"+str(credentials['user'])+":"+str(credentials['password'])+"@"+str(credentials['host'])+":3306/"+str(credentials["database"]))
            cls._instance = super().__new__(cls)
            cls._instance.engine = engine
        return cls._instance


    def get_engine(self):
        try:
           return self.engine
        except Exception as error:
           self.logger.error("connection error -", str(error))