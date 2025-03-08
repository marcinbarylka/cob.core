"""A board segment module."""

import random

from cob_core.mechanics import dice
from cob_core.mechanics.enums import Exit
from cob_core.mechanics.features import Feature, FeatureFactory


class Segment:
    def __init__(self, exits: list[int] | None) -> None:
        self.exits: list[int] = (
            exits
            if exits is not None
            else [
                Exit.undefined,
                Exit.undefined,
                Exit.undefined,
                Exit.undefined,
            ]
        )

    def complete_exits(self):
        """
        Complete the exits of a segment.

        If there are less than 2 corridors, add corridors until there are 2.
        If there are more than 2 corridors, remove corridors until there are 2.
        """
        corridor_exits = self.exits.count(Exit.corridor)
        undefined_exits_indices = [i for i, e in enumerate(self.exits) if e == Exit.undefined]

        # Add corridors if there are less than 2
        while corridor_exits < 2 and undefined_exits_indices:
            new_corridor_index = random.choice(undefined_exits_indices)
            self.exits[new_corridor_index] = Exit.corridor
            undefined_exits_indices.remove(new_corridor_index)
            corridor_exits += 1

        # Decide for each undefined exit whether it becomes a room or a wall
        for i in undefined_exits_indices:
            self.exits[i] = Exit.room if dice.roll("d100") > 50 else Exit.wall

        # Ensure all undefined exits are now walls if they weren't turned into rooms
        self.exits = [Exit.wall if e == Exit.undefined else e for e in self.exits]

    def _exits_to_str(self) -> tuple[str, ...]:
        """
        A helper function to convert the exits to a string.

        Returns:
            tuple of strings representing the exits

        """
        str_exits = ("north", "east", "south", "west")
        result = []
        for idx, ex in enumerate(self.exits):
            if ex > 0:
                result.append(str_exits[idx])
        return tuple(result)

    def __str__(self) -> str:
        return f"Segment with exits: {self._exits_to_str()}"

    def __repr__(self) -> str:
        return f"Segment({self.exits})"


class Room(Segment):
    def __init__(self, exits: list[int] | None, feature: Feature | None = None) -> None:
        super().__init__(exits)
        self.feature: Feature | None = feature

    def complete_exits(self) -> None:
        """
        Complete the exits of a room.

        If there are less than 2 corridors, add corridors until there are 2.
        If there are more than 2 corridors, remove corridors until there are 2.
        """
        possible_exits = [idx for idx, e in enumerate(self.exits) if e == Exit.undefined]
        for _exit in possible_exits:
            if dice.roll("d100") > 50:
                self.exits[_exit] = Exit.room
        for idx, _ in enumerate(self.exits):
            if self.exits[idx] == Exit.undefined:
                self.exits[idx] = Exit.wall

    def random_feature(self) -> None:
        """
        Add a random feature to the room.
        """
        self.feature = FeatureFactory.random_feature()

    def __str__(self) -> str:
        return f"Room with exits: {self._exits_to_str()} and features: {self.feature}"

    def __repr__(self) -> str:
        return f"Room({self.exits}, {self.feature})"


class GatewayOfEvil(Segment):
    def __init__(self) -> None:
        super().__init__([Exit.corridor, Exit.wall, Exit.wall, Exit.wall])
