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
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
