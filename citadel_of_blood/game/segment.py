"""Segment GUI module for Citadel of Blood game engine."""

import pygame

from citadel_of_blood.engine.segment import Segment


class SegmentGUI(Segment):
    def __init__(
        self, exits: list[int] | None, surface: pygame.Surface | None = None
    ) -> None:
        """Initialize the segment for GUI.

        Args:
            exits: list of exits of the segment

        """
        super().__init__(exits)

    def render(self):
        """Render the segment for GUI display.

        Returns:
            A string representation of the segment for GUI.

        """
