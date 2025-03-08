"""Errors for the mechanics module."""


class PartyCharacterError(Exception):
    """Error raised when a party character is not found in the party."""


class CharacterNotInPartyError(Exception):
    """Error raised when a character is not found in the party."""


class CharacterAlreadyInPartyError(Exception):
    """Error raised when a character is already in the party."""
