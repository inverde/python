from sqlalchemy import create_engine, Metadata
# Get the path from a SQLite database file

db_path='/worspaces/python/Flask-projects/survey/data/instance/app.sqlite3.db'
tables=['Regions', 'Districts', 'Buildings', 'Schools', 'Respondents', 'Sections', 'Questions', 'Answers']

def drop_all_tables(db_path:str, tables=None):
    """
    Drops all tables from a SQLite database file.

    Parameters:
        db_path(str): Path to the SQLite databse file, e.g. 'example.db'
    """
    # Get tables from global
    global tables
    try:

        # Create engine
        engine = create_engine(f"sqlite:///{db_path}", echo=True)

        # Reflect existing database schema
        metadata = Metadata()
        metadata.reflect(bind=engine)

        # Drop all existing defined tables
        metadata.drop_all(bind=engine)
        print(f"All tables dropped from {db_path}]")
    except Exception as e:
        # Catch-all exception handler
        print(f"An error occurred while droppinng tables: {e}")


if __name__ == "__main__":
    drop_all_tables(db_path)
