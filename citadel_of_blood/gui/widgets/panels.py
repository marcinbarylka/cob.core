"""Panel widget for grouping other widgets in the GUI."""

import pygame

from citadel_of_blood.constants import PROJECT_ROOT
from citadel_of_blood.gui.colors import ColorPair, ColorsEnum, WidgetColors
from citadel_of_blood.gui.graphics import load_pygame_image
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

    _ASSET_PATHS = {
        "p0": PROJECT_ROOT / "assets/gui/pattern-0.png",
        "p1": PROJECT_ROOT / "assets/gui/pattern-1.png",
        "p2": PROJECT_ROOT / "assets/gui/pattern-2.png",
        "line-left": PROJECT_ROOT / "assets/gui/line-left-32.png",
        "line-right": PROJECT_ROOT / "assets/gui/line-right-32.png",
    }

    # Preload assets to avoid loading during draw
    _ASSETS = {}

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
        if pattern not in (0, 1, 2):
            msg = f"Pattern {pattern} is not supported."
            raise ValueError(msg)
        self.pattern: str = f"p{pattern}"

        # Load assets only once
        if not Panel._ASSETS:
            for key, path in self._ASSET_PATHS.items():
                Panel._ASSETS[key] = load_pygame_image(path).convert_alpha()

        # Cache dimensions
        self._pattern_surface = Panel._ASSETS[self.pattern]
        self._pattern_width, self._pattern_height = self._pattern_surface.get_size()
        self._line_left_img = Panel._ASSETS["line-left"]
        self._line_right_img = Panel._ASSETS["line-right"]
        self._line_left_width = self._line_left_img.get_width()
        self._line_left_height = self._line_left_img.get_height()
        self._line_right_width = self._line_right_img.get_width()

        # Precalculate some positions
        self._panel_rect = pygame.Rect(self.x, self.y, self.width, self.height - self._pattern_height // 2)
        self._pattern_x = self.x + (self.width - self._pattern_width) // 2
        self._pattern_y = 0

        # cache kolorów i pozycji granic
        self._bg_color = self.colors.normal.background_color
        self._fade_color = ColorsEnum.FADING_BAR
        self._top_y = self._panel_rect.y + self._pattern_height // 4
        self._bottom_y = self._panel_rect.y + self._panel_rect.height + self._line_left_height * 2
        self._left_x = self._panel_rect.x
        self._right_x = self._panel_rect.x + self._panel_rect.width - self._line_right_width

    def draw(self) -> None:
        """Draw the panel on the given surface."""
        # clear the surface
        self.surface.fill((0, 0, 0, 0))

        # tło panela
        pygame.draw.rect(
            self.surface,
            self._bg_color,
            (self._left_x, self._top_y, self._panel_rect.width, self._panel_rect.height),
        )

        # górna krawędź
        self.surface.blit(self._line_left_img, (self._left_x, self._top_y))
        self.surface.blit(self._line_right_img, (self._right_x, self._top_y))
        pygame.draw.line(
            self.surface,
            self._fade_color,
            (self._left_x + self._line_left_width, self._top_y),
            (self._right_x, self._top_y),
            2,
        )

        # dolna krawędź
        self.surface.blit(self._line_left_img, (self._left_x, self._bottom_y))
        self.surface.blit(self._line_right_img, (self._right_x, self._bottom_y))
        pygame.draw.line(
            self.surface,
            self._fade_color,
            (self._left_x + self._line_left_width, self._bottom_y),
            (self._right_x, self._bottom_y),
            2,
        )

        # wzorek na środku
        self.surface.blit(self._pattern_surface, (self._pattern_x, self._pattern_y))

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
