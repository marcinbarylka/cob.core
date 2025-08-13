"""A modal dialog widget for displaying messages or prompts in the GUI."""

import pygame

from citadel_of_blood.gui.colors import ColorPair, ColorsEnum, WidgetColors
from citadel_of_blood.gui.settings import Settings
from citadel_of_blood.gui.widgets import BaseWidget
from citadel_of_blood.gui.widgets.buttons import Button
from citadel_of_blood.gui.widgets.mixins import PanelRendererMixin

# Colors for the panel rendered inside the modal
PANEL_WIDGET_COLORS = WidgetColors(
    normal=ColorPair(background_color=ColorsEnum.PANEL_BACKGROUND, foreground_color=ColorsEnum.PANEL_FOREGROUND)
)


class Modal(PanelRendererMixin, BaseWidget):
    """A modal dialog widget that can be used to display messages or prompts."""

    def __init__(self, title: str, message: str, width: int = 400, height: int = 200, buttons: list[str] | None = None):
        """Initialize the Modal widget."""
        settings = Settings.instance()
        # Full-screen overlay (fills the screen)
        super().__init__(x=0, y=0, width=settings.gui.width, height=settings.gui.height, colors=PANEL_WIDGET_COLORS)

        # Inner panel geometry
        self.panel_width = width
        self.panel_height = height
        self.panel_x = (self.width - self.panel_width) // 2
        self.panel_y = (self.height - self.panel_height) // 2

        self.title = title
        self.message = message
        self.is_visible = False

        # Load panel assets once
        self.init_panel_renderer(pattern=2)

        # Buttons
        self.button_labels = buttons or ["OK"]
        self.button_widgets: list[Button] = []

        # Prepare overlay and buttons
        self.initialize_surface()
        self._init_buttons()

    def initialize_surface(self) -> None:
        """Initialize or refresh the full-screen dimmed overlay surface."""
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.surface.fill(ColorsEnum.MODAL_BACKGROUND)

    def show(self) -> None:
        """Show the modal dialog."""
        self.is_visible = True

    def hide(self) -> None:
        """Hide the modal dialog."""
        self.is_visible = False

    def draw(self) -> None:
        """Draw the modal dialog."""
        if not self.is_visible:
            return

        # Redraw dimmed background every frame (in case of other draws)
        self.surface.fill(ColorsEnum.MODAL_BACKGROUND)

        # Render panel to a temporary surface to avoid clearing the overlay
        panel_surface = pygame.Surface((self.panel_width, self.panel_height), pygame.SRCALPHA)

        # Backup geometry and surface
        _backup = (self.surface, self.x, self.y, self.width, self.height)
        try:
            self.surface = panel_surface
            self.x = 0
            self.y = 0
            self.width = self.panel_width
            self.height = self.panel_height
            self.render_panel()
        finally:
            self.surface, self.x, self.y, self.width, self.height = _backup

        # Blit the panel onto the overlay at centered position
        self.surface.blit(panel_surface, (self.panel_x, self.panel_y))

        # Draw buttons on top
        for btn in self.button_widgets:
            btn.draw()
            self.surface.blit(btn.surface, (btn.x, btn.y))

    def on_hover_in(self) -> None:
        """Handle hover in event for modal overlay (no-op)."""
        pass

    def on_hover_out(self) -> None:
        """Handle hover out event for modal overlay (no-op)."""
        pass

    def on_click(self) -> None:
        """Handle click on modal overlay (no-op)."""
        pass

    def handle_events(self, events: list[pygame.event.Event]) -> None:
        """Handle events for the modal dialog."""
        if not self.is_visible:
            return
        super().handle_events(events)
        for btn in self.button_widgets:
            btn.handle_events(events)

    def update(self) -> None:
        """Update the modal dialog."""
        for btn in self.button_widgets:
            btn.update()

    def _init_buttons(self) -> None:
        # Layout buttons centered at bottom of the inner panel
        btn_w, btn_h, spacing = 80, 30, 10
        count = len(self.button_labels)
        total_w = count * btn_w + (count - 1) * spacing
        start_x = self.panel_x + (self.panel_width - total_w) // 2
        y = self.panel_y + self.panel_height - btn_h - 20
        for i, label in enumerate(self.button_labels):
            x = start_x + i * (btn_w + spacing)
            btn = Button(x, y, btn_w, btn_h, PANEL_WIDGET_COLORS, caption=label)
            self.button_widgets.append(btn)
