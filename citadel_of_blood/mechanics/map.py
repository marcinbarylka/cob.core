"""Game map module."""

from citadel_of_blood import Axis, Direction, Exit
from citadel_of_blood.mechanics import dice
from citadel_of_blood.mechanics.monsters import Monster
from citadel_of_blood.mechanics.segment import GatewayOfEvil, Room, Segment


class Board:
    """Board class. It is responsible for rendering the board and moving the party counter. It also stores the map and
    monsters.
    """

    def __init__(self) -> None:
        """Initialize the Board class."""
        self.map: dict[tuple[int, int, int], Segment] = {(0, 0, 0): GatewayOfEvil()}
        self.monsters: dict[tuple[int, int, int], Monster] = {}
        self.party_position: tuple[int, int, int] = (0, 0, 0)

    def get_adjacent_segment_exits(self, position: tuple[int, int, int]) -> list[int]:
        """Get exits of the segments adjacent to the segment at given position.

        Args:
            position: position of the segment

        Returns:
            list of exits of the adjacent segments

        """
        directions = [Direction.north.value, Direction.east.value, Direction.south.value, Direction.west.value]
        opposite_directions = [Direction.south.value, Direction.west.value, Direction.north.value, Direction.east.value]
        offsets = [(0, -1, 0), (1, 0, 0), (0, 1, 0), (-1, 0, 0)]

        exits = [Exit.undefined for _ in directions]

        for i, (dx, dy, dz) in enumerate(offsets):
            neighbor_position = (position[Axis.x.value] + dx, position[Axis.y.value] + dy, position[Axis.z.value] + dz)
            neighbor_segment = self.map.get(neighbor_position)

            if neighbor_segment:
                exits[i] = neighbor_segment.exits[opposite_directions[i]]

        return exits

    def get_segment(self, position: tuple[int, int, int]) -> Segment:
        """Get segment at given position. If there is no segment at given position, then it is created.

        Args:
            position: position of the segment

        Returns:
            segment at given position

        """
        if position not in self.map:
            exits = self.get_adjacent_segment_exits(position)
            s = Segment(exits=exits)

            # In the original Citadel of Blood core there are 200 segments and 80 of them are rooms.
            # In Polish pirated version the ratio room:corridor is 0.38.
            # Here, we use the extended ratio.
            if Exit.room in exits and Exit.corridor not in exits:
                d100 = dice.roll("d100")
                if d100 <= 50:
                    s = Room(exits=exits)

            s.complete_exits()
            return s

        return self.map[position]
