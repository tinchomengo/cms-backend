from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base

class ArticleTag(Base):
    __tablename__ = 'article_tags'
    article_id = Column(Integer, ForeignKey('articles.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    tag_id = Column(Integer, ForeignKey('tags.id', ondelete='CASCADE'), primary_key=True, nullable=False)
