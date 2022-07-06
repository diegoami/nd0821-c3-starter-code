# Script to train machine learning model.

from sklearn.model_selection import train_test_split

# Add the necessary imports for the starter code.
#!/usr/bin/env python
import argparse
import itertools
import logging
import os

import yaml
import tempfile
import pandas as pd
import joblib
import numpy as np

from .ml.data import process_data
from .ml.model import train_model

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Train a model",
        fromfile_prefix_chars="@",
    )

    parser.add_argument(
        "--data_file_name",
        type=str,
        help="Fully-qualified file name location for data",
        required=True,
    )

    parser.add_argument(
        "--model_file_name",
        type=str,
        help="Fully-qualified file name location for model",
        required=True,
    )


    # Add code to load in the data.
    args = parser.parse_args()
    data = pd.read_csv(args.data_file_name)
    # Optional enhancement, use K-fold cross validation instead of a train-test split.
    train, test = train_test_split(data, test_size=0.20)

    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]
    X_train, y_train, encoder, lb = process_data(
        train, categorical_features=cat_features, label="salary", training=True
    )

    # Proces the test data with the process_data function.

    model = train_model(X_train, y_train)
    filename = args.model_file_name
    joblib.dump(model, filename)

    # Train and save a model.



