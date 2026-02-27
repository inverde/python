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
    return new_survey

# Read Survey
def get_survey(session: Session, survey_id: int) -> Survey:
    pass

