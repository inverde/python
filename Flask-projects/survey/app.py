from sqlalchemy import inspect
from models.__init__ import Base, engine
import logging
import sys, os

"""
# Import all models so they are registered with base
from models.region import Region
from models.district import District
from models.building import Building
from models.school import School
from models.respondent import Respondent
from models.section import Section
from models.question import Question
from models.answer import Answer
"""
#original_stdout = sys.stdout
#sys.stdout = open(os.devnull, 'w')  # Redirect stdout to null to suppress output
#sys.stdout = sys.__stdout__

logging.getLogger("sqlalchemy").setLevel(logging.WARNING)
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
logging.getLogger("sqlalchemy.dialects").setLevel(logging.WARNING)


tablenames = [
    'Regions',
    'Districts',
    'Buildings',
    'Schools',
    'Respondents',
    'Sections',
    'Questions',
    'Answers'
]

def init_db():
    """
    Initializes the database by creating all tables defined in the models.
    Check if any tables from `tablenames` list are missing before creating them.
    If any tables are missing, it will print a message indicating which tables need to be created.
    """
    # Use global variable to access the list of expected table names
    global tablenames
    # Get all the existing table names from the database
    expected_tables = set(tablenames)
    db_tables = set(inspect(engine).get_table_names())
    missing = set([ table for table in tablenames if  table not in db_tables])
    if expected_tables.issubset(db_tables):
        # All tables are present, no need to create them
        print("All tables have been created already !!!")
    elif missing == expected_tables:
        print("Database is empty, creating all tables...")
        if engine.url.database:
            db_path = os.path.abspath(engine.url.database)
            print(f"Database file will be created at path: {db_path}")
            print("Priting all tables imported into Base metadata:", Base.metadata.tables.keys())
        #Base.metadata.create_all(engine)
        #print("Base de datos creada exitosamente.")
        #print(missing)
    else:
        print("Some tables are missing:", missing)


#sys.stdout = original_stdout
#print("Base de datos creada exitosamente.")
if __name__ == "__main__":
    init_db()
