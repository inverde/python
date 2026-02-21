from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import datetime
from . import Base

class Respondent(Base):
    __tablename__ = "Respondents"
    
    RespondentID = Column(Integer, primary_key=True, autoincrement=True)
    SchoolID = Column(Integer, ForeignKey("Schools.SchoolID"), nullable=False)
    Age = Column(Integer)
    Grade = Column(String) 
    Gender = Column(String)
    SurveyYear = Column(Integer, nullable=True)
    AccessToken = Column(String, unique=True)
    DeviceInfo = Column(String)
    IPAddress = Column(String)
    Timestamp = Column(DateTime, default=datetime.datetime.utcnow)


    school = relationship("School", back_populates="respondents")
    answers = relationship("Answer", back_populates="respondent")