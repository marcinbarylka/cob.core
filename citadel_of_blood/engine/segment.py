"""A board segment module."""

import random

from citadel_of_blood.engine import dice
from citadel_of_blood.engine.enums import Exit
from citadel_of_blood.engine.features import Feature, FeatureFactory


class Segment:
    """Segment of the board."""

    def __init__(self, exits: list[int] | None) -> None:
        """Initialize the segment.

        Args:
            exits: list of exits of the segment

        """
        self.exits: list[int] = (
            exits
            if exits is not None
            else [
                Exit.UNDEFINED,
                Exit.UNDEFINED,
                Exit.UNDEFINED,
                Exit.UNDEFINED,
            ]
        )

    def complete_exits(self):
        """Complete the exits of a segment.

        If there are less than 2 corridors, add corridors until there are 2.
        If there are more than 2 corridors, remove corridors until there are 2.
        """
        corridor_exits = self.exits.count(Exit.CORRIDOR)
        undefined_exits_indices = [
            i for i, e in enumerate(self.exits) if e == Exit.UNDEFINED
        ]

        # Add corridors if there are less than 2
        while corridor_exits < 2 and undefined_exits_indices:
            new_corridor_index = random.choice(undefined_exits_indices)  # noqa: S311 [this is not a crypto function]
            self.exits[new_corridor_index] = Exit.CORRIDOR
            undefined_exits_indices.remove(new_corridor_index)
            corridor_exits += 1

        # Decide for each undefined exit whether it becomes a room or a wall
        for i in undefined_exits_indices:
            self.exits[i] = Exit.ROOM if dice.roll("d100") > 50 else Exit.WALL

        # Ensure all undefined exits are now walls if they weren't turned into rooms
        self.exits = [Exit.WALL if e == Exit.UNDEFINED else e for e in self.exits]

    def _exits_to_str(self) -> tuple[str, ...]:
        """Return the exits as a tuple of strings.

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
        """Return the string representation of the segment."""
        return f"Segment with exits: {self._exits_to_str()}"

    def __repr__(self) -> str:
        """Return the string representation of the segment."""
        return f"Segment({self.exits})"


class Room(Segment):
    """A room segment."""

    def __init__(self, exits: list[int] | None, feature: Feature | None = None) -> None:
        """Initialize the room segment.

        Args:
            exits: list of exits of the room
            feature: feature of the room

        """
        super().__init__(exits)
        self.feature: Feature | None = feature

    def complete_exits(self) -> None:
        """Complete the exits of a room.

        If there are less than 2 corridors, add corridors until there are 2.
        If there are more than 2 corridors, remove corridors until there are 2.
        """
        possible_exits = [
            idx for idx, e in enumerate(self.exits) if e == Exit.UNDEFINED
        ]
        for _exit in possible_exits:
            if dice.roll("d100") > 50:
                self.exits[_exit] = Exit.ROOM
        for idx, _ in enumerate(self.exits):
            if self.exits[idx] == Exit.UNDEFINED:
                self.exits[idx] = Exit.WALL

    def randomize_feature(self) -> None:
        """Add a random feature to the room."""
        self.feature = FeatureFactory.random_feature()

    def __str__(self) -> str:
        """Return the string representation of the room."""
        return f"Room with exits: {self._exits_to_str()} and features: {self.feature}"

    def __repr__(self) -> str:
        """Return the string representation of the room."""
        return f"Room({self.exits}, {self.feature})"


class GatewayOfEvil(Segment):
    """Gateway of evil segment."""

    def __init__(self) -> None:
        """Initialize the gateway of evil segment."""
        super().__init__([Exit.CORRIDOR, Exit.WALL, Exit.WALL, Exit.WALL])
