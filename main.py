from fastapi import FastAPI
import psycopg2

app = FastAPI()

def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="postgres",
        user="postgres",
        password="secreto123"
    )

@app.get("/pharmacies/nearby")
def pharmacies_nearby(lat: float, lon: float, radius_meters: int = 1000):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT name,
               ST_Distance(location, ST_MakePoint(%s, %s)::geography) AS distance_meters
        FROM pharmacies
        WHERE ST_DWithin(location, ST_MakePoint(%s, %s)::geography, %s)
        ORDER BY distance_meters;
    """, (lon, lat, lon, lat, radius_meters))
    results = cur.fetchall()
    cur.close()
    conn.close()
    return [{"name": r[0], "distance_meters": r[1]} for r in results]