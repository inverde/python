from sqlalchemy import (
    Column, String, Integer, Text, DateTime, Boolean,
    ForeignKey, CheckConstraint, UniqueConstraint
)
from sqlalchemy.orm import relationship
import datetime
from . import Base

class Section(Base):
    __tablename__ = "Sections"

    SectionID = Column(Integer, primary_key=True, autoincrement=True)
    SectionName = Column(String, nullable=False)
    SectionDescription = Column(Text, nullable=True)
    SectionOrder = Column(Integer, nullable=True)

    questions = relationship("Question", back_populates="section", cascade="all, delete-orphan")


