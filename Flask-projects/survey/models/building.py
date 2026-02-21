from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from . import Base

class Building(Base):
    
    __tablename__ = "buildings"

    ID = Column(Integer, primary_key=True, nullable=False)
    BuildingName = Column(String, nullable=False)

    school = relationship("School", back_populates="building")
