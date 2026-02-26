from sqlalchemy import (
    Column, String, Integer, Text, DateTime, Boolean,
    ForeignKey, CheckConstraint, UniqueConstraint
)
from sqlalchemy.orm import relationship
import datetime
from . import Base

class School(Base):
    __tablename__ = "Schools"

    SchoolID = Column(Integer, primary_key=True, autoincrement=True)
    SchoolCode = Column(String, unique=True, nullable=False)
    SchoolName = Column(String, nullable=False)
    SchoolDistrictID = Column(Integer, ForeignKey("Districts.ID"), nullable=False)
    SchoolType = Column(String, nullable=False)  # Public / Private / Semioficial
    SchoolLevel = Column(String, nullable=False) # enumerated list below
    StudentCount = Column(Integer, nullable=False)
    GeospatialCoordinates = Column(String, nullable=False)
    FullAddress = Column(String)
    Municipality = Column(String, nullable=False)
    Province = Column(String, nullable=False)
    PostalCode = Column(String)
    SchoolYear = Column(String, nullable=False)

    # Objects relationships
    district = relationship("District", back_populates="schools")
    respondents = relationship("Respondent", back_populates="school", cascade="all, delete-orphan")
    building = relationship("Building", back_populates="school", uselist=False)


    # Table check constraints
    __table_args__ = (
        CheckConstraint("SchoolType IN ('Privado', 'Público', 'Semioficial')", name="check_school_type"),
        CheckConstraint(
            "SchoolLevel IN ('Adultos','Básica de Adultos','Inicial - Primario','Inicial - Primario-Secundario',"
            "'Prepara Acelera','Prepara Regular','Prepara Regular - Prepara Acelera','Primario',"
            "'Primario - Secundario','Secundario','Other')",
            name="check_school_level"
        ),
    )

    def __init__(self, SchoolCode, SchoolName, SchoolDistrictID, SchoolType, SchoolLevel,
                 StudentCount, GeospatialCoordinates, Municipality, Province, SchoolYear,
                 FullAddress=None, PostalCode=None):
        self.SchoolCode = SchoolCode
        self.SchoolName = SchoolName
        self.SchoolDistrictID = SchoolDistrictID
        self.SchoolType = SchoolType
        self.SchoolLevel = SchoolLevel
        self.StudentCount = StudentCount
        self.GeospatialCoordinates = GeospatialCoordinates
        self.Municipality = Municipality
        self.Province = Province
        self.SchoolYear = SchoolYear
        self.FullAddress = FullAddress
        self.PostalCode = PostalCode

    def __repr__(self):
        return (
            f"<School(SchoolID={self.SchoolID}, SchoolCode='{self.SchoolCode}', "
            f"SchoolName='{self.SchoolName}', SchoolDistrictID={self.SchoolDistrictID}, "
            f"SchoolType='{self.SchoolType}', SchoolLevel='{self.SchoolLevel}', "
            f"StudentCount={self.StudentCount}, Municipality='{self.Municipality}', "
            f"Province='{self.Province}', SchoolYear='{self.SchoolYear}')>"
        )

