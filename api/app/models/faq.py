from sqlalchemy import Column, Integer, String, Text, DateTime, func

from app.core.database import Base


class Faq(Base):
    __tablename__ = "faqs"

    id = Column(Integer, primary_key=True, index=True)
    course = Column(String(50), nullable=False)
    category = Column(String(50), nullable=True)
    question = Column(String(300), nullable=False)
    answer = Column(Text, nullable=False)
    keywords = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now())