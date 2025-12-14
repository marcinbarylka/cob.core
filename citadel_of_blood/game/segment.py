"""Segment GUI module for Citadel of Blood game engine."""

import pygame

from citadel_of_blood.engine.segment import Segment
from citadel_of_blood.gui.settings import Settings


class SegmentGUI(Segment):
    def __init__(
        self, exits: list[int] | None, surface: pygame.Surface | None = None
    ) -> None:
        """Initialize the segment for GUI.

        Args:
            exits: list of exits of the segment

        """
        super().__init__(exits)
        self.settings = Settings()
        if not surface:
            self.surface = pygame.Surface(self.settings.segment_size)
    # Default size

    def render(self):
        """Render the segment for GUI display.

        Returns:
            A string representation of the segment for GUI.

        """
