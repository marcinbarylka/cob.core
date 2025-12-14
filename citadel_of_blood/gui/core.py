"""Core module."""

import pygame

from citadel_of_blood.gui.settings import Settings


class Game:
    """Core class for the game GUI."""

    def __init__(self) -> None:
        """Initialize the game core."""
        self.settings = Settings()
        self.surface: pygame.Surface | None = None
        self.clock = pygame.time.Clock()
        self.running = True

        self.console_manager = None  # Placeholder for ConsoleManager

    def init_gui(self) -> None:
        """Initialize the GUI."""
        pygame.init()
        self.surface = pygame.display.set_mode(
            (self.settings.width, self.settings.height)
        )
        pygame.display.set_caption("Citadel of Blood")

    def run(self) -> None:
        """Run the main game loop."""
        if not pygame.get_init():
            # todo: proper exception handling
            raise RuntimeError("Pygame is not initialized. Call init_gui() first.")

        while self.running:
            dt_ms = self.clock.tick(60)
            dt = dt_ms / 1000.0
            events = pygame.event.get()
            # Forward events through the ConsoleManager (it returns the events list)
            # Per-frame update with delta seconds
            pygame.display.update()

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
        pygame.quit()
