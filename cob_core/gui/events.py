"""Event handling for the GUI."""

import pygame


class EventsHandler:
    """Handles events for the GUI."""

    def __init__(self) -> None:
        """Initialize the EventsHandler class."""
        self.running: bool = True

    def handle_events(self) -> None:
        """Handle the events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown_event(event)

    def _handle_keydown_event(self, event) -> None:
        """Handle keyboard events.

        Args:
            event: Pygame keyboard event.
        """
        if event.key == pygame.K_ESCAPE:
            self.running = False
        # Handle other keyboard events here
