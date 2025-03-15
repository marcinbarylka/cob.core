"""Helper functions for the GUI module."""

import pygame


def serialize_surface(surface: pygame.Surface) -> dict:
    """Serialize a pygame surface to dict.

    Args:
        surface (pygame.Surface): The surface to serialize.

    Returns:
        dict: The serialized surface.
    """
    return {
        "size": surface.get_size(),
        "flags": surface.get_flags(),
        "depth": surface.get_bitsize(),
    }


def deserialize_surface(surface: dict) -> pygame.Surface:
    """Deserialize a pygame surface from dict.

    Args:
        surface (dict): The serialized surface.

    Returns:
        pygame.Surface: The deserialized surface.

    """
    return pygame.Surface(surface["size"], surface["flags"], surface["depth"])
