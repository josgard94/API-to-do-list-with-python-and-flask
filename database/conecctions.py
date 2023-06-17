from sqlalchemy import create_engine
from config.credentials import credentials

class SingletonConnection:
    _instance = None

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
            print(error)