"""Specific consoles for the game GUI."""

import pygame
from bdfparser import Font
from tileconsole.console import BDFConsole

from citadel_of_blood import Exit
from citadel_of_blood.engine.segment import Segment
from citadel_of_blood.gui.colors import ColorsEnum
from citadel_of_blood.gui.settings import Settings


class SegmentConsole(BDFConsole):
    """Segment of the board."""

    def __init__(
            self,
            x: int,
            y: int,
            font: str | None = None,
            segment: Segment | None = None,
    ) -> None:
        """Initialize the segment console.

        Args:
            **kwargs: Additional keyword arguments for BDFConsole.

        """
        settings = Settings()

        # Determine font file to use for measuring character size
        if font is None:
            default_font_path = BDFConsole.get_default_font_path()
            font_file = f"{default_font_path}/{settings.font}"
        else:
            font_file = font

        super().__init__(
            x=x,
            y=y,
            width=settings.segment_size[0],
            height=settings.segment_size[1],
            font=font_file,
            foreground=ColorsEnum.BLACK,
            background=ColorsEnum.SEGMENT_BLUE,
            margin=(0, 0, 0, 0),
        )
        self.segment = segment

    def _init_surface(self):
        """Initialize the console surface."""
        # load font once and measure
        self.font = Font(self.font_file)
        char_w, char_h = self.measure_bdf(self.font_file)
        self.char_width = int(char_w)
        self.char_height = int(char_h)

        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(self.background)

    def render(self) -> None:
        """Render the segment console."""
        super().render()
        if self.segment is None:
            return

        # Draw segment representation (placeholder)
        self.clear()

        # Draw center
        for col in range(1, 4):
            for row in range(1, 4):
                self._draw_cell(col, row, ColorsEnum.WHITE)

        # Draw exits
        exits = self.segment.exits
        room_coords = {
            0: (2, 0),  # NORTH
            1: (4, 2),  # EAST
            2: (2, 4),  # SOUTH
            3: (0, 2),  # WEST
        }

        for i, ex in enumerate(exits):
            if ex == Exit.CORRIDOR:
                if i in (0, 2):  # NORTH or SOUTH -> horizontal corridor
                    row = 0 if i == 0 else 4
                    for col in range(1, 4):
                        self._draw_cell(col, row, ColorsEnum.WHITE)
                else:  # EAST or WEST -> vertical corridor
                    col = 4 if i == 1 else 0
                    for row in range(1, 4):
                        self._draw_cell(col, row, ColorsEnum.WHITE)
            elif ex in (Exit.ROOM, Exit.ROOM_CLOSED):
                col, row = room_coords[i]
                self._draw_cell(col, row, ColorsEnum.WHITE)

        self._changed = True

    def _draw_cell(self, col: int, row: int, color: pygame.Color) -> None:
        """Draw a single cell in the 5x5 grid.

        Args:
            col (int): Column index (0-4).
            row (int): Row index (0-4).
            color (pygame.Color): Color to fill the cell with.

        """
        cell_width = self.width // 5
        cell_height = self.height // 5
        rect = pygame.Rect(
            col * cell_width,
            row * cell_height,
            cell_width,
            cell_height,
        )
        pygame.draw.rect(self.surface, color, rect)
        self._draw_frame()

    def _draw_frame(self) -> None:
        """Draw the console frame."""
        pygame.draw.rect(
            self.surface,
            ColorsEnum.BLACK_OPACITY_50,
            self.surface.get_rect(),
            width=1,
        )

    def _draw_feature(self) -> None:
        """If the segment has a feature, draw it on the console."""
