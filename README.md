![Tests](https://github.com/TU_USUARIO/mi-proyecto-geoespacial/actions/workflows/tests.yml/badge.svg)

# Geospatial API - Nearby Pharmacies

API built with FastAPI + PostgreSQL/PostGIS that allows querying nearby pharmacies for a given location using spatial queries (ST_DWithin, ST_Distance).

## Tech Stack
- FastAPI
- PostgreSQL 16 + PostGIS 3.4
- Docker / Docker Compose
- psycopg2

## How to Run

1. Start the database:
   \`\`\`
   docker-compose up -d
   \`\`\`

2. Create a virtual environment and install dependencies:
   \`\`\`
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   \`\`\`

3. Run the server:
   \`\`\`
   uvicorn main:app --reload
   \`\`\`

4. Open the interactive API docs at:
   http://127.0.0.1:8000/docs

## Main Endpoint

`GET /farmacias/cerca?lat={lat}&lon={lon}&radio_metros={radio}`

Returns pharmacies within the specified radius, ordered by distance.

## What This Project Demonstrates
- Spatial SQL queries with PostGIS (proximity search, distance calculation)
- REST API design with FastAPI
- Containerized local development with Docker Compose
- Clean separation between database layer and API layer