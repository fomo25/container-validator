#!/usr/bin/env python3
"""
FOMO25 Challenge - Task 2: Binary Segmentation
"""
import argparse
import nibabel as nib
import numpy as np
from pathlib import Path

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="FOMO25 Task 2 Binary Segmentation")
    
    # Input paths for each modality
    parser.add_argument("--flair", type=str, help="Path to T2 FLAIR image")
    parser.add_argument("--dwi_b1000", type=str, help="Path to DWI b1000 image")
    parser.add_argument("--t2s", type=str, help="Path to T2* image (optional)")
    parser.add_argument("--swi", type=str, help="Path to SWI image (optional)")
    
    # Output path for segmentation mask
    parser.add_argument("--output", type=str, required=True, help="Path to save segmentation NIfTI")
    
    return parser.parse_args()

def predict_segmentation(args):
    """
    Generate binary segmentation mask based on the provided modalities.
    
    Returns:
        tuple: (segmentation_mask, reference_image) where:
            - segmentation_mask: numpy array with binary mask (0 or 1)
            - reference_image: nibabel image object for metadata
    """
    
    # Load a reference image to get shape and metadata
    reference_img = None
    for modality in ['flair', 'dwi_b1000', 't2s', 'swi']:
        path = getattr(args, modality)
        if path and Path(path).exists():
            reference_img = nib.load(path)
            break
    
    if reference_img is None:
        raise ValueError("No valid modality found")
    
    # Get image shape for creating the mask
    shape = reference_img.shape
    
    #########################################################################
    # PLACEHOLDER: ADD YOUR SEGMENTATION INFERENCE CODE HERE
    #########################################################################
    # 
    # Available image paths:
    #   - args.flair: T2 FLAIR image path
    #   - args.dwi_b1000: DWI b1000 image path
    #   - args.t2s: T2* image path (may be None)
    #   - args.swi: SWI image path (may be None)
    #
    # Example steps you might implement:
    #   1. Load the images you need (not all are required)
    #   2. Preprocess the images (normalize, resample, register, etc.)
    #   3. Load your trained segmentation model
    #   4. Run inference to get predictions
    #   5. Post-process predictions (threshold, clean up, etc.)
    #   6. Return binary mask (0 or 1 values)
    #
    # Example (replace with your actual code):
    #   model = load_your_segmentation_model()
    #   images = load_and_preprocess_images(args)
    #   prediction = model.predict(images)
    #   binary_mask = (prediction > 0.5).astype(np.uint8)
    #
    #########################################################################
    
    # Dummy segmentation - REPLACE THIS WITH YOUR ACTUAL PREDICTION
    segmentation_mask = np.zeros(shape, dtype=np.uint8)
    
    return segmentation_mask, reference_img

def main():
    """Main execution function."""
    args = parse_args()
    
    # Create output directory if it doesn't exist
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    
    # Generate segmentation
    segmentation_mask, reference_img = predict_segmentation(args)
    
    # Create NIfTI image with segmentation mask
    # Uses the reference image's affine matrix and header for proper spatial alignment
    output_img = nib.Nifti1Image(
        segmentation_mask, 
        reference_img.affine, 
        reference_img.header
    )
    
    # Save segmentation mask
    nib.save(output_img, args.output)
    
    return 0

if __name__ == "__main__":
    exit(main())