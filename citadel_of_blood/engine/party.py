"""Module for managing party of characters in the game."""

from citadel_of_blood.engine.heroes import Hero, Initiate
from citadel_of_blood.engine.monsters import Monster
from citadel_of_blood.engine.types import (
    MAX_CHARACTERS_IN_RANK,
    MIN_RANK,
    Character,
    PartyPosition,
    PartyRank,
)
from citadel_of_blood.errors.engine_errors import (
    CharacterAlreadyInPartyError,
    CharacterNotInPartyError,
    InvalidPartyCharacterError,
    InvalidPartyPositionError,
    InvalidPartyRankError,
)


class Party(list):
    """A group of characters organized in ranks.

    The Party is organized in ranks, where each rank can have at most 3 characters.
    The ranks are:
    - Front rank (rank 0)
    - Middle rank (rank 1)
    - Back rank (rank 2, if present)

    Characters in each rank can support and interact with characters in other ranks
    based on their position and abilities.
    """

    def __init__(self, characters: list[Character | None] | None = None) -> None:
        """Initialize a new party.

        Args:
            characters: Optional list of characters to add to the party initially

        """
        super().__init__()
        if characters:
            for character in characters:
                self._validate_character(character)
                self.append(character)

    def get_size_xy(self) -> PartyPosition:
        """Get the party's dimensions.

        Returns:
            Tuple of (width, height) where width is always MAX_CHARACTERS_IN_RANK
            and height is at least 1

        """
        return MAX_CHARACTERS_IN_RANK, max(1, len(self) // MAX_CHARACTERS_IN_RANK)

    def _validate_position(self, x_pos: int, y_pos: int) -> None:
        """Validate if a position is within party bounds.

        Args:
            x_pos: Horizontal position (0 to MAX_CHARACTERS_IN_RANK - 1)
            y_pos: Vertical position (rank number)

        Raises:
            InvalidPartyPositionError: If the position is out of bounds

        """
        width, height = self.get_size_xy()
        if not (0 <= x_pos < width and 0 <= y_pos < height):
            raise InvalidPartyPositionError(x_pos, y_pos)

    def _validate_character(self, character: Character | None) -> None:
        """Validate if a character can be added to the party.

        Args:
            character: The character to validate

        Raises:
            InvalidPartyCharacterError: If the character is not of a valid type

        """
        if character is not None and not isinstance(
            character, Hero | Initiate | Monster
        ):
            raise InvalidPartyCharacterError()

    def calculate_linear_index(self, x_pos: int, y_pos: int) -> int:
        """Convert 2D position to linear index.

        Args:
            x_pos: Horizontal position
            y_pos: Vertical position (rank number)

        Returns:
            Linear index in the party list

        """
        return x_pos + y_pos * MAX_CHARACTERS_IN_RANK

    def calculate_position(self, linear_index: int) -> PartyPosition:
        """Convert linear index to 2D position.

        Args:
            linear_index: Index in the party list

        Returns:
            Tuple of (x_pos, y_pos) coordinates

        """
        return (
            linear_index % MAX_CHARACTERS_IN_RANK,
            linear_index // MAX_CHARACTERS_IN_RANK,
        )

    def add_character(self, character: Character | None) -> None:
        """Add a character to the next available position.

        Args:
            character: The character to add

        Raises:
            InvalidPartyCharacterError: If the character is not of a valid type
            CharacterAlreadyInPartyError: If the character is already in the party

        """
        self._validate_character(character)
        if character in self:
            raise CharacterAlreadyInPartyError()
        self.append(character)

    def remove_character(self, character: Character) -> None:
        """Remove a character from the party.

        Args:
            character: The character to remove

        Raises:
            CharacterNotInPartyError: If the character is not in the party

        """
        if character not in self:
            raise CharacterNotInPartyError()
        position = self.calculate_position(self.index(character))
        self.add_character_at(None, *position)

    def remove_at(self, x_pos: int, y_pos: int) -> None:
        """Remove a character at a specific position.

        Args:
            x_pos: Horizontal position
            y_pos: Vertical position (rank number)

        Raises:
            InvalidPartyPositionError: If the position is out of bounds

        """
        self._validate_position(x_pos, y_pos)
        self.add_character_at(None, x_pos, y_pos)

    def find_character(self, character: Character) -> PartyPosition:
        """Find a character's position in the party.

        Args:
            character: The character to find

        Returns:
            Tuple of (x_pos, y_pos) coordinates

        Raises:
            InvalidPartyCharacterError: If the character is not of a valid type
            CharacterNotInPartyError: If the character is not in the party

        """
        self._validate_character(character)
        if character not in self:
            raise CharacterNotInPartyError()
        return self.calculate_position(self.index(character))

    def add_character_at(
        self, character: Character | None, x_pos: int, y_pos: int
    ) -> None:
        """Place a character at a specific position.

        If the position is beyond the current party size, the party will be
        expanded with None values up to that position.

        Args:
            character: The character to add
            x_pos: Horizontal position
            y_pos: Vertical position (rank number)

        Raises:
            InvalidPartyCharacterError: If the character is not of a valid type

        """
        self._validate_character(character)
        linear_index = self.calculate_linear_index(x_pos, y_pos)

        # Expand party if needed
        while len(self) <= linear_index:
            self.append(None)

        self[linear_index] = character

    def get_from(self, x_pos: int, y_pos: int) -> Character | None:
        """Get the character at a specific position.

        Args:
            x_pos: Horizontal position
            y_pos: Vertical position (rank number)

        Returns:
            The character at the position, or None if the position is empty
            or out of bounds

        """
        linear_index = self.calculate_linear_index(x_pos, y_pos)
        return self[linear_index] if linear_index < len(self) else None

    def get_rank(self, rank_no: int) -> PartyRank:
        """Get all characters in a specific rank.

        Args:
            rank_no: The rank number (0 for front, 1 for middle, 2 for back)

        Returns:
            List of characters in the rank

        Raises:
            InvalidPartyRankError: If the rank number is invalid

        """
        if rank_no < MIN_RANK or rank_no * MAX_CHARACTERS_IN_RANK >= len(self):
            raise InvalidPartyRankError(rank_no)

        start_index = rank_no * MAX_CHARACTERS_IN_RANK
        end_index = min(start_index + MAX_CHARACTERS_IN_RANK, len(self))
        return self[start_index:end_index]

    def get_ranks(self) -> list[PartyRank]:
        """Get all ranks in the party.

        Returns:
            List of ranks, where each rank is a list of characters

        """
        num_full_ranks = len(self) // MAX_CHARACTERS_IN_RANK
        ranks = [self.get_rank(rank_no) for rank_no in range(num_full_ranks)]

        # Add partial rank if it exists
        if len(self) % MAX_CHARACTERS_IN_RANK:
            ranks.append(self.get_rank(num_full_ranks))

        return ranks
