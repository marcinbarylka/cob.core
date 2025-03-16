"""Event handling for the GUI."""

import pygame


class EventsHandler:
    """Handles events for the GUI."""

    def __init__(self) -> None:
        """Initialize the EventsHandler class."""
        self.running: bool = True

    def handle_events(self, events: list[pygame.event.Event] | None = None) -> list[pygame.event.Event]:
        """Handle the events."""
        if not events:
            events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown_event(event)
        return events

    def _handle_keydown_event(self, event) -> None:
        """Handle keyboard events.

        Args:
            event: Pygame keyboard event.

        """
        if event.key == pygame.K_ESCAPE:
            self.running = False
        # Handle other keyboard events here
