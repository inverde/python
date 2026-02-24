from sqlalchemy import (
    Column, String, Integer, Text, DateTime, Boolean,
    ForeignKey, CheckConstraint, UniqueConstraint
)
from sqlalchemy.orm import relationship
import datetime

from . import Base


class District(Base):
    __tablename__ = "Districts"

    ID = Column(Integer, primary_key=True, nullable=False)
    DistrictName = Column(String, nullable=False)
    RegionID = Column(Integer, ForeignKey("Regions.ID"), nullable=False)

    region = relationship("Region", back_populates="districts")
    schools = relationship("School", back_populates="district", cascade="all, delete-orphan")

    __table_args__ = (
        UniqueConstraint("DistrictName", "RegionID", name="uq_district_region"),
    )
