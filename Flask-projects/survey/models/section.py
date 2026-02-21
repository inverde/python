from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from . import Base


class Section(Base):
    __tablename__ = "Sections"
    
    Section = Column(Integer, primary_key=True, autoincrement=True)
    SectionName = Column(String, nullable=False)
    SectionDescription = Column(Text)
    SectionOrder = Column(Integer)

    questions = relationship("Question", back_populates="section")