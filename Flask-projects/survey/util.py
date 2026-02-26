from app import drop_all_tables
from sqlalchemy import create_engine, Metadata
# Get the path from a SQLite database file

db_path='/worspaces/python/Flask-projects/survey/data/instance/app.sqlite3.db'
import datetime
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Answer(Base):
    __tablename__ = "Answers"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    RespondentID = Column(Integer, ForeignKey("Respondents.ID"), nullable=False)
    QuestionID = Column(Integer, ForeignKey("Questions.ID"), nullable=False)
    AnswerValue = Column(Text, nullable=False)  # store numeric as text or JSON; convert as needed
    AnswerTimestamp = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    # Relationships
    respondent = relationship("Respondent", back_populates="answers")
    question = relationship("Question", back_populates="answers")

    def __init__(self, RespondentID, QuestionID, AnswerValue, AnswerTimestamp=None):
        self.RespondentID = RespondentID
        self.QuestionID = QuestionID
        self.AnswerValue = AnswerValue
        self.AnswerTimestamp = AnswerTimestamp or datetime.datetime.utcnow()

    def __repr__(self):
        return (
            f"<Answer(ID={self.ID}, RespondentID={self.RespondentID}, "
            f"QuestionID={self.QuestionID}, AnswerValue='{self.AnswerValue}', "
            f"AnswerTimestamp={self.AnswerTimestamp})>"
        )


def drop_database_tables(db_path:str):
    """
    Drops all tables from a SQLite database file.

    Parameters:
        db_path(str): Path to the SQLite databse file, e.g. 'example.db'
    """
    # Create engine
    engine = create_engine(f"sqlite:///{db_paty}", echo=True)

    # Reflect existing database schema
    metadata = Metadata()
    metadata.reflect(bind=engine)

if __name__ == "__main__":
    app.drop_all_tables(tables)
