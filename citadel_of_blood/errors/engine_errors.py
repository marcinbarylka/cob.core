"""Module containing custom exceptions for the Citadel of Blood engine."""


class PartyCharacterError(Exception):
    """Error raised when a party character is not found in the party."""


class CharacterNotInPartyError(PartyCharacterError):
    """Error raised when a character is not found in the party."""


class CharacterAlreadyInPartyError(PartyCharacterError):
    """Error raised when a character is already in the party."""


class GameScreenError(Exception):
    """Error raised when there is an issue with the game screen."""


class ColorError(Exception):
    """Error raised when there is an issue with a color."""


class InvalidDiceCodeError(ValueError):
    """Raised when dice code format is invalid."""

    def __init__(self, dice_code: str) -> None:
        """Initialize the InvalidDiceCodeError class."""
        super().__init__(f"Unrecognized dice code: {dice_code}")
