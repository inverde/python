from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class School(Base):
    __tablename__ = "Schools"
    SchoolID = Column(Integer, primary_key=True, autoincrement=True)
    SchoolCode = Column(String, unique=True, nullable=False)
    SchoolName = Column(String, nullable=False)
    Province = Column(String, nullable=False)
    Municipality = Column(String, nuallable=False)
    SchoolType = Column(String, nullable=False)  # Public / Private / Semioficial
    SchoolLevel = Column(String, nullable=False) # Adultos / Básica De Adultos / Inicial - Primario / Inicial - Primario - Secundario / Prepara Acelera / Prepara Regular / Prepara Regular - Prepara Acelera
						 # Primario / Primario - Secundario / Secundario / Other
    RegionalCode = Column(String)

    respondents = relationship("Respondent", back_populates="school")
    
    __table_args__ = (
       CheckConstraint("SchoolType IN ('Privado', 'Público', 'Semioficial')", name="check_school_type"),
       CheckConstraint("SchoolLevel IN ('Adultos', 'Básica de Adultos', 'Inicial - Primario', 'Inicial - Primario-Secundario', 'Prepara Acelera', 'Prepara Regular', 'Prepara Regular - Prepara Acelera', 
						'Primario', 'Primario - Secundario', 'Secundario', 'Other')", name="check_school_level"),
    )