from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, func
from app.database import Base

class AdminSession(Base):
    __tablename__ = 'admin_sessions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    admin_id = Column(Integer, ForeignKey('admins.id', ondelete='CASCADE'), nullable=False)
    session_token = Column(String, unique=True, nullable=False)
    expires_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
