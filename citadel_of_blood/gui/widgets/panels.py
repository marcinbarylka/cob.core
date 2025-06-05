"""Panel widget for grouping other widgets in the GUI."""

import pygame

from citadel_of_blood.constants import PROJECT_ROOT
from citadel_of_blood.gui.colors import ColorPair, ColorsEnum, WidgetColors
from citadel_of_blood.gui.widgets import BaseWidget


class Panel(BaseWidget):
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

    _ASSET_PATHS = [
        PROJECT_ROOT / "assets/gui/pattern-0.png",
        PROJECT_ROOT / "assets/gui/pattern-1.png",
        PROJECT_ROOT / "assets/gui/pattern-2.png",
    ]

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
        self.pattern: int = pattern

    def draw(self) -> None:
        """Draw the panel on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the panel on.
        """
        pattern_surface = pygame.image.load(self._ASSET_PATHS[self.pattern]).convert_alpha()
        pattern_width, pattern_height = pattern_surface.get_size()
        color_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.surface, self.colors.normal.background_color, color_rect)

        # draw the panel pattern at the top-center of the panel
        pattern_x = self.x + (self.width - pattern_width) // 2
        pattern_y = 0
        if pattern_surface.get_alpha() is None:
            pattern_surface.set_alpha(255)

        self.surface.blit(pattern_surface, (pattern_x, pattern_y))

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
