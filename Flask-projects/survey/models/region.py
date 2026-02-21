from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from . import Base

class Region(Base):
    __tablename__="regions"
    ID = Column(Integer, primary_key=True, nullable=False)
    RegionName = Column(String, nullable=False)

    districts = relatioship("District", back_populates="region")