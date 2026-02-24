from sqlalchemy import (
    Column, String, Integer, Text, DateTime, Boolean,
    ForeignKey, CheckConstraint, UniqueConstraint
)
from sqlalchemy.orm import relationship
import datetime
from . import Base


class Question(Base):

    __tablename__ = "Questions"

    QuestionID = Column(Integer, primary_key=True, autoincrement=True)
    SectionID = Column(Integer, ForeignKey("Sections.SectionID"), nullable=False)
    QuestionText = Column(Text, nullable=False)
    QuestionType = Column(String, nullable=False)  # closed, multiple, scale, open
    AnswerOptions = Column(Text, nullable=True)    # JSON/text list of options for closed/multiple
    QuestionOrder = Column(Integer, nullable=True)

    section = relationship("Section", back_populates="questions")
    answers = relationship("Answer", back_populates="question", cascade="all, delete-orphan")

    __table_args__ = (
      CheckConstraint("QuestionType IN ('Closed', 'Multiple', 'Scale', Open')", name="check_question_type"),
    )
