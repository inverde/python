from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# SQLITE Engine

engine = create_engine("sqlite:///instance/app.sqlite3", echo=True)

# Probar conexión inmediatamente
try:
    with engine.connect() as connection: 
        print("✅ Conexión establecida con la base de datos SQLite.")
except Exception as e:
    
    print("❌ Error al conectar con la base de datos:", e)

# Session
sessionLocal = sessionmaker(bind=engine)
