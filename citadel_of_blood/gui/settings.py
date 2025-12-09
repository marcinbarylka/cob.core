"""Settings for the GUI."""


class Settings:
    """Settings for the game GUI."""

    def __init__(self) -> None:
        """Initialize default settings."""
        self.width: int = 1024
        self.height: int = 768
        self.fps: int = 60
        self.font: str = "atarixl_standard.bdf"
