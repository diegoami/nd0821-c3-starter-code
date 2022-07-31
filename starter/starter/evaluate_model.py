# Script to train machine learning model.

from sklearn.model_selection import train_test_split

# Add the necessary imports for the starter code.
#!/usr/bin/env python
import argparse
import pandas as pd
import joblib
import os

from ml.data import process_data
from ml.model import train_model, inference, compute_model_metrics
from sklearn.metrics import confusion_matrix

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
        "--model_dir_name",
        type=str,
        help="Fully-qualified dir name location for model",
        required=True,
    )



    # Add code to load in the data.
    args = parser.parse_args()
    data = pd.read_csv(args.data_file_name)
    dirname = args.model_dir_name

    # Add code to load in the data.
    model = joblib.load(os.path.join(dirname, 'model'))
    encoder = joblib.load(os.path.join(dirname, 'encoder'))
    lb = joblib.load(os.path.join(dirname, 'lb'))
    cat_features = joblib.load(os.path.join(dirname, 'cat_features'))

    X, y, _, _ =  process_data(
        data, categorical_features=cat_features, label="salary", encoder = encoder, lb = lb, training = True
    )

    idx_pos, idx_neg = y == 0, y == 1

    preds = inference(model, X)
    print(" =============== GENERAL ====================")
    precision, recall, fbeta = compute_model_metrics(y, preds)
    cm = confusion_matrix(y, preds).ravel()

    # Add code to load in the data.
    print(f"precision: {precision}, recall: {recall}, fbeta: {fbeta}")
    if len(cm) == 4:
        tn, fp, fn, tp = cm
        print(f"TP, FP, FN, TN: {(tn, fp, fn, tp)}")

    print("============================================")
    print()
    print()
    print()

    for slice_feature in cat_features:
        list_unique = data[slice_feature].unique()
        print(f"{slice_feature} : {list_unique}")

    for slice_feature in cat_features:
        print(f"==== SLICE FORF FEATURE : {slice_feature}")
        for cls in data[slice_feature].unique():
            print(f"== CLS FOR FEATURE : {cls}")
            idx_slice = data[slice_feature] == cls
            x_slice, y_slice, preds_slice = X[idx_slice], y[idx_slice], preds[idx_slice]
            precision, recall, fbeta = compute_model_metrics(y_slice, preds_slice)
            print(f"precision: {precision}, recall: {recall}, fbeta: {fbeta}")
            cm = confusion_matrix(y_slice, preds_slice).ravel()
            if len(cm) == 4:
                tn, fp, fn, tp = cm
                print(f"TP, FP, FN, TN: {(tn, fp, fn, tp)}")
        print()
        print()
        print()
        print()
