from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
#get_base = lambda: Base if Base is not None else globals().update(Base=declarative_base()) or Base


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
