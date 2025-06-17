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


class ScreenError(Exception):
    """Base class for screen-related errors."""

    ERROR_MESSAGES = {
        "widget_initialization_failed": "Failed to initialize widgets: {error}",
    }

    def __init__(self, error_type: str, error: Exception | str) -> None:
        """Initialize the ScreenError class."""
        message = self.ERROR_MESSAGES[error_type].format(error=error)
        super().__init__(message)


class WidgetError(Exception):
    """Base class for widget-related errors."""

    ERROR_MESSAGES = {
        "invalid_dimensions": "Invalid dimensions: {error}",
        "invalid_colors": "Invalid colors: {error}",
        "missing_required_field": "Missing required field: {error}",
        "deserialization_failed": "Failed to deserialize widget: {error}",
        "surface_deserialization_failed": "Failed to deserialize surface: {error}",
        "asset_loading_failed": "Failed to load asset: {error}",
        "asset_not_found": "Asset not found: {error}",
        "font_initialization_failed": "Failed to initialize font: {error}",
    }

    def __init__(self, error_type: str, error: Exception | str) -> None:
        """Initialize the WidgetError class."""
        message = self.ERROR_MESSAGES[error_type].format(error=error)
        super().__init__(message)


class ColorError(Exception):
    """Base class for color-related errors."""

    ERROR_MESSAGES = {
        "invalid_color": "Invalid color: {error}",
        "color_not_found": "Color not found: {error}",
        "color_serialization_failed": "Failed to serialize color: {error}",
        "color_deserialization_failed": "Failed to deserialize color: {error}",
        "invalid_color_pair": "Invalid color pair: {error}",
        "color_depth_mismatch": "Color depth mismatch: {error}",
    }

    def __init__(self, error_type: str, error: Exception | str) -> None:
        """Initialize the ColorError class."""
        message = self.ERROR_MESSAGES[error_type].format(error=error)
        super().__init__(message)
