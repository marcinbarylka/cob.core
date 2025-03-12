"""Settings for the GUI."""

import tomllib
from pathlib import Path
from typing import TypeVar

import platformdirs
import toml
from pydantic import BaseModel

from citadel_of_blood.constants import PROJECT_NAME

S = TypeVar("S", bound="Settings")


class GUIColors(BaseModel):
    """The colors for the GUI."""

    background: str = "#000000"
    foreground: str = "#ffffff"


class GUISettings(BaseModel):
    """The settings for the GUI."""

    fullscreen: bool = False
    width: int = 1920
    height: int = 1080
    caption: str = "Citadel of Blood"
    fps: int = 60
    colors: GUIColors


class Settings(BaseModel):
    """The settings."""

    gui: GUISettings

    @staticmethod
    def load(toml_file: str) -> S:
        """Load the settings.

        Args:
            toml_file (str): The TOML file to load.

        """
        config_path = Path(platformdirs.user_config_path(PROJECT_NAME))
        try:
            with Path(config_path / toml_file).open("rb") as f:
                toml_data = tomllib.load(f)
                settings = Settings(**toml_data)
        except FileNotFoundError:
            settings = Settings.create_default_settings_conf(toml_file)
        return settings

    @staticmethod
    def create_default_settings_conf(toml_file: str) -> S:
        """Create a default settings file."""
        settings = Settings(gui=GUISettings(colors=GUIColors()))
        config_path = Path(platformdirs.user_config_path(PROJECT_NAME))
        if not Path(config_path).exists():
            Path(config_path).mkdir(parents=True)
        with Path(config_path / toml_file).open("w") as f:
            toml.dump(settings.model_dump(), f=f)
        return settings
