from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from . import Base

class Question(Base):

    __tablename__ = "Questions"
    QuestionID = Column(Integer, primary_key=True, autoincrement=True)
    SectionID = Column(Integer, ForeignKey("Sections.SectionID"), nullable=False)
    QuestionText = Column(Text, nullable=False)
    QuestionType = Column(String) # closed, multiple, scale, open
    AnswersOptions = Column(Text)
    QuestionOrder = Column(Integer)

    section = relationship("Section", back_populates="questions")
    answers = relationship("Answer", back_populates="question")


    __table_args__ = (
      CheckConstraint("QuestionType IN ('Closed', 'Multiple', 'Scale', Open')",
      name="check_question_type"),
    )