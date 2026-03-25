# \# \*\*🚀 FastAPI + MySQL: Lokale Setup\*\*

# 

# 

# \*Dit project gebruikt FastAPI om een API-connectie op te bouwen,

# vervolgens wordt er data uit een lokale sql-database geladen als er een GET-request wordt gedaan.

# In deze situatie wordt er een MySQL database gebruikt die draait op XAMPP.\*

# 

# 

# \## \*\*📦 1. Installeer de benodigde packages\*\*

# 

# Maak lokaal een map api-sql-project aan en gebruik deze als je rootmap voor dit project.

# 

# Open VS Code en open de rootmap, maak hier je venv aan: python -m venv venv

# Activeer de virtual environment:  .\\venv\\Scripts\\Activate.ps1

# 

# \*\*Gebruik je virtual environment en installeer:\*\*

# 

# \- FastAPI → je API‑framework

# \- Uvicorn → ASGI server

# \- SQLAlchemy → ORM / database‑laag

# \- mysql-connector-python → MySQL driver

# \- python-dotenv → gegevens afschermen

# 

# 

# Voer onderstaande opdracht uit in je venv:

# 

# \*\*pip install fastapi uvicorn mysql-connector-python sqlalchemy python-dotenv\*\*

# 

# 

# !\[pip list](images/11.jpg)

# 

# 

# \## \*\*🗂️ 2. Maak een projectstructuur\*\*

# 

# 

# \*\*api-sql-project/

# │── main.py

# │── database.py

# └── models.py\*\*

# 

# 

# \## \*\*🔌 3. Database‑configuratie (database.py)\*\*

# 

# Maak eerst een \*\*.env bestand \*\* en vul gegevens in:

# 

# !\[env-bestand](images/22.jpg)

# 

# 

# !\[database.py](images/3.jpg)

# 

# Databaseverbinding

# Dit script maakt de verbinding met de MySQL‑database.

# Het laadt de instellingen uit het .env‑bestand, bouwt de database‑URL, maakt een SQLAlchemy‑engine

# en zorgt voor een SessionLocal waarmee andere scripts database‑sessies kunnen openen.

# Regelt de connectie met MySQL en levert sessies voor database‑operaties.

# 

# 

# 

# \## \*\*🧱 4. Maak een model (models.py)\*\*

# 

# 

# !\[models.py](images/4.jpg)

# 

# Database‑tabellen

# In dit script staan de SQLAlchemy‑modellen.

# Elke class stelt een tabel voor in de database (zoals fact\_sales).

# De kolommen in de class komen overeen met de kolommen in MySQL.

# Definieert de structuur van de tabellen die je API gebruikt

# 

# 

# \## \*\*🌐 5. Bouw je FastAPI‑app (main.py)\*\*

# 

# 

# !\[main.py](images/5.jpg)

# 

# 

# FastAPI applicatie

# Dit is het hoofdscript van de API.

# Het start de FastAPI‑server, maakt de database‑tabellen aan (als ze nog niet bestaan)

# en bevat de endpoints zoals /sales. Via Depends(get\_db) krijgt elk endpoint automatisch een database‑sessie.

# Start de API en bevat de routes waarmee je data uit de database kunt opvragen.

# 

# 

# \## ▶️\*\* 6. Start je API\*\*

# 

# \*\*uvicorn main:app --reload\*\* (start de API-applicatie vanuit main.py)

# 

# 

# !\[server starten](images/6.jpg)

# 

# 

# \## \*\*▶️ 7. TESTEN\*\*

# 

# Ga naar: http://127.0.0.1:8000/sales om te testen of de data uit de\*\* fact\_sales\*\* tabel wordt weergegeven.

# 

# 

# !\[API-call output](images/7.jpg)

# 

# 

# 

# 

# 



