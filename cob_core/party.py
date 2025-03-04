""" "Module for the party class."""

from cob_core.heroes import Hero, Initiate
from cob_core.monsters import Monster


class Party(list):
    """
    Party class. It is responsible for storing the heroes and the initiate of the party.

    The Party is organized in ranks. Every rank can have at most 3 characters. The first rank is the front rank, the
    second rank is the middle rank, and the third rank (if any) is the back rank.

    The party is a list of characters. The characters are stored in the list in the following order:
    - front rank characters
    - middle rank characters
    - back rank characters

    """

    MAX_CHARACTER_IN_RANK = 3

    def get_size_xy(self) -> tuple[int, int]:
        """
        Get the size of the party in the x and y dimensions.

        Returns:
            tuple of the size of the party in the x and y dimensions

        """
        return Party.MAX_CHARACTER_IN_RANK, len(self) // Party.MAX_CHARACTER_IN_RANK

    def _check_position(self, x_pos: int, y_pos: int) -> None:
        """
        Check if the position is valid.

        Args:
            x_pos: x position
            y_pos: y position

        """
        if (
            x_pos < 0
            or x_pos >= Party.MAX_CHARACTER_IN_RANK
            or y_pos < 0
            or y_pos >= len(self) // Party.MAX_CHARACTER_IN_RANK
        ):
            raise ValueError("Invalid position")

    def calculate_linear_index(self, x_pos: int, y_pos: int) -> int:
        """
        Calculate the linear index from the x and y positions.

        Args:
            x_pos: x position
            y_pos: y position

        Returns:
            linear index

        """
        return x_pos + y_pos * Party.MAX_CHARACTER_IN_RANK

    def calculate_position(self, linear_index: int) -> tuple[int, int]:
        """
        Calculate the x and y positions from the linear index.

        Args:
            linear_index: linear index

        Returns:
            x and y positions

        """
        return linear_index % Party.MAX_CHARACTER_IN_RANK, linear_index // Party.MAX_CHARACTER_IN_RANK

    def add_character(self, character: Hero | Initiate | Monster) -> None:
        """
        Add a character to the party.

        Args:
            character: character to add to the party

        """
        self.append(character)

    def remove_character(self, character: Hero | Initiate | Monster) -> None:
        """
        Remove a character from the party.

        Args:
            character: character to remove from the party

        """
        if character not in self:
            raise ValueError("Character not in party")
        linear = self.index(character)
        self.set_at(None, *self.calculate_position(linear))

    def remove_at(self, x_pos: int, y_pos: int) -> None:
        """
        Remove a character from the party at a specific index.

        Args:
            x_pos: x position
            y_pos: y position

        """
        self._check_position(x_pos, y_pos)
        self.set_at(None, x_pos, y_pos)

    def find_character(self, character: Hero | Initiate | Monster) -> tuple[int, int]:
        """
        Find the position of a character in the party.

        Args:
            character: character to find

        Returns:
            position of the character in the party

        """
        linear_index = self.index(character)
        return self.calculate_position(linear_index)

    def set_at(self, character: Hero | Initiate | Monster, x_pos: int, y_pos: int) -> None:
        """
        Set a character at a specific index.

        Args:
            character: character to set
            x_pos: x position
            y_pos: y position

        """
        linear_index = self.calculate_linear_index(x_pos, y_pos)
        if linear_index > len(self):
            for _ in range(len(self), linear_index + 1):
                self.append(None)
        self[linear_index] = character

    def get_from(self, x_pos: int, y_pos: int) -> Hero | Initiate | Monster:
        """
        Get a character at a specific index.

        Args:
            x_pos: x position
            y_pos: y position

        Returns:
            character at the given position

        """
        return self[self.calculate_linear_index(x_pos, y_pos)]

    def get_rank(self, rank_no: int) -> list[Hero | Initiate | Monster]:
        """
        Get the characters of a specific rank.

        Args:
            rank_no: rank number

        Returns:
            list of characters of the given rank

        """
        if rank_no < 0 or rank_no >= len(self) // Party.MAX_CHARACTER_IN_RANK:
            raise ValueError("Invalid rank number")
        return self[rank_no * Party.MAX_CHARACTER_IN_RANK : (rank_no + 1) * Party.MAX_CHARACTER_IN_RANK]

    def get_ranks(self) -> list[list[Hero | Initiate | Monster]]:
        """
        Get the characters of all ranks.

        Returns:
            list of lists of characters of all ranks

        """
        return [self.get_rank(rank_no) for rank_no in range(len(self) // Party.MAX_CHARACTER_IN_RANK)]
