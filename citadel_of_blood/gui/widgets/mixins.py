"""Mixins for the GUI widgets."""

import abc
from typing import Any, Protocol, runtime_checkable

import pygame
from pygame import Rect
from pygame.event import Event

from citadel_of_blood.gui.widgets import WidgetStateEnum


@runtime_checkable
class Clickable(Protocol):
    """Protocol defining the interface for clickable objects."""

    rect: Rect
    state: WidgetStateEnum

    def on_mouse_down(self) -> None:
        """Called when the mouse button is pressed over the widget."""
        ...

    def on_mouse_up(self) -> None:
        """Called when the mouse button is released."""
        ...

    def on_click(self) -> None:
        """Called when a valid click (down+up) is detected."""
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
        """Called when the mouse button is pressed over the widget."""

    @abc.abstractmethod
    def on_mouse_up(self) -> None:
        """Called when the mouse button is released."""

    @abc.abstractmethod
    def on_click(self) -> None:
        """Called when a valid click (down+up) is detected."""
