"""Mixins for the GUI widgets."""

import abc
from typing import Any, Protocol, runtime_checkable

import pygame
from pygame import Rect
from pygame.event import Event

from citadel_of_blood.constants import PROJECT_ROOT
from citadel_of_blood.errors.gui_errors import PanelRendererError
from citadel_of_blood.gui.colors import ColorsEnum, WidgetColors
from citadel_of_blood.gui.graphics import load_pygame_image
from citadel_of_blood.gui.widgets import WidgetStateEnum


@runtime_checkable
class Clickable(Protocol):
    """Protocol defining the interface for clickable objects."""

    rect: Rect
    state: WidgetStateEnum

    def on_mouse_down(self) -> None:
        """Handle mouse button press over the widget."""
        ...

    def on_mouse_up(self) -> None:
        """Handle mouse button release."""
        ...

    def on_click(self) -> None:
        """Call when a valid click (down+up) is detected."""
        ...


class ClickableMixin(abc.ABC):
    """Mixin providing click-handling functionality.

    This mixin implements click event handling for widgets. The class using this mixin
    must implement the Clickable protocol, providing:
        - rect: pygame.Rect
        - state: WidgetStateEnum
        - on_mouse_down(), on_mouse_up(), on_click() methods
    """

    def handle_click_events(self: Any, events: list[Event]) -> None:
        """Process mouse click events.

        Args:
            events: List of pygame events to process

        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.on_mouse_down()
                    self.state = WidgetStateEnum.MOUSE_DOWN
            elif event.type == pygame.MOUSEBUTTONUP and self.state == WidgetStateEnum.MOUSE_DOWN:
                self.on_mouse_up()
                if self.rect.collidepoint(event.pos):
                    self.on_click()
                    self.state = WidgetStateEnum.MOUSE_UP

    @abc.abstractmethod
    def on_mouse_down(self) -> None:
        """Handle mouse button press over the widget."""

    @abc.abstractmethod
    def on_mouse_up(self) -> None:
        """Handle mouse button release."""

    @abc.abstractmethod
    def on_click(self) -> None:
        """Handle valid click (down+up) detection."""


class PanelRendererMixin:
    """Mixin providing panel rendering and resizing functionality."""

    # Attributes expected from BaseWidget
    x: int
    y: int
    width: int
    height: int
    surface: pygame.Surface
    colors: WidgetColors  # WidgetColors provided by BaseWidget

    # Panel rendering attributes
    _panel_rect: Rect
    _pattern_surface: pygame.Surface
    _pattern_width: int
    _pattern_height: int
    _line_left_img: pygame.Surface
    _line_right_img: pygame.Surface
    _line_left_width: int
    _line_left_height: int
    _line_right_width: int
    _pattern_x: int
    _pattern_y: int

    _ASSET_PATHS = {
        "p0": PROJECT_ROOT / "assets/gui/pattern-0.png",
        "p1": PROJECT_ROOT / "assets/gui/pattern-1.png",
        "p2": PROJECT_ROOT / "assets/gui/pattern-2.png",
        "line-left": PROJECT_ROOT / "assets/gui/line-left-32.png",
        "line-right": PROJECT_ROOT / "assets/gui/line-right-32.png",
    }

    _ASSETS: dict[str, pygame.Surface] = {}

    def init_panel_renderer(self: Any, pattern: int) -> None:
        """Initialize panel rendering assets and calculate layout based on size and pattern."""
        if pattern not in (0, 1, 2):
            raise PanelRendererError("invalid_pattern", f"Pattern {pattern} is not supported.")
        self.pattern = f"p{pattern}"

        # Load assets only once
        if not PanelRendererMixin._ASSETS:
            for key, path in PanelRendererMixin._ASSET_PATHS.items():
                PanelRendererMixin._ASSETS[key] = load_pygame_image(str(path)).convert_alpha()

        # Cache surfaces and dimensions
        self._pattern_surface = PanelRendererMixin._ASSETS[self.pattern]
        self._pattern_width, self._pattern_height = self._pattern_surface.get_size()
        self._line_left_img = PanelRendererMixin._ASSETS["line-left"]
        self._line_right_img = PanelRendererMixin._ASSETS["line-right"]
        self._line_left_width = self._line_left_img.get_width()
        self._line_left_height = self._line_left_img.get_height()
        self._line_right_width = self._line_right_img.get_width()

    def render_panel(self) -> None:
        """Render the panel onto its surface."""
        # Calculate panel rectangle and pattern position for current size
        self._panel_rect = pygame.Rect(self.x, self.y, self.width, self.height - self._pattern_height // 2)
        self._pattern_x = self.x + (self.width - self._pattern_width) // 2
        self._pattern_y = self.y
        # Clear the surface
        self.surface.fill((0, 0, 0, 0))

        # Draw panel background
        bg_rect = (
            self._panel_rect.x,
            self._panel_rect.y + self._pattern_height // 4,
            self._panel_rect.width,
            self._panel_rect.height,
        )
        pygame.draw.rect(
            self.surface,
            self.colors.normal.background_color,
            bg_rect,
        )

        # Calculate border positions
        top_y = self._panel_rect.y + self._pattern_height // 4
        bottom_y = self._panel_rect.y + self._panel_rect.height + self._line_left_height * 2
        left_x = self._panel_rect.x
        right_x = self._panel_rect.x + self._panel_rect.width - self._line_right_width

        # Draw borders
        self._draw_horizontal_border(top_y, left_x, right_x)
        self._draw_horizontal_border(bottom_y, left_x, right_x)

        # Draw panel pattern at top-center
        self.surface.blit(self._pattern_surface, (self._pattern_x, self._pattern_y))

    def _draw_horizontal_border(self, y_pos: int, left_x: int, right_x: int) -> None:
        """Draw horizontal border segments.

        Args:
            y_pos (int): The vertical position to draw the border.
            left_x (int): The x-coordinate for the left border segment.
            right_x (int): The x-coordinate for the right border segment.

        Raises:
            PanelRendererError: If the left or right x-coordinates are invalid.

        """
        # Draw corners
        self.surface.blit(self._line_left_img, (left_x, y_pos))
        self.surface.blit(self._line_right_img, (right_x, y_pos))
        # Draw connecting line
        pygame.draw.line(
            self.surface,
            ColorsEnum.FADING_BAR,
            (left_x + self._line_left_width, y_pos),
            (right_x, y_pos),
            2,
        )
