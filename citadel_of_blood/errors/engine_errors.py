"""Module containing custom exceptions for the Citadel of Blood engine."""


class PartyError(Exception):
    """Base class for party-related errors."""


class InvalidPartyPositionError(PartyError):
    """Raised when trying to access an invalid position in the party."""

    def __init__(self, x_pos: int, y_pos: int) -> None:
        """Initialize the InvalidPartyPositionError class.

        Args:
            x_pos: The invalid x position
            y_pos: The invalid y position

        """
        super().__init__(f"Invalid party position: ({x_pos}, {y_pos})")


class InvalidPartyRankError(PartyError):
    """Raised when trying to access an invalid rank in the party."""

    def __init__(self, rank: int) -> None:
        """Initialize the InvalidPartyRankError class.

        Args:
            rank: The invalid rank number

        """
        super().__init__(f"Invalid rank number: {rank}")


class InvalidPartyCharacterError(PartyError):
    """Raised when trying to add an invalid character to the party."""

    def __init__(self) -> None:
        """Initialize the InvalidPartyCharacterError class."""
        super().__init__("Character must be of type Hero, Initiate, Monster or None")


class CharacterNotInPartyError(PartyError):
    """Raised when a character is not found in the party."""

    def __init__(self) -> None:
        """Initialize the CharacterNotInPartyError class."""
        super().__init__("Character not found in party")


class CharacterAlreadyInPartyError(PartyError):
    """Raised when a character is already in the party."""

    def __init__(self) -> None:
        """Initialize the CharacterAlreadyInPartyError class."""
        super().__init__("Character already in party")


class GameScreenError(Exception):
    """Error raised when there is an issue with the game screen."""


class ColorError(Exception):
    """Error raised when there is an issue with a color."""


class InvalidDiceCodeError(ValueError):
    """Raised when dice code format is invalid."""

    def __init__(self, dice_code: str) -> None:
        """Initialize the InvalidDiceCodeError class."""
        super().__init__(f"Unrecognized dice code: {dice_code}")


class WeaponNotFoundError(ValueError):
    """Raised when a hero doesn't have the specified weapon."""

    def __init__(self, hero_name: str) -> None:
        """Initialize the WeaponNotFoundError class."""
        super().__init__(f"{hero_name} does not have this weapon.")


class MaxWeaponsReachedError(ValueError):
    """Raised when trying to add more weapons than allowed."""

    def __init__(self) -> None:
        """Initialize the MaxWeaponsReachedError class."""
        super().__init__("The Initiate already has two weapons.")
