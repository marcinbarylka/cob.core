"""Specific consoles for the game GUI."""

import pygame
from bdfparser import Font
from tileconsole.console import BDFConsole

from citadel_of_blood import Exit
from citadel_of_blood.engine.segment import Segment
from citadel_of_blood.gui.colors import ColorsEnum
from citadel_of_blood.gui.settings import Settings
from engine.map import Board


class FontInitMixin:
    """Mixin for consoles that represent map segments."""

    def _init_font(self, font: str | None) -> str:
        """Initialize the font for the console.

        Args:
            font (str | None): Font file to use. If None, use default font from settings.

        Returns:
            str: Font file path.
        """

        settings = Settings()
        if font is None:
            default_font_path = BDFConsole.get_default_font_path()
            font_file = f"{default_font_path}/{settings.font}"
        else:
            font_file = font

        return font_file

    def _init_surface(self):
        """Initialize the console surface."""
        # load font once and measure
        self.font = Font(self.font_file)
        char_w, char_h = self.measure_bdf(self.font_file)
        self.char_width = int(char_w)
        self.char_height = int(char_h)

        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(self.background)


class SegmentConsole(FontInitMixin, BDFConsole):
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
            x (int): X position of the console.
            y (int): Y position of the console.
            font (str | None): Font file to use. If None, use default font from settings.
            segment (Segment | None): Segment to represent. If None, no segment is drawn.

        """
        settings = Settings()
        font_file = self._init_font(font)

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

        feature = self._draw_feature()
        if feature:
            self.surface.blit(
                feature,
                (
                    (self.width - feature.get_width()) // 2,
                    (self.height - feature.get_height()) // 2,
                ),
            )

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
        # self._draw_frame()

    def _draw_frame(self) -> None:
        """Draw the console frame."""
        pygame.draw.rect(
            self.surface,
            ColorsEnum.BLACK_OPACITY_50,
            self.surface.get_rect(),
            width=1,
        )

    def _draw_feature(self) -> pygame.Surface | None:
        """If the segment has a feature, draw it on the console.

        Returns:
            pygame.Surface | None: Surface with the feature drawn, or None if no feature.

        """
        if self.segment is not None:
            if hasattr(self.segment, "feature") and self.segment.feature is not None:
                feature = self.segment.feature
                if feature is not None:
                    glyph = self.font.glyph(feature.symbol.value).draw().bindata
                    char_surface = pygame.Surface((self.char_width, self.char_height))
                    char_surface.fill(ColorsEnum.WHITE)
                    for gy in range(self.char_height):
                        for gx in range(self.char_width):
                            if glyph[gy][gx] == "1":  # pixel is set
                                char_surface.set_at((gx, gy), ColorsEnum.BLACK)
                    return char_surface
        return


class BoardConsole(FontInitMixin, BDFConsole):
    """Map console."""

    def __init__(
            self,
            x: int,
            y: int,
            width: int,
            height: int,
            font: str | None = None,
            level: int = 0,
            board: Board | None = None,
    ) -> None:
        """Initialize the map console.

        Args:
            x (int): X position of the console.
            y (int): Y position of the console.
            width (int): Width of the console.
            height (int): Height of the console.
            font (str | None): Font file to use. If None, use default font from settings.

        """
        font_file = self._init_font(font)
        super().__init__(
            x=x,
            y=y,
            width=width,
            height=height,
            font=font_file,
            foreground=ColorsEnum.WHITE,
            background=ColorsEnum.GRAY,
            margin=(0, 0, 0, 0),
        )
        self.level = level
        self.board = board

    def render(self) -> None:
        """Render the map console."""
        # super().render()
        if self.board is None:
            return

        self.clear()

        settings = Settings()

        # Placeholder: Draw segments in a grid
        # get the segments from the board and draw them (but only those on the current level)
        # the level is represented by the Z coordinate in the position tuple

        level_map = {
            pos: seg for pos, seg in self.board.map.items() if pos[2] == self.level
        }

        for position, segment in level_map.items():
            x = position[0] * settings.segment_size[0]  # Offset to center
            y = position[1] * settings.segment_size[1]  # Offset to center

            # Draw segment representation (simple square)
            segment_console = SegmentConsole(
                x=0,
                y=0,
                segment=segment,
            )
            segment_console.render()
            self.surface.blit(segment_console.surface, (x, y))

        self._changed = True
