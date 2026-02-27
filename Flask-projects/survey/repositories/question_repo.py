from sqlalchemy.orm import Session
from survey.models import Question, Section

# CREATE
def create_question(session: Session,
                    SectionID: int,
                    QuestionOrder: int,
                    QuestionText: str,
                    QuestionType: str,
                    AnswerOptions: str = None):
    # Validation: ensure SectionID exists
    section = session.query(Section).filter(Section.id == SectionID).first()
    if not section:
        raise ValueError(f"SectionID {SectionID} does not exist in Section table.")

    new_question = Question(
        SectionID=SectionID,
        QuestionOrder=QuestionOrder,
        QuestionText=QuestionText,
        QuestionType=QuestionType,
        AnswerOptions=AnswerOptions
    )
    # QuestionCode is auto-generated in __init__
    session.add(new_question)
    session.commit()
    session.refresh(new_question)
    return new_question

# READ (single + all)
def get_question(session: Session, question_code: str):
    return session.query(Question).filter(Question.QuestionCode == question_code).first()

def get_all_questions(session: Session):
    return session.query(Question).all()

# UPDATE
def update_question(session: Session, question_code: str, **kwargs):
    question = session.query(Question).filter(Question.QuestionCode == question_code).first()
    if not question:
        return None
    for key, value in kwargs.items():
        if hasattr(question, key):
            setattr(question, key, value)
    session.commit()
    session.refresh(question)
    return question

# DELETE
def delete_question(session: Session, question_code: str):
    question = session.query(Question).filter(Question.QuestionCode == question_code).first()
    if not question:
        return False
    session.delete(question)
    session.commit()
    return True
