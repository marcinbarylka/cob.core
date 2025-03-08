"""Settings for the GUI."""

import tomllib
from pathlib import Path

from pydantic import BaseModel


class GUIColors(BaseModel):
    """The colors for the GUI."""

    background: str = "#000000"
    foreground: str = "#ffffff"


class GUISettings(BaseModel):
    """The settings for the GUI.

    Attributes
    ----------
        fullscreen (bool): Whether to run in fullscreen mode.
        width (int): The width of the window.
        height (int): The height of the window.
        caption (str): The caption of the window.
        fps (int): The frames per second.
        colors (GUIColors): The colors.

    """

    fullscreen: bool = False
    width: int = 0
    height: int = 0
    caption: str = "GUI"
    fps: int = 60
    colors: GUIColors


class Settings(BaseModel):
    """The settings.

    Attributes
    ----------
        gui (GUISettings): The GUI settings.

    """

    gui: GUISettings

    @staticmethod
    def load(toml_file: str) -> "Settings":
        """Load the settings.

        Args:
        ----
            toml_file (str): The TOML file to load.

        Returns:
        -------
            Settings: The settings.

        """
        with Path.open(toml_file, "rb") as f:
            return Settings(**tomllib.load(f))
