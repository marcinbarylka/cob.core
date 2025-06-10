"""Sound effects and music."""

import pygame


def init_sfx() -> None:
    """Initialize the sound effects and music system."""
    pygame.mixer.init()
    pygame.mixer.set_num_channels(8)  # Set the number of channels for sound effects
    pygame.mixer.music.set_volume(0.5)  # Set the volume for background music
    pygame.mixer.set_reserved(1)  # Reserve a channel for sound effects or special use


def play_sfx(sfx: str) -> None:
    """Play a sound effect.

    Args:
        sfx: The path to the sound effect file
    """
    pygame.mixer.Sound(sfx).play()


def play_music(music: str) -> None:
    """Play a background music.

    Args:
        music: The path to the music file
    """
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)
