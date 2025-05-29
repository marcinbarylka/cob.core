"""Module for dice rolling."""

import re
from random import randint


class Dice:
    """A dice representation. It can parse and roll a dice."""

    def __init__(self, dice_code="D6"):
        """Initialize the Dice class.

        Args:
            dice_code: a code of the dice: i.e. 2d10+20.

        """
        self.code = dice_code
        self.number = 0
        self.type = 0
        self.modifier = 0
        self.multiplier = 1
        self.parse()

    def parse(self, dice_code: str | None = None) -> None:
        """Dice parser.

        Args:
            dice_code: a code of the dice: i.e. 2d10+20.

        """
        if dice_code:
            self.code = dice_code

        pattern = r"^(\d*)[dD](\d+)([\+\-\*]?)(\d*)$"
        self.number = 1
        self.type = 0
        modifier_sign = 1
        self.modifier = 0
        self.multiplier = 1

        match_data = re.match(pattern, self.code)
        if match_data:
            if match_data.group(1) != "":
                self.number = int(match_data.group(1))
            if match_data.group(2) != "":
                self.type = int(match_data.group(2))
            if match_data.group(3) == "-":
                modifier_sign = -1
            if match_data.group(4) != "" and match_data.group(3) != "*":
                self.modifier = int(match_data.group(4)) * modifier_sign
                self.multiplier = 1
            if match_data.group(3) == "*":
                self.multiplier = int(match_data.group(4))
                self.modifier = 0
        else:
            msg = f"Unrecognized dice code: {dice_code}"
            raise ValueError(msg)

    def roll(self, dice_code: str | None = None) -> int:
        """Roll a parsed dice.

        Args:
            dice_code: a code of the dice: i.e. 2d10+20.

        Returns:
            int. The result of the roll.

        """
        if dice_code:
            self.parse(dice_code)
        result = 0
        for _ in range(0, self.number):
            result += randint(1, self.type)
        result *= self.multiplier
        result += self.modifier
        return result

    @property
    def max(self):  # noqa: D102
        """Max value of the roll.

        Returns:
            int. The max value of the roll.

        """
        return self.type * self.number * self.multiplier + self.modifier

    @property
    def min(self):  # noqa: D102
        """Min value of the roll.

        Returns:
            int. The min value of the roll.

        """
        return self.number * self.multiplier + self.modifier


def roll(dice_code):
    """Roll a dice.

    This is a wrapper function for the Dice class.

    Args:
        dice_code: a code of the dice: i.e. 2d10+20.

    Returns:
        int. The result of the roll.

    """
    return Dice().roll(dice_code)
