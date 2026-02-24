from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from . import Base

class School(Base):
    __tablename__ = "Schools"
    # Database table columns
    SchoolID = Column(Integer, primary_key=True, autoincrement=True)
    SchoolCode = Column(String, unique=True, nullable=False)
    SchoolName = Column(String, nullable=False)
    SchoolDistrictID = Column(Integer, ForeignKey("Districts.ID"), nullable=False)
    SchoolType = Column(String, nullable=False)  # Public / Private / Semioficial
    SchoolLevel = Column(String, nullable=False) # Adultos / Básica De Adultos / Inicial - Primario / Inicial - Primario - Secundario / Prepara Acelera / Prepara Regular / Prepara Regular - Prepara Acelera
						 # Primario / Primario - Secundario / Secundario / Other
    SchoolCount = Column(Integer)
    SchoolBuildingID = Column(Integer, ForeignKey("Buildings.ID"), nullable=False)
    FullAddress = Column(String)
    Municipality = Column(String, nullable=False)
    Province = Column(String, nullable=False)
    PostalCode = Column(String)
    GeospatialCoordinates = Column(String, nullable=False)
    SchoolYear = Column(String, nullable=False)

    # Object Relationships
    district = relationship("District", back_populates="schools")
    building = relationship("Building", back_populates="building")
    respondents = relationship("Respondent", back_populates="school")

    # Check Constraints
    __table_args__ = (
       CheckConstraint("SchoolType IN ('Privado', 'Público', 'Semioficial')", name="check_school_type"),
       CheckConstraint("SchoolLevel IN ('Adultos', 'Básica de Adultos', 'Inicial - Primario', 'Inicial - Primario-Secundario', 'Prepara Acelera', 'Prepara Regular', " \
           "'Prepara Regular - Prepara Acelera', 'Primario', 'Primario - Secundario', 'Secundario', 'Other')", name="check_school_level"),
    )
