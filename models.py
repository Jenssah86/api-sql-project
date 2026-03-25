# models.py

# Modules om tabellen te definiëren
from sqlalchemy import Column, Integer, Float, String, DateTime
from database import Base

# Definieer de FactSales tabel als een SQLAlchemy model
class FactSales(Base):
    __tablename__ = "fact_sales"
    # Definieer de kolommen van de fact_sales tabel
    sales_key = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(String(50))
    customer_key = Column(Integer)
    product_key = Column(Integer)
    date_key = Column(Integer)
    quantity = Column(Integer)
    price = Column(Float)
    total_price = Column(Float)
