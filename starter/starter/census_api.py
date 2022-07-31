# bar.py

from fastapi import FastAPI
from pydantic import BaseModel
from values.census_entry import CensusEntry
from ml.data import process_data
import argparse
import pandas as pd
import joblib
import os

dirname = os.path.join(os.getcwd(), '..', 'model', 'v1')
# Add code to load in the data.
model = joblib.load(os.path.join(dirname, 'model'))
encoder = joblib.load(os.path.join(dirname, 'encoder'))
lb = joblib.load(os.path.join(dirname, 'lb'))
cat_features = joblib.load(os.path.join(dirname, 'cat_features'))


app = FastAPI()


@app.post("/predict")
async def predict(body: CensusEntry):
    return body