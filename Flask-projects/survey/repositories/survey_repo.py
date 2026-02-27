from sqlalchemy.orm import Session
from survey.models.survey import Survey

# CRUD functions for survey insert
def create_survey(session:Session,
                  SurveyTitle,
                  SurveyPurpose=None,
                  Year=None,
                  Release=None,
                  SponsorInstitution=None):
    new_survey = Survey(
        SurveyTitle=SurveyTitle,
        SurveyPurpose=SurveyPurpose,
    )
