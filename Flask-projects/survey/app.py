from models.__init__ import Base, engine

# Import all models so they are registered with base
from models.school import School
from models.respondent import Respondent
from models.section import Section
from models.question import Question
from models.answer import Answer

# Crear todas las tablas
Base.metadata.create_all(engine)

print("Base de datos creada exitosamente.")