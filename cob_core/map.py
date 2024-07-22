"""Game map module."""

from cob_core import EAST, EXIT_CORRIDOR, EXIT_ROOM, EXIT_UNDEFINED, NORTH, SOUTH, WEST, X, Y, Z, dice
from cob_core.monsters import Monster
from cob_core.segment import Entrance, Room, Segment


class Board:
    """
    Board class. It is responsible for rendering the board and moving the party counter. It also stores the map and
    monsters.
    """

    def __init__(self) -> None:
        self.map: dict[tuple[int, int, int], Segment] = {(0, 0, 0): Entrance()}
        self.monsters: dict[tuple[int, int, int], Monster] = {}
        self.party_position: tuple[int, int, int] = (0, 0, 0)

    def get_adjacent_segment_exits(self, position: tuple[int, int, int]) -> list[int]:
        directions = [NORTH, EAST, SOUTH, WEST]
        opposite_directions = [SOUTH, WEST, NORTH, EAST]
        offsets = [(0, -1, 0), (1, 0, 0), (0, 1, 0), (-1, 0, 0)]

        exits = [EXIT_UNDEFINED for _ in directions]

        for i, (dx, dy, dz) in enumerate(offsets):
            neighbor_position = (position[X] + dx, position[Y] + dy, position[Z] + dz)
            neighbor_segment = self.map.get(neighbor_position)

            if neighbor_segment:
                exits[i] = neighbor_segment.exits[opposite_directions[i]]

        return exits

    def get_segment(self, position: tuple[int, int, int]) -> Segment:
        """
        Get segment at given position. If there is no segment at given position, then it is created.

        :param position: position of the segment
        :return: segment at given position
        """
        if position not in self.map.keys():
            exits = self.get_adjacent_segment_exits(position)
            s = Segment(exits=exits)

            # In the original Citadel of Blood core there are 200 segments and 80 of them are rooms.
            # In Polish pirated version the ratio room:corridor is 0.38.
            # Here, we use the extended ratio.
            if EXIT_ROOM in exits and EXIT_CORRIDOR not in exits:
                d100 = dice.roll("d100")
                if d100 <= 50:
                    s = Room(exits=exits)

            s.complete_exits()
            return s

        return self.map[position]
