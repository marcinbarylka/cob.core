"""Settings for the GUI."""

import re
from pathlib import Path
from typing import Annotated, TypeVar

import platformdirs
import toml
from pydantic import BaseModel, Field, field_validator

from citadel_of_blood.constants import PROJECT_NAME
from citadel_of_blood.errors.gui_errors import InvalidHexColorError, NonPositiveDimensionError, NonPositiveFPSError

S = TypeVar("S", bound="Settings")


def validate_hex_color(v: str) -> str:
    """Validate hex color format."""
    if not re.match(r"^#[0-9a-fA-F]{6}$", v):
        raise InvalidHexColorError()
    return v


class GUIColors(BaseModel):
    """The colors for the GUI."""

    background: Annotated[str, Field(default="#000000", validator=validate_hex_color)]
    foreground: Annotated[str, Field(default="#ffffff", validator=validate_hex_color)]


class GUISettings(BaseModel):
    """The settings for the GUI."""

    fullscreen: bool = False
    width: int = 1920
    height: int = 1080
    caption: str = "Citadel of Blood"
    fps: int = 60
    colors: GUIColors
    basic_font: Path = Path("assets/fonts/Roboto-Regular.ttf")
    sfx_enabled: bool = True
    music_enabled: bool = True
    cache_folder: Path | str = Field(default_factory=lambda: Path(platformdirs.user_cache_path(PROJECT_NAME)))

    @field_validator("width", "height")
    @classmethod
    def validate_dimensions(cls, v: int) -> int:
        """Validate screen dimensions."""
        if v <= 0:
            raise NonPositiveDimensionError()
        return v

    @field_validator("fps")
    @classmethod
    def validate_fps(cls, v: int) -> int:
        """Validate FPS value."""
        if v <= 0:
            raise NonPositiveFPSError()
        return v


class Settings(BaseModel):
    """The settings."""

    gui: GUISettings

    @staticmethod
    def load(toml_file: str) -> "Settings":
        """Load the settings.

        Args:
            toml_file (str): The TOML file to load.

        Returns:
            Settings: The loaded settings.

        Raises:
            toml.TomlDecodeError: If the TOML file is invalid.
            pydantic.ValidationError: If the settings are invalid.
        """
        config_path = Path(platformdirs.user_config_path(PROJECT_NAME))
        try:
            with Path(config_path / toml_file).open("r") as f:
                toml_data = toml.load(f)
                return Settings(**toml_data)
        except FileNotFoundError:
            # Create a default settings file if it doesn't exist.
            return Settings.create_default_settings_conf(toml_file)

    @staticmethod
    def create_default_settings_conf(toml_file: str) -> "Settings":
        """Create a default settings file.

        Args:
            toml_file (str): The TOML file to create.

        Returns:
            Settings: The default settings.
        """
        settings = Settings(gui=GUISettings(colors=GUIColors()))
        config_path = Path(platformdirs.user_config_path(PROJECT_NAME))
        config_path.mkdir(parents=True, exist_ok=True)

        with Path(config_path / toml_file).open("w") as f:
            toml.dump(settings.model_dump(), f)
        return settings

    @staticmethod
    def create_cache_folder() -> Path:
        """Create the cache folder."""
        cache_path = Path(platformdirs.user_cache_path(PROJECT_NAME))
        cache_path.mkdir(parents=True, exist_ok=True)
        if not cache_path.exists():
            msg = f"Cache folder {cache_path} could not be created."
            raise FileNotFoundError(msg)
        # Ensure the cache folder is a Path object
        if isinstance(cache_path, str):
            cache_path = Path(cache_path)
        # save a placeholder file to ensure the folder is created
        placeholder_file = cache_path / "placeholder.txt"
        if not placeholder_file.exists():
            with placeholder_file.open("w") as f:
                f.write("This is a placeholder file to ensure the cache folder exists.")
        else:
            print(f"Cache folder already exists at {cache_path}.")
        return cache_path
