import json
from fastapi.testclient import TestClient

from census_api import app

client = TestClient(app)

dummy_census_entry = {
    "age": 20,
    "workclass": "State-gov",
    "fnlgt": 3000,
    "education": "Doctorate",
    "education-num": 20,
    "marital-status": "Never-married",
    "occupation": "Sales",
    "relationship": "Not-in-family",
    "race": "White",
    "sex": "Male",
    "capital-gain": 10000,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States"
}



def test_print_out():
    r = client.post("/print_out", json=dummy_census_entry)
    print(r.json())


def test_predict():
    r = client.post("/predict", json=dummy_census_entry)
    print(r.json())
