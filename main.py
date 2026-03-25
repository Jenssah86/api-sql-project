# main.py

# Modules om FastAPI te gebruiken en verbinding te maken met de database
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

# Maak de database tabellen aan op basis van de modellen
models.Base.metadata.create_all(bind=engine)

# Maak een FastAPI applicatie
app = FastAPI()

# Functie om een database session te krijgen
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint om alle sales records op te halen
@app.get("/sales")
def get_sales(db: Session = Depends(get_db)):
    return db.query(models.FactSales).all()
