from sqlalchemy.orm import Session
from survey.models import Building, School

# CREATE
def create_building(session: Session, ID: int, BuildingCode: str, BuildingName: str, SchoolID: int):
    # Validation: ensure SchoolID exists in School table
    school = session.query(School).filter(School.SchoolCode == SchoolID).first()
    if not school:
        raise ValueError(f"SchoolID {SchoolID} does not exist in School table.")

    new_building = Building(
        ID=ID,
        BuildingCode=BuildingCode,
        BuildingName=BuildingName,
        SchoolID=SchoolID
    )
    session.add(new_building)
    session.commit()
    session.refresh(new_building)  # ensures persisted state is returned
    return new_building

# READ (single + all)
def get_building(session: Session, building_id: int):
    return session.query(Building).filter(Building.ID == building_id).first()

def get_all_buildings(session: Session):
    return session.query(Building).all()

# UPDATE
def update_building(session: Session, building_id: int, **kwargs):
    building = session.query(Building).filter(Building.ID == building_id).first()
    if not building:
        return None
    for key, value in kwargs.items():
        if hasattr(building, key):
            setattr(building, key, value)
    session.commit()
    session.refresh(building)
    return building

# DELETE
def delete_building(session: Session, building_id: int):
    building = session.query(Building).filter(Building.ID == building_id).first()
    if not building:
        return False
    session.delete(building)
    session.commit()
    return True
