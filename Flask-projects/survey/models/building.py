from sqlalchemy import (
    Column, String, Integer, Text, DateTime, Boolean,
    ForeignKey, CheckConstraint, UniqueConstraint
)
from sqlalchemy.orm import relationship
import datetime
from . import Base

class Building(Base):
    __tablename__ = "Buildings"

    ID = Column(Integer, primary_key=True, nullable=False)  # Not autoincrement, must be provided manually
    BuildingCode = Column(String, nullable=False, unique=True)  # unique building code
    BuildingName = Column(String, nullable=False)
    # Each building is assigned to one and only one school.
    # We model this by having Building.SchoolID be a unique FK to Schools.SchoolID (one-to-one).
    SchoolID = Column(Integer, ForeignKey("Schools.SchoolID"), nullable=False, unique=True)

    # Relationship to School
    school = relationship("School", back_populates="building")

    def __init__(self, ID, BuildingCode, BuildingName, SchoolID):
        self.ID = ID
        self.BuildingCode = BuildingCode
        self.BuildingName = BuildingName
        self.SchoolID = SchoolID

    def __repr__(self):
        return (
            f"<Building(ID={self.ID}, BuildingCode='{self.BuildingCode}', "
            f"BuildingName='{self.BuildingName}', SchoolID={self.SchoolID})>"
        )
