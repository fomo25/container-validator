#!/usr/bin/env python3
"""
FOMO26 Challenge - Task 4: Trigeminal Neuralgia Multiclass Segmentation
"""
import argparse
import nibabel as nib
import numpy as np
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description="FOMO26 Task 4 Trigeminal Multiclass Segmentation")
    parser.add_argument("--t2w", type=str, required=True, help="Path to T2-weighted image")
    parser.add_argument("--output", type=str, required=True, help="Path to save segmentation NIfTI")
    return parser.parse_args()

def predict_segmentation(args):
    """
    Generate multiclass segmentation mask from T2w.

    Returns:
        tuple: (segmentation_mask, reference_image)
            - segmentation_mask: int array with values in {0, 1, 2}
            - reference_image: nibabel image used to copy affine/header
    """
    reference_img = nib.load(args.t2w)
    shape = reference_img.shape

    #########################################################################
    # PLACEHOLDER: ADD YOUR MULTICLASS SEGMENTATION CODE HERE
    #########################################################################
    #
    # Available image paths:
    #   - args.t2w: T2-weighted image path
    #
    # Output convention:
    #   0 = background
    #   1 = structure_1
    #   2 = structure_2
    #
    #########################################################################

    segmentation_mask = np.zeros(shape, dtype=np.int16)
    return segmentation_mask, reference_img

def main():
    args = parse_args()

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)

    segmentation_mask, reference_img = predict_segmentation(args)

    output_img = nib.Nifti1Image(
        segmentation_mask,
        reference_img.affine,
        reference_img.header,
    )
    nib.save(output_img, args.output)

    return 0

if __name__ == "__main__":
    exit(main())
