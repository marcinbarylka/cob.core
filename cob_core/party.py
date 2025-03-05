""" "Module for the party class."""

from cob_core.heroes import Hero, Initiate
from cob_core.monsters import Monster

Character = Hero | Initiate | Monster


class Party(list):
    """
    Party class. It is responsible for storing the heroes and the initiate of the party.

    The Party is organized in ranks. Every rank can have at most 3 characters. The first rank is the front rank, the
    second rank is the middle rank, and the third rank (if any) is the back rank.

    Parameters:
        characters (list[Hero | Initiate | Monster | None]): list of characters to initialize the party with

    """

    MAX_CHARACTER_IN_RANK = 3

    def __init__(self, characters: list[Character | None] | None = None):
        super().__init__()
        if characters:
            for character in characters:
                self._check_character(character)
                self.append(character)

    def get_size_xy(self) -> tuple[int, int]:
        """
        Get the size of the party in the x and y dimensions.

        Returns:
            tuple of the size of the party in the x and y dimensions

        """
        return Party.MAX_CHARACTER_IN_RANK, max(1, len(self) // Party.MAX_CHARACTER_IN_RANK)

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

    def _check_character(self, character: Character | None) -> None:
        """
        Check if the character is valid.

        Args:
            character: character to check

        """
        if character is not None and not isinstance(character, Character):
            raise TypeError("Character must be of type Hero, Initiate, Monster or None")

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

    def add_character(self, character: Character | None) -> None:
        """
        Add a character to the party.

        Args:
            character: character to add to the party

        Raises:
            ValueError: if the character is already in the party

        """
        self._check_character(character)
        if character in self:
            raise ValueError("Character already in party")
        self.append(character)

    def remove_character(self, character: Character) -> None:
        """
        Remove a character from the party.

        Args:
            character: character to remove from the party

        """
        if character not in self:
            raise ValueError("Character not in party")
        linear = self.index(character)
        self.add_character_at(None, *self.calculate_position(linear))

    def remove_at(self, x_pos: int, y_pos: int) -> None:
        """
        Remove a character from the party at a specific index.

        Args:
            x_pos: x position
            y_pos: y position

        """
        self._check_position(x_pos, y_pos)
        self.add_character_at(None, x_pos, y_pos)

    def find_character(self, character: Character) -> tuple[int, int]:
        """
        Find the position of a character in the party.

        Args:
            character: character to find

        Returns:
            position of the character in the party

        Raises:
            ValueError: if the character is not in the party

        """
        self._check_character(character)
        if character not in self:
            raise ValueError("Character not in party")
        linear_index = self.index(character)
        return self.calculate_position(linear_index)

    def add_character_at(self, character: Character | None, x_pos: int, y_pos: int) -> None:
        """
        Set a character at a specific index.

        Args:
            character: character to set
            x_pos: x position
            y_pos: y position

        """
        linear_index = self.calculate_linear_index(x_pos, y_pos)
        if linear_index >= len(self):
            for _ in range(len(self), linear_index + 1):
                self.append(None)
        self[linear_index] = character

    def get_from(self, x_pos: int, y_pos: int) -> Character | None:
        """
        Get a character at a specific index.

        Args:
            x_pos: x position
            y_pos: y position

        Returns:
            character at the given position

        """
        linear_index = self.calculate_linear_index(x_pos, y_pos)
        if linear_index >= len(self):
            return None
        return self[self.calculate_linear_index(x_pos, y_pos)]

    def get_rank(self, rank_no: int) -> list[Character | None]:
        """
        Get the characters of a specific rank.

        Args:
            rank_no: rank number

        Returns:
            list of characters of the given rank

        """
        if rank_no < 0 or rank_no * Party.MAX_CHARACTER_IN_RANK >= len(self):
            raise ValueError("Invalid rank number")
        start_index = rank_no * Party.MAX_CHARACTER_IN_RANK
        end_index = min(start_index + Party.MAX_CHARACTER_IN_RANK, len(self))
        return self[start_index:end_index]

    def get_ranks(self) -> list[list[Character | None]]:
        """
        Get the characters of all ranks.

        Returns:
            list of lists of characters of all ranks

        """
        num_full_ranks = len(self) // Party.MAX_CHARACTER_IN_RANK
        ranks = [self.get_rank(rank_no) for rank_no in range(num_full_ranks)]

        # Check for remaining characters in a partial rank
        if len(self) % Party.MAX_CHARACTER_IN_RANK != 0:
            ranks.append(self.get_rank(num_full_ranks))

        return ranks
