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


#U Update Region
def update_region(session: Session, region_id: int, **kwargs) -> Region:
    pass
