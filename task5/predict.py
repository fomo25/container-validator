#!/usr/bin/env python3
"""
FOMO26 Challenge - Task 5: Polymicrogyria Binary Classification
"""
import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description="FOMO26 Task 5 Polymicrogyria Classification")
    parser.add_argument("--t1w", type=str, required=True, help="Path to T1-weighted image")
    parser.add_argument("--output", type=str, required=True, help="Path to save output .txt")
    return parser.parse_args()

def predict(args):
    """
    Predict polymicrogyria probability from T1w.

    Returns:
        float: probability of positive class (between 0 and 1)
    """

    #########################################################################
    # PLACEHOLDER: ADD YOUR INFERENCE CODE HERE
    #########################################################################
    #
    # Available image paths:
    #   - args.t1w: T1-weighted image path
    #
    #########################################################################

    probability = 0.5
    return probability

def main():
    args = parse_args()

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    probability = predict(args)

    # Match the txt-output convention used by other classification tasks:
    # write to <output_stem>.txt next to the requested output path.
    out_file = output_path.parent / f"{output_path.stem}.txt"
    with open(out_file, "w") as f:
        f.write(f"{probability:.3f}")

    return 0

if __name__ == "__main__":
    exit(main())
