from sqlalchemy.orm import Session
from survey.models.survey import Survey

# CRUD functions
# Insert Survey
def create_survey(session:Session,
                  SurveyTitle,
                  SurveyPurpose=None,
                  Year=None,
                  Release=None,
                  SponsorInstitution=None) -> Survey:
    new_survey = Survey(
        SurveyTitle=SurveyTitle,
        SurveyPurpose=SurveyPurpose,
        Year=Year,
        Release=Release,
        SponsorInstitution=SponsorInstitution
    )
    session.add(new_survey)
    session.commit()
    session.refresh(new_survey)
    return new_survey

# Read Survey
def get_survey(session: Session, survey_id: int) -> Survey:
    return session.query(Survey).Filter(Survey.ID == survey_id)

def get_all_surveys(session: Session) -> list:
    return session.query(Survey).all()


# Update Survey
def updtate_survey(session: Session, survey_id: int, **kwargs) -> Survey:
    survey = session.query(Survey).filter(Survey.ID == survey_id).first()
    if survey:
        for key, value in kwargs.items():
            if hasattr(survey, key):
                setattr(survey, key, value)
        session.commit()
    return survey

# Delete Survey
def delete_survey(session: Session, survey_id: int) -> bool:
    survey = session.query(Survey).filter(Survey.ID == survey_id).first()
    if survey:
        session.delete(survey)
        session.commit()
        return True
    return False
