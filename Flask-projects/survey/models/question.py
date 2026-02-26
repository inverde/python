from sqlalchemy import (
    Column, String, Integer, Text, DateTime, Boolean,
    ForeignKey, CheckConstraint, UniqueConstraint
)
from sqlalchemy.orm import relationship
import datetime
from . import Base


class Question(Base):
    __tablename__ = "Questions"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    SectionID = Column(Integer, ForeignKey("Sections.ID", ondelete="CASCADE"), nullable=False)
    QuestionOrder = Column(Integer, nullable=False)
    QuestionText = Column(Text, nullable=False)
    QuestionType = Column(String, nullable=False)
    AnswerOptions = Column(Text, nullable=True)

    QuestionCode = Column(String(10), unique=True, nullable=False)

    section = relationship("Section", back_populates="questions")
    answers = relationship("Answer", back_populates="question", cascade="all, delete-orphan")

    __table_args__ = (
        CheckConstraint("QuestionType IN ('Closed', 'Multiple', 'Scale', 'Open')", name="check_question_type"),
    )

    def __init__(self, SectionID, QuestionOrder, QuestionText, QuestionType, AnswerOptions=None):
        self.SectionID = SectionID
        self.QuestionOrder = QuestionOrder
        self.QuestionText = QuestionText
        self.QuestionType = QuestionType
        self.AnswerOptions = AnswerOptions
        self.QuestionCode = self.generate_code(SectionID, QuestionOrder)

    def __repr__(self):
        return (
            f"<Question(QuestionID={self.QuestionID}, QuestionCode='{self.QuestionCode}', "
            f"SectionID={self.SectionID}, QuestionOrder={self.QuestionOrder}, "
            f"QuestionType='{self.QuestionType}')>"
        )

    def generate_code(self, section_id, question_order):
        # Adjust padding here if format changes
        return f"Q_{section_id:03d}_{question_order:04d}"

