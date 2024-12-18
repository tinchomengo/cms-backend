from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey, func
from app.database import Base

class ArticleImage(Base):
    __tablename__ = 'article_images'
    id = Column(Integer, primary_key=True, autoincrement=True)
    article_id = Column(Integer, ForeignKey('articles.id', ondelete='CASCADE'), nullable=False)
    image_id = Column(Integer, ForeignKey('images.id', ondelete='CASCADE'), nullable=False)
    position = Column(Integer, nullable=False, default=0)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
