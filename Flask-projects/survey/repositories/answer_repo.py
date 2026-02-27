import datetime
from sqlalchemy.orm import Session
from survey.models import Answer, Question, Respondent

# CREATE
def create_answer(session: Session,
                  RespondentID: int,
                  QuestionID: int,
                  AnswerValue: str,
                  AnswerTimestamp: datetime.datetime = None):

    # Validation: ensure QuestionID exists
    question = session.query(Question).filter(Question.id == QuestionID).first()
    if not question:
        raise ValueError(f"QuestionID {QuestionID} does not exist in Question table.")

    # Validation: ensure RespondentID exists
    respondent = session.query(Respondent).filter(Respondent.id == RespondentID).first()
    if not respondent:
        raise ValueError(f"RespondentID {RespondentID} does not exist in Respondent table.")

    new_answer = Answer(
        RespondentID=RespondentID,
        QuestionID=QuestionID,
        AnswerValue=AnswerValue,
        AnswerTimestamp=AnswerTimestamp or datetime.datetime.utcnow()
    )
    session.add(new_answer)
    session.commit()
    session.refresh(new_answer)
    return new_answer

# READ (single + all)
def get_answer(session: Session, answer_id: int):
    return session.query(Answer).filter(Answer.id == answer_id).first()

def get_all_answers(session: Session):
    return session.query(Answer).all()

# UPDATE
def update_answer(session: Session, answer_id: int, **kwargs):
    answer = session.query(Answer).filter(Answer.id == answer_id).first()
    if not answer:
        return None
    for key, value in kwargs.items():
        if hasattr(answer, key):
            setattr(answer, key, value)
    session.commit()
    session.refresh(answer)
    return answer

# DELETE
def delete_answer(session: Session, answer_id: int):
    answer = session.query(Answer).filter(Answer.id == answer_id).first()
    if not answer:
        return False
    session.delete(answer)
    session.commit()
    return True
