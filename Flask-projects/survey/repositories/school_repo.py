from sqlalchemy.orm import Session
from survey.models import School

# CREATE
def create_school(session: Session,
                  SchoolCode: str,
                  SchoolName: str,
                  SchoolDistrictID: int,
                  SchoolType: str,
                  SchoolLevel: str,
                  StudentCount: int,
                  GeospatialCoordinates: dict,
                  Municipality: str,
                  Province: str,
                  SchoolYear: int,
                  FullAddress: str = None,
                  PostalCode: str = None):
    new_school = School(
        SchoolCode=SchoolCode,
        SchoolName=SchoolName,
        SchoolDistrictID=SchoolDistrictID,
        SchoolType=SchoolType,
        SchoolLevel=SchoolLevel,
        StudentCount=StudentCount,
        GeospatialCoordinates=GeospatialCoordinates,
        Municipality=Municipality,
        Province=Province,
        SchoolYear=SchoolYear,
        FullAddress=FullAddress,
        PostalCode=PostalCode
    )
    session.add(new_school)
    session.commit()
    session.refresh(new_school)  # ensures persisted state is returned
    return new_school

# READ (single + all)
def get_school(session: Session, school_code: str):
    return session.query(School).filter(School.SchoolCode == school_code).first()

def get_all_schools(session: Session):
    return session.query(School).all()

# UPDATE
def update_school(session: Session, school_code: str, **kwargs):
    school = session.query(School).filter(School.SchoolCode == school_code).first()
    if not school:
        return None
    for key, value in kwargs.items():
        if hasattr(school, key):
            setattr(school, key, value)
    session.commit()
    session.refresh(school)
    return school

# DELETE
def delete_school(session: Session, school_code: str):
    school = session.query(School).filter(School.SchoolCode == school_code).first()
    if not school:
        return False
    session.delete(school)
    session.commit()
    return True
