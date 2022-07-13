# Script to train machine learning model.

from sklearn.model_selection import train_test_split

# Add the necessary imports for the starter code.
#!/usr/bin/env python
import argparse
import pandas as pd
import joblib


from ml.data import process_data
from ml.model import train_model, inference, compute_model_metrics


def perform_data(df, feature, model, categorical_features):
    print("==== FEATURE : {feature}")
    for cls in df[feature].unique():
        print("==CLS  : {cls}")
        df_temp = df[df[feature] == cls]
        X, y, _, _ = process_data(df_temp, categorical_features=categorical_features, label="salary", training = True)
        preds = inference(model, X)
        compute_model_metrics(y, preds)
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Evalaute a model",
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

    # Add code to load in the data.


    # Add code to load in the data.
    model = joblib.load(args.model_file_name)

    # Train and save a model.
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

    for feature in cat_features:
        perform_data(data, feature, model, cat_features)


