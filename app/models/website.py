from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from app.database import Base

class Website(Base):
    __tablename__ = 'websites'
    id = Column(Integer, primary_key=True, autoincrement=True)
    domain = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
