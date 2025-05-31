"""Module for all widgets used in the GUI."""

from typing import TYPE_CHECKING

from citadel_of_blood.gui.widgets.base import BaseWidget, WidgetStateEnum
from citadel_of_blood.gui.widgets.buttons import Button, GothicButton
from citadel_of_blood.gui.widgets.mixins import ClickableMixin

if TYPE_CHECKING:
    from pygame import Surface
    from pygame.event import Event

__all__ = [
    "BaseWidget",
    "Button",
    "GothicButton",
    "ClickableMixin",
    "WidgetStateEnum",
    "Surface",
    "Event",
]
