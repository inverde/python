from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class District(Base):
    __tablename__ = "Districts"

    ID = Column(Integer, primary_key=True, nullable=False)
    DistrictName = Column(String, nullable=False)
    RegionID = Column(Integer, ForeignKey("regions.ID"), nullable=False)

    region = relationship("Region", back_populates="district")
