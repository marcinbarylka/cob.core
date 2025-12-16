"""Settings for the GUI."""

from __future__ import annotations


class Settings:
    """Settings for the game_gui GUI."""

    _instance: Settings | None = None

    def __new__(cls) -> "Settings":
        """Create a singleton instance of Settings."""
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """Initialize default settings."""
        self.width: int = 1024
        self.height: int = 768
        self.fps: int = 60
        self.font: str = "atarixl_standard.bdf"

        self.segment_size: tuple[int, int] = (75, 75)
