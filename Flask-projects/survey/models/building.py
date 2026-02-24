from sqlalchemy import (
    Column, String, Integer, Text, DateTime, Boolean,
    ForeignKey, CheckConstraint, UniqueConstraint
)
from sqlalchemy.orm import relationship
import datetime
from . import Base

class Building(Base):
    __tablename__ = "Buildings"

    ID = Column(Integer, primary_key=True, nullable=False)
    BuildingCode = Column(String, nullable=False, unique=True)  # unique building code
    BuildingName = Column(String, nullable=False)
    # Each building is assigned to one and only one school.
    # We model this by having Building.SchoolID be a unique FK to Schools.SchoolID (one-to-one).
    SchoolID = Column(Integer, ForeignKey("Schools.SchoolID"), nullable=False, unique=True)

    school = relationship("School", back_populates="building")
