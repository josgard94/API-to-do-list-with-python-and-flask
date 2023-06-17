from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer(), primary_key=True)
    name = Column(String(30), nullable=False, unique=False)
    description = Column(String(30), nullable=False, unique=False)
    priority = Column(String(30), nullable=False, unique=False)
    created_at = Column(DateTime(),default=datetime.now())

    def __str__(self) -> str:
        return self.name