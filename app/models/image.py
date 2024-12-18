from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from app.database import Base

class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True, autoincrement=True)
    s3_url = Column(String, unique=True, nullable=False)
    alt_text = Column(String)
    file_size = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
