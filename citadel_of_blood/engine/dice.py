"""Module for dice rolling."""

import re
from dataclasses import dataclass
from random import randint
from typing import Final

from citadel_of_blood.errors.engine_errors import InvalidDiceCodeError


@dataclass
class DiceComponents:
    """Components of a parsed dice code."""

    number: int = 1
    type: int = 0
    modifier: int = 0
    multiplier: int = 1


class Dice:
    """A dice representation that can parse and roll dice notation.

    The dice notation follows the format: NdS[+/-/]*M
    where:
    - N is the number of dice (optional, defaults to 1)
    - S is the number of sides on each die
    - +/-/* is the optional operator
    - M is the optional modifier or multiplier

    Examples:
        >>> dice = Dice("2d6+3")  # roll 2 six-sided dice and add 3
        >>> dice = Dice("d20")    # roll 1 twenty-sided die
        >>> dice = Dice("3d8*2")  # roll 3 eight-sided dice and multiply by 2

    """

    DICE_PATTERN: Final = r"^(\d*)[dD](\d+)([\+\-\*]?)(\d*)$"

    def __init__(self, dice_code: str = "D6") -> None:
        """Initialize the Dice class.

        Args:
            dice_code: A code representing dice roll (e.g. "2d10+20")

        Raises:
            InvalidDiceCodeError: If the dice code format is invalid

        """
        self._components = DiceComponents()
        self.code = dice_code
        self.parse(dice_code)

    def _parse_modifier(self, operator: str, value: str) -> tuple[int, int]:
        """Parse modifier or multiplier from dice code.

        Args:
            operator: The operator ('+', '-', or '*')
            value: The value to parse

        Returns:
            tuple[int, int]: (modifier, multiplier)

        """
        if not value:
            return 0, 1

        parsed_value = int(value)
        if operator == "*":
            return 0, parsed_value
        if operator == "-":
            return -parsed_value, 1
        return parsed_value, 1

    def parse(self, dice_code: str) -> None:
        """Parse a dice code string into its components.

        Args:
            dice_code: A code representing dice roll (e.g. "2d10+20")

        Raises:
            InvalidDiceCodeError: If the dice code format is invalid

        """
        match = re.match(self.DICE_PATTERN, dice_code)
        if not match:
            raise InvalidDiceCodeError(dice_code)

        number_str, type_str, operator, mod_str = match.groups()

        self._components.number = int(number_str) if number_str else 1
        self._components.type = int(type_str)
        self._components.modifier, self._components.multiplier = self._parse_modifier(operator, mod_str)

    def roll(self, dice_code: str | None = None) -> int:
        """Roll the dice according to the parsed dice code.

        Args:
            dice_code: Optional new dice code to parse before rolling

        Returns:
            The result of the dice roll

        Raises:
            InvalidDiceCodeError: If the new dice code format is invalid

        """
        if dice_code:
            self.parse(dice_code)

        result = sum(randint(1, self._components.type) for _ in range(self._components.number))
        return result * self._components.multiplier + self._components.modifier

    @property
    def max(self) -> int:
        """Calculate the maximum possible value for this dice roll.

        Returns:
            The maximum possible roll value

        """
        return self._components.type * self._components.number * self._components.multiplier + self._components.modifier

    @property
    def min(self) -> int:
        """Calculate the minimum possible value for this dice roll.

        Returns:
            The minimum possible roll value

        """
        return self._components.number * self._components.multiplier + self._components.modifier


def roll(dice_code: str) -> int:
    """Roll dice using the specified dice code.

    This is a convenience wrapper function for the Dice class.

    Args:
        dice_code: A code representing dice roll (e.g. "2d10+20")

    Returns:
        The result of the dice roll

    Raises:
        InvalidDiceCodeError: If the dice code format is invalid

    Examples:
        >>> roll("2d6+3")  # roll 2 six-sided dice and add 3
        >>> roll("d20")    # roll 1 twenty-sided die
        >>> roll("3d8*2")  # roll 3 eight-sided dice and multiply by 2

    """
    return Dice().roll(dice_code)
