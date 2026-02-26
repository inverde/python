from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Survey(Base):
    __tablename__ = "Surveys"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    SurveyTitle = Column(String, nullable=False)
    SurveyPurpose = Column(String, nullable=True)
    Year = Column(Integer, nullable=True)
    Release = Column(String, nullable=True)
    SponsorInstitution = Column(String, nullable=True)

    # Relationship to Sections (cascade delete enabled)
    sections = relationship(
        "Section",
        back_populates="survey",
        cascade="all, delete, delete-orphan",
        passive_deletes=True
    )

    def __init__(self, SurveyTitle, SurveyPurpose=None, Year=None, Release=None, SponsorInstitution=None):
        self.SurveyTitle = SurveyTitle
        self.SurveyPurpose = SurveyPurpose
        self.Year = Year
        self.Release = Release
        self.SponsorInstitution = SponsorInstitution

    def __repr__(self):
        return (
            f"<Survey(ID={self.ID}, SurveyTitle='{self.SurveyTitle}', "
            f"SurveyPurpose='{self.SurveyPurpose}', Year={self.Year}, "
            f"Release='{self.Release}', SponsorInstitution='{self.SponsorInstitution}')>"
        )
