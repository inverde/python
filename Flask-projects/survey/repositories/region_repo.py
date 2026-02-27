from sqlalchemy.orm import Session
from survey.models import Region

# Create Region
def create_region(session: Session, ID: int, RegionName: str) -> Region:
    new_region = Region(
        ID=ID,
        RegionName=RegionName
    )
    session.add(new_region)
    session.commit()
    session.refresh(new_region) # To get the persisted state
    return new_region

# Read (single + all) Region
def get_region(session: Session, region_id: int) -> Region:
    return session.query(Region).filter(Region.ID == region_id).first()

def get_all_region(session: Session) -> list:
    return session.query(Region).all()


# Update Region
def update_region(session: Session, region_id: int, **kwargs) -> Region:
    region = session.query(Region).filter(Region.ID == region_id).first()
    if not region:
        return None
    for key, value in kwargs.items():
        if hasattr(region, key):
            setattr(region, key, value)
    session.commit()
    session.refresh()
    return region

# Delete Region
def delete_region(session: Session, region_id: int) -> bool:
    region = session.query(Region).filter(Region.ID == region_id).first()
    if not region:
        return False
    session.delete(region)
    session.commit()
    return True
