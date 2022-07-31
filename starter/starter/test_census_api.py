import json
from fastapi.testclient import TestClient

from census_api import app

client = TestClient(app)

dummy_census_entry = {
    'age': 20,
    'workclass' : 'State-gov',
    'fnlgt': 3000,
    'education': 'Doctorate',
    'education_num': 20,
    'marital_status': 'Never-married',
    'occupation': 'Sales',
    'relationship': 'Not-in-family',
    'race': 'White',
    'sex': 'Male',
    'capital_gain': 10000,
    'capital_loss': 0,
    'hours_per_week': 40,
    'native_country': 'United-States'
}



def test_post():
    r = client.post("/predict", json=dummy_census_entry)
    print(r.json())
