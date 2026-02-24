from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


std_base = None
Base = None
def get_Base():
    global std_base
    global Base
    if Base is None:
        std_base = declarative_base()
        return std_base
    return Base

Base = get_Base()

engine = create_engine("sqlite:////workspaces/python/Flask-projects/survey/data/instance/app.sqlite3.db", echo=True)

from models.region import Region
from models.district import District
from models.building import Building
from models.school import School
from models.respondent import Respondent
from models.section import Section
from models.question import Question
from models.answer import Answer


# SQLITE Engine



# Probar conexión inmediatamente
try:
    with engine.connect() as connection:
        print("✅ Conexión establecida con la base de datos SQLite.")

except Exception as e:

    print("❌ Error al conectar con la base de datos:", e)

# Session
sessionLocal = sessionmaker(bind=engine)
