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

# Read (single + all)
def get_region(session: Session, )
