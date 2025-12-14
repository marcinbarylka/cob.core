"""Specific consoles for the game GUI."""

from tileconsole.console import BDFConsole

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

        # Measure character size before calling super().__init__ (self.char_width not set yet)
        char_width, char_height = BDFConsole.measure_bdf(font_file)

        super().__init__(
            x=x,
            y=y,
            width=settings.segment_size[0] // char_width,
            height=settings.segment_size[1] // char_height,
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
        for x in range(5):  # type: ignore[union-attr]
            for y in range(5):  # type: ignore[union-attr]
                ...

        self._changed = True
