# test_api.py
import requests

BASE_URL = "https://google.com"

def test_health():
    r = requests.get(BASE_URL)
    assert r.status_code == 200

def test_get_users():
    r = requests.get(f"{BASE_URL}/users")
    assert r.status_code == 200

# Repeat for your 20 endpoints...
