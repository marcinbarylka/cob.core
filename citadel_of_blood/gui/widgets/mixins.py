"""Mixins for the GUI widgets."""

import abc

import pygame


class ClickableMixin(abc.ABC):
    """Mixin providing click-handling functionality.
    It assumes that the class has attributes:
      - rect: pygame.Rect
      - _pressed: bool
      - on_mouse_down(), on_mouse_up(), on_click().
    """

    def __init__(self) -> None:
        """Initialize the ClickableMixin class."""
        self._pressed: bool = False

    def handle_click_events(self, events: list[pygame.event.Event]) -> None:
        """Processes mouse click events."""
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.on_mouse_down()
                    self._pressed = True
            elif event.type == pygame.MOUSEBUTTONUP and self._pressed:
                self.on_mouse_up()
                if self.rect.collidepoint(event.pos):
                    self.on_click()
                self._pressed = False

    @abc.abstractmethod
    def on_mouse_down(self) -> None:
        """Called when the mouse button is pressed over the widget."""
        raise NotImplementedError

    @abc.abstractmethod
    def on_mouse_up(self) -> None:
        """Called when the mouse button is released."""
        raise NotImplementedError

    @abc.abstractmethod
    def on_click(self) -> None:
        """Called when a valid click (down+up) is detected."""
        raise NotImplementedError
