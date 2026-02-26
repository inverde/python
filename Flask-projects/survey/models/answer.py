from sqlalchemy import (
    Column, String, Integer, Text, DateTime, Boolean,
    ForeignKey, CheckConstraint, UniqueConstraint
)
from sqlalchemy.orm import relationship
import datetime
from . import Base

class Answer(Base):

    __tablename__ = "Answers"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    RespondentID = Column(Integer, ForeignKey("Respondents.ID"), nullable=False)
    QuestionID = Column(Integer, ForeignKey("Questions.ID"), nullable=False)
    AnswerValue = Column(Text, nullable=False)  # store numeric as text or JSON; convert as needed
    AnswerTimestamp = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    respondent = relationship("Respondent", back_populates="answers")
    question = relationship("Question", back_populates="answers")

    def __init__(self, RespondentID, QuestionID, AnswerValue, AnswerTimestamp=None):
        self.D = RespondentID
        self.QuestionID = QuestionID
        self.AnswerValue = AnswerValue
        self.AnswerTimestamp = AnswerTimestamp or datetime.datetime.utcnow()

    def __repr__(self):
        return (
            f"<Answer(ID={self.ID}, RespondentID={self.RespondentID}, "
            f"QuestionID={self.QuestionID}, AnswerValue='{self.AnswerValue}', "
            f"AnswerTimestamp={self.AnswerTimestamp})>"
        )
