"""A modal dialog widget for displaying messages or prompts in the GUI."""

import pygame

from citadel_of_blood.gui.colors import DEFAULT_WIDGET_COLORS
from citadel_of_blood.gui.widgets import BaseWidget


class Modal(BaseWidget):
    """A modal dialog widget that can be used to display messages or prompts.

    This widget is typically used to interrupt the normal flow of the application
    and require user interaction before proceeding.
    """

    def __init__(self, title: str, message: str, width: int = 400, height: int = 200):
        """Initialize the Modal widget."""
        super().__init__(x=0, y=0, width=width, height=height, colors=DEFAULT_WIDGET_COLORS)
        self.title = title
        self.message = message
        self.is_visible = True
        # Initialize the surface for the modal dialog
        # We need to create a surface that matches the GUI dimensions, because modals typically cover the entire screen
        self.surface = pygame.Surface((self.settings.gui.width, self.settings.gui.height), pygame.SRCALPHA)

    def show(self) -> None:
        """Display the modal dialog."""
        self.is_visible = True

    def hide(self) -> None:
        """Hide the modal dialog."""
        self.is_visible = False

    def draw(self) -> None:
        """Draw the modal dialog if it is visible."""
        if not self.is_visible:
            return
        # Draw the modal background
        pygame.draw.rect(self.surface, (0, 0, 0, 128), (0, 0, self.settings.gui.width, self.settings.gui.height))

        # Draw the modal border
        # pygame.draw.rect(self.surface, (255, 255, 255), (self.x, self.y, self.width, self.height), 2)
        # Draw the title
        # title_surface = self.settings.gui.default_font_path.render(self.title, True, (255, 255, 255))
        # self.surface.blit(title_surface, (self.x + 10, self.y + 10))
        # Draw the message
        # message_surface = self.settings.font.render(self.message, True, (255, 255, 255))
        # self.surface.blit(message_surface, (self.x + 10, self.y + 40))
        # Draw the modal content
        # This can be extended to include buttons or other interactive elements
        # For now, we just draw a simple message
        # pygame.draw.rect(self.surface, (50, 50, 50), (self.x + 10, self.y + 70, self.width - 20, self.height - 90))
        # self.surface.blit(message_surface, (self.x + 10, self.y + 70))

    def on_hover_out(self) -> None:
        """Handle hover out event."""
        # No specific action needed for modal, but can be overridden if needed
        pass

    def on_click(self) -> None:
        """Handle click event."""
        # No specific action needed for modal, but can be overridden if needed
        pass

    def on_hover_in(self) -> None:
        """Handle hover event."""
        # No specific action needed for modal, but can be overridden if needed
        pass

    def update(self) -> None:
        """Update the modal state."""
        # No specific update logic needed for modal, but can be overridden if needed
        pass
