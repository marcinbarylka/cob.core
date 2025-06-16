"""Panel widget for grouping other widgets in the GUI."""

from citadel_of_blood.gui.colors import ColorPair, ColorsEnum, WidgetColors
from citadel_of_blood.gui.widgets import BaseWidget
from citadel_of_blood.gui.widgets.mixins import PanelRendererMixin


class Panel(BaseWidget, PanelRendererMixin):
    """A simple panel widget that can contain other widgets.

    This class provides a container for other widgets, allowing them to be grouped
    together visually. It does not handle any specific events or interactions itself,
    but serves as a base for more complex panels.
    """

    _WIDGET_COLORS = WidgetColors(
        normal=ColorPair(
            foreground_color=ColorsEnum.PANEL_FOREGROUND,
            background_color=ColorsEnum.PANEL_BACKGROUND,
        ),
        hover=ColorPair(
            foreground_color=ColorsEnum.PIXEL_BUTTON_TEXT,
            background_color=ColorsEnum.PANEL_BACKGROUND,
        ),
        click=ColorPair(
            foreground_color=ColorsEnum.PANEL_FOREGROUND,
            background_color=ColorsEnum.PANEL_BACKGROUND,
        ),
    )

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        pattern: int = 2,
        *args,
        **kwargs,
    ) -> None:
        """Initialize the panel with a rectangle and color.

        Args:
            x (int): The x-coordinate of the panel.
            y (int): The y-coordinate of the panel.
            width (int): The width of the panel.
            height (int): The height of the panel.
            pattern (int): The index of the pattern to use for the panel.
                Defaults to 0, which corresponds to the first pattern.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        super().__init__(x, y, width, height, colors=self._WIDGET_COLORS, *args, **kwargs)
        # Initialize panel renderer logic
        self.init_panel_renderer(pattern)

    def draw(self) -> None:
        """Draw the panel via PanelRendererMixin."""
        self.render_panel()

    def on_hover_in(self) -> None:
        """Handle hover in event."""
        pass

    def on_hover_out(self) -> None:
        """Handle hover out event."""
        pass

    def update(self) -> None:
        """Update the panel state.

        This method can be overridden by subclasses to implement specific update logic.
        """
        pass

    def on_click(self) -> None:
        """Handle click event."""
        pass
