from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey, CheckConstraint, func
from app.database import Base

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    status = Column(String, nullable=False)
    meta_description = Column(String(160))
    created_by = Column(Integer, ForeignKey('admins.id', ondelete='CASCADE'), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        CheckConstraint("status IN ('published', 'error', 'scheduled')", name="ck_article_status"),
    )
