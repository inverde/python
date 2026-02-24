from sqlalchemy import inspect
from models.__init__ import Base, engine

# Import all models so they are registered with base
from models.region import Region
from models.district import District
from models.building import Building
from models.school import School
from models.respondent import Respondent
from models.section import Section
from models.question import Question
from models.answer import Answer


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

# Check if a specific table is missing

inspector = inspect(engine)

print(inspector.get_table_names())

for tablename in tablenames:
    if tablename in inspector.get_table_names():
        print(f"Table '{tablename}' already exists.")
    else:
        print("Please create all missing tables in engine")
        break


# Crear todas las tablas
#Base.metadata.create_all(engine)

#print("Base de datos creada exitosamente.")
