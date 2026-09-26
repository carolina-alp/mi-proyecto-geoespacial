from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_pharmacies_nearby_returns_200():
    response = client.get("/pharmacies/nearby?lat=-17.3900&lon=-66.1550&radius_meters=1000")
    assert response.status_code == 200

def test_pharmacies_nearby_returns_central_pharmacy():
    response = client.get("/pharmacies/nearby?lat=-17.3900&lon=-66.1550&radius_meters=1000")
    data = response.json()
    assert any(p["name"] == "Central Pharmacy" for p in data)

def test_pharmacies_nearby_empty_far_away():
    response = client.get("/pharmacies/nearby?lat=0&lon=0&radius_meters=100")
    data = response.json()
    assert data == []