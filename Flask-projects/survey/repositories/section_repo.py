from sqlalchemy.orm import Session
from survey.models import Section, Survey

# CREATE
def create_section(session: Session, name: str, survey_id: int, section_order: int):
    # Validation: ensure SurveyID exists
    survey = session.query(Survey).filter(Survey.id == survey_id).first()
    if not survey:
        raise ValueError(f"SurveyID {survey_id} does not exist in Survey table.")

    new_section = Section(
        name=name,
        survey_id=survey_id,
        section_order=section_order
    )
    # SectionCode is auto-generated in __init__
    session.add(new_section)
    session.commit()
    session.refresh(new_section)
    return new_section

# READ (single + all)
def get_section(session: Session, section_code: str):
    return session.query(Section).filter(Section.SectionCode == section_code).first()

def get_all_sections(session: Session):
    return session.query(Section).all()

# UPDATE
def update_section(session: Session, section_code: str, **kwargs):
    section = session.query(Section).filter(Section.SectionCode == section_code).first()
    if not section:
        return None
    for key, value in kwargs.items():
        if hasattr(section, key):
            setattr(section, key, value)
    session.commit()
    session.refresh(section)
    return section

# DELETE
def delete_section(session: Session, section_code: str):
    section = session.query(Section).filter(Section.SectionCode == section_code).first()
    if not section:
        return False
    session.delete(section)
    session.commit()
    return True
