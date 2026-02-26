from sqlalchemy import (
    Column, String, Integer, Text, DateTime, Boolean,
    ForeignKey, CheckConstraint, UniqueConstraint
)
from sqlalchemy.orm import relationship
import datetime, secrets
from . import Base

class Respondent(Base):
    __tablename__ = "Respondents"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    SchoolID = Column(Integer, ForeignKey("Schools.SchoolID"), nullable=False)
    Age = Column(Integer, nullable=True)
    Grade = Column(String, nullable=True)
    Gender = Column(String, nullable=True)
    SurveyYear = Column(Integer, nullable=True)
    AccessToken = Column(String, unique=True, nullable=False, default=lambda: secrets.token_urlsafe(24))
    TokenUsed = Column(Boolean, default=False, nullable=False)
    TokenExpiry = Column(DateTime, nullable=True)  # optional expiry
    DeviceInfo = Column(String, nullable=True)
    IPAddress = Column(String, nullable=True)
    Timestamp = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    school = relationship("School", back_populates="respondents")
    answers = relationship("Answer", back_populates="respondent", cascade="all, delete-orphan")
