from sqlalchemy import create_engine
from config.credentials import credentials
import logging
from sqlalchemy.orm import sessionmaker


class SingletonConnection:
    _instance = None

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_engine()
        return cls._instance

    def _initialize_engine(self):
        self.logger = logging.getLogger(__name__)
        self.engine = create_engine(
            f"mysql+pymysql://{credentials['user']}:{credentials['password']}@{credentials['host']}:3306/{credentials['database']}")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_engine(self):
        try:
            return self.engine
        except Exception as error:
            self.logger.error("connection error -", str(error))

    def get_session(self):
        return self.session
