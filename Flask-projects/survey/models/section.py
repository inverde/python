from sqlalchemy import (
    Column, String, Integer, Text, DateTime, Boolean,
    ForeignKey, CheckConstraint, UniqueConstraint
)
from sqlalchemy.orm import relationship
import datetime
from . import Base

class Section(Base):
    __tablename__ = "Sections"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    SurveyID = Column(Integer, ForeignKey("Surveys.ID", ondelete="CASCADE"),nullable=False)
    SectionName = Column(String, nullable=False)
    SectionDescription = Column(Text, nullable=True)
    SectionOrder = Column(Integer, nullable=True)

    questions = relationship("Question", back_populates="section", cascade="all, delete-orphan")
    # Relationship to Survey
    survey = relationship("Survey", back_populates="sections")

    # New field: section_code
    SectionCode = Column(String(11), unique=True, nullable=False)

    def __init__(self, name, survey_id, section_order):
        self.SectionName = name
        self.SurveyID = survey_id
        self.SectionOrder = section_order
        # Generate the code automatically
        self.SectionCode = f"S_{survey_id:05d}_{section_order:03d}"

    def __repr__(self):
        return f"<Section(id={self.ID}, SectionCode='{self.SectionCode}', Section='{self.SectionName}')>"
