"""A modal dialog widget for displaying messages or prompts in the GUI."""

import pygame

from citadel_of_blood.gui.colors import DEFAULT_WIDGET_COLORS, ColorsEnum
from citadel_of_blood.gui.widgets import BaseWidget
from citadel_of_blood.gui.widgets.buttons import Button


class Modal(BaseWidget):
    """A modal dialog widget that can be used to display messages or prompts.

    This widget is typically used to interrupt the normal flow of the application
    and require user interaction before proceeding.
    """

    def __init__(self, title: str, message: str, width: int = 400, height: int = 200, buttons: list[str] | None = None):
        """Initialize the Modal widget."""
        super().__init__(x=0, y=0, width=width, height=height, colors=DEFAULT_WIDGET_COLORS)
        self.title = title
        self.message = message
        self.is_visible = True
        # Initialize the surface for the modal dialog
        self.surface = pygame.Surface((self.settings.gui.width, self.settings.gui.height), pygame.SRCALPHA)
        # Setup buttons
        self.button_labels = buttons or ["OK"]
        self.button_widgets: list[Button] = []
        self._init_buttons()

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
        # Draw the modal background overlay
        pygame.draw.rect(
            self.surface, ColorsEnum.MODAL_BACKGROUND, (0, 0, self.settings.gui.width, self.settings.gui.height)
        )

        # Draw the modal border
        # pygame.draw.rect(self.surface, (255, 255, 255), (self.x, self.y, self.width, self.height), 2)
        # Draw the title and message (omitted for brevity)
        # Draw buttons
        for btn in self.button_widgets:
            btn.update()
            btn.draw()
            self.surface.blit(btn.surface, (btn.x, btn.y))

    def on_hover_out(self) -> None:
        """Handle hover out event."""
        # No specific action needed for modal, but can be overridden if needed
        pass

    def on_click(self) -> None:
        """Handle click event."""
        # No specific action needed for modal, but can be overridden if needed
        pass

    def handle_events(self, events: list[pygame.event.Event]) -> None:
        """Propagate events to modal and its buttons."""
        if not self.is_visible:
            return
        # Handle hover for modal itself
        super().handle_events(events)
        # Delegate events to buttons
        for btn in self.button_widgets:
            btn.handle_events(events)

    def update(self) -> None:
        """Update modal and button states."""
        for btn in self.button_widgets:
            btn.update()

    def _init_buttons(self) -> None:
        """Initialize Button widgets based on labels."""
        # Layout buttons centered at bottom of modal
        btn_w, btn_h, spacing = 80, 30, 10
        count = len(self.button_labels)
        total_w = count * btn_w + (count - 1) * spacing
        start_x = (self.settings.gui.width - total_w) // 2
        y = (self.settings.gui.height + self.height) // 2 - btn_h - 20
        for i, label in enumerate(self.button_labels):
            x = start_x + i * (btn_w + spacing)
            btn = Button(x, y, btn_w, btn_h, DEFAULT_WIDGET_COLORS, caption=label)
            self.button_widgets.append(btn)

    def on_hover_in(self) -> None:
        """Handle hover in event."""
        # No specific action needed for modal, but can be overridden if needed
        pass

    def on_click(self) -> None:
        """Handle click event."""
        # No specific action needed for modal, but can be overridden if needed
        pass
