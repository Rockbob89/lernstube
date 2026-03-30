# Task 07: Capstone — Image Manipulator

## Objective
Build an image manipulation tool using only NumPy (no PIL/OpenCV for transformations). Demonstrate mastery of arrays, slicing, broadcasting, and vectorized operations.

## Requirements

Create `image_ops.py` with the following functions. Images are represented as NumPy arrays of shape (H, W, 3) with dtype uint8 (RGB).

You may use `PIL`/`matplotlib` only for loading/saving images, not for transformations.

### Functions to Implement

1. **`load_image(path) -> np.ndarray`** — Load image as (H, W, 3) uint8 array.
2. **`save_image(arr, path)`** — Save array back to image file.
3. **`to_grayscale(img) -> np.ndarray`** — Weighted conversion: 0.2989*R + 0.5870*G + 0.1140*B. Return (H, W) uint8.
4. **`adjust_brightness(img, factor) -> np.ndarray`** — Multiply by factor, clip to [0, 255].
5. **`crop(img, top, left, height, width) -> np.ndarray`** — Crop region.
6. **`rotate_90(img, k=1) -> np.ndarray`** — Rotate 90 degrees clockwise, k times.
7. **`flip(img, axis) -> np.ndarray`** — Flip horizontal ('h') or vertical ('v').
8. **`box_blur(img, kernel_size) -> np.ndarray`** — Average blur using a square kernel. Handle edges by ignoring out-of-bounds.
9. **`threshold(img, value) -> np.ndarray`** — Convert to grayscale, then binary (0 or 255) based on threshold.
10. **`blend(img1, img2, alpha) -> np.ndarray`** — Alpha blend two same-size images.

### Deliverable
- `image_ops.py` with all functions
- A `demo.py` script that loads a test image, applies each transformation, and saves results to an `output/` directory
- Include a sample image or instructions for obtaining one

### Evaluation Criteria
- No loops over pixels (vectorized operations only)
- Correct dtype handling (uint8 overflow is a common trap)
- Clean, readable code
