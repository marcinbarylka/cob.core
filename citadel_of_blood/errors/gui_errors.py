"""GUI errors."""


class InvalidHexColorError(ValueError):
    """Raised when a hex color format is invalid."""

    def __init__(self) -> None:
        """Initialize the InvalidHexColorError class."""
        super().__init__("Invalid hex color format")


class NonPositiveDimensionError(ValueError):
    """Raised when a dimension value is not positive."""

    def __init__(self) -> None:
        """Initialize the NonPositiveDimensionError class."""
        super().__init__("Dimensions must be positive")


class NonPositiveFPSError(ValueError):
    """Raised when FPS value is not positive."""

    def __init__(self) -> None:
        """Initialize the NonPositiveFPSError class."""
        super().__init__("FPS must be positive")
