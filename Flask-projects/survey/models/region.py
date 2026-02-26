from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from . import Base

class Region(Base):
    __tablename__ = "Regions"

    ID = Column(Integer, primary_key=True, nullable=False)
    RegionName = Column(String, nullable=False, unique=True)

    districts = relationship("District", back_populates="region", cascade="all, delete-orphan")

    def __init__(self, RegionName):
        self.RegionName = RegionName

    def __repr__(self):
        return f"<Region(ID={self.ID}, RegionName='{self.RegionName}')>"
