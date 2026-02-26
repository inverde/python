import app
from sqlalchemy import create_engine, Metadata

# Create engine
engine = create_engine()

tables=['Regions', 'Districts', 'Buildings', 'Schools', 'Respondents', 'Sections', 'Questions', 'Answers']

if __name__ == "__main__":
    app.drop_all_tables(tables)
