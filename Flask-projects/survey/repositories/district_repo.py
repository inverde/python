from sqlalchemy.orm import Session
from survey.models.models import District

# CREATE
def create_district(session: Session, ID: int, DistrictName: str, RegionID: int):
    new_district = District(
        ID=ID,
        DistrictName=DistrictName,
        RegionID=RegionID
    )
    session.add(new_district)
    session.commit()
    session.refresh(new_district)  # ensures persisted state is returned
    return new_district

# READ (single + all)
def get_district(session: Session, district_id: int):
    return session.query(District).filter(District.ID == district_id).first()

def get_all_districts(session: Session):
    return session.query(District).all()

# UPDATE
def update_district(session: Session, district_id: int, **kwargs):
    district = session.query(District).filter(District.ID == district_id).first()
    if not district:
        return None
    for key, value in kwargs.items():
        if hasattr(district, key):
            setattr(district, key, value)
    session.commit()
    session.refresh(district)
    return district

# DELETE
def delete_district(session: Session, district_id: int):
    district = session.query(District).filter(District.ID == district_id).first()
    if not district:
        return False
    session.delete(district)
    session.commit()
    return True
