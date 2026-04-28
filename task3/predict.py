#!/usr/bin/env python3
"""
FOMO26 Challenge - Task 3: Brain Age Prediction (Regression)
"""
import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description="FOMO26 Task 3 Brain Age Prediction")
    parser.add_argument("--t1", type=str, required=True, help="Path to T1-weighted image")
    parser.add_argument("--output", type=str, required=True, help="Path to save output .txt")
    return parser.parse_args()

def predict_age(args):
    """
    Predict brain age from T1.

    Returns:
        float: Predicted brain age in years
    """

    #########################################################################
    # PLACEHOLDER: ADD YOUR BRAIN AGE PREDICTION CODE HERE
    #########################################################################
    #
    # Available image paths:
    #   - args.t1: T1-weighted image path
    #
    # Example steps you might implement:
    #   1. Load T1 image
    #   2. Preprocess (normalize, skull-strip, register, etc.)
    #   3. Load your trained regression model
    #   4. Run inference to predict age
    #   5. Return predicted age value
    #
    #########################################################################

    predicted_age = 45.0
    return predicted_age

def main():
    args = parse_args()

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    predicted_age = predict_age(args)

    with open(output_path, "w") as f:
        f.write(f"{predicted_age:.2f}\n")

    return 0

if __name__ == "__main__":
    exit(main())
