from app import drop_all_tables
from sqlalchemy import create_engine, Metadata
# Get the path from a SQLite database file

db_path='/worspaces/python/Flask-projects/survey/data/instance/app.sqlite3.db'


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

tables=['Regions', 'Districts', 'Buildings', 'Schools', 'Respondents', 'Sections', 'Questions', 'Answers']

if __name__ == "__main__":
    app.drop_all_tables(tables)
