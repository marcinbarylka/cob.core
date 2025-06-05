"""Module for image processing utilities."""

from PIL import Image


def pixel_upscale(image: Image.Image, factor: int) -> Image.Image:
    """
    Upscale image by an integer factor without smoothing (nearest neighbor).

    Args:
        image: Source PIL image.
        factor: Upscale factor (must be a power of 2, e.g. 2, 4, 8).

    Returns:
        A new PIL image upscaled by the given factor.
    """
    if factor < 1 or factor & (factor - 1) != 0:
        msg = f"Invalid upscale factor: {factor}. Must be a power of 2."
        raise ValueError(msg)

    width, height = image.size
    new_size = (width * factor, height * factor)
    return image.resize(new_size, resample=Image.NEAREST)
