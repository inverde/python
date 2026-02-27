from sqlalchemy.orm import Session
from survey.models import Respondent, School

# CREATE
def create_respondent(session: Session,
                      SchoolID: int,
                      Age: int = None,
                      Grade: str = None,
                      Gender: str = None,
                      SurveyYear: int = None,
                      DeviceInfo: str = None,
                      IPAddress: str = None,
                      TokenExpiry: str = None):
    # Validation: ensure SchoolID exists
    school = session.query(School).filter(School.SchoolCode == SchoolID).first()
    if not school:
        raise ValueError(f"SchoolID {SchoolID} does not exist in School table.")

    new_respondent = Respondent(
        SchoolID=SchoolID,
        Age=Age,
        Grade=Grade,
        Gender=Gender,
        SurveyYear=SurveyYear,
        DeviceInfo=DeviceInfo,
        IPAddress=IPAddress,
        TokenExpiry=TokenExpiry
    )
    session.add(new_respondent)
    session.commit()
    session.refresh(new_respondent)
    return new_respondent

# READ
def get_respondent(session: Session, respondent_id: int):
    return session.query(Respondent).filter(Respondent.id == respondent_id).first()

def get_all_respondents(session: Session):
    return session.query(Respondent).all()

# UPDATE
def update_respondent(session: Session, respondent_id: int, **kwargs):
    respondent = session.query(Respondent).filter(Respondent.id == respondent_id).first()
    if not respondent:
        return None
    for key, value in kwargs.items():
        if hasattr(respondent, key):
            setattr(respondent, key, value)
    session.commit()
    session.refresh(respondent)
    return respondent

# DELETE
def delete_respondent(session: Session, respondent_id: int):
    respondent = session.query(Respondent).filter(Respondent.id == respondent_id).first()
    if not respondent:
        return False
    session.delete(respondent)
    session.commit()
    return True
