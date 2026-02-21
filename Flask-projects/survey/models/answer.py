from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from . import Base

class Answer(Base):

    __tablename__ = "Answers"
    AnswerID = Column(Integer, primary_key=True, autoincrement=True)
    RespondentID = Column(Integer, ForeignKey("Respondents.RespondentID"), nullable=False)
    QuestionID = Column(Integer, ForeignKey("Questions.QuestionID"), nullable=False)
    AnswerValue = Column(Text, nullable=False)
    AnswerTimestamp = Column(DateTime, default=datetime.datetime.utcnow)

    respondent = relationship("Respondent", back_populates="answers")
    question = relationship("Question", back_populates="answers")