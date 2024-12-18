from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, func
from app.database import Base

class Subscriber(Base):
    __tablename__ = 'subscribers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    website_id = Column(Integer, ForeignKey('websites.id', ondelete='CASCADE'), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
