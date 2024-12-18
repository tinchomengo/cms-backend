from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey
from app.database import Base

class ArticleWebsite(Base):
    __tablename__ = 'article_websites'
    article_id = Column(Integer, ForeignKey('articles.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    website_id = Column(Integer, ForeignKey('websites.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    published_at = Column(TIMESTAMP)
