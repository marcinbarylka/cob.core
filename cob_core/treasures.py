import enum
from dataclasses import dataclass

from cob_core.dice import roll


@dataclass
class TreasureItems:
    gold: str
    jewelery: str
    magic_items: str


class Treasure(enum.Enum):
    A = TreasureItems("0:0", "0:0", "0:0")
    B = TreasureItems("6:1D6", "0:0", "0:0")
    C = TreasureItems("6:1D6", "0:0", "1:1")
    D = TreasureItems("1:3D6", "1:1D3", "0:0")
    E = TreasureItems("2:1D6*10", "1:1D6", "2:1")
    F = TreasureItems("3:1D6*5", "3:1D3", "1:1")
    G = TreasureItems("6:1D6*5", "3:1D6", "2:1")
    H = TreasureItems("6:2D6", "3:1D3", "1:1")
    I = TreasureItems("6:1D6*5", "2:1D6", "2:1")
    J = TreasureItems("6:1D6*20", "2:1D6", "3:1D3")
    K = TreasureItems("6:2D6*20", "3:1D6", "3:1D3")
    L = TreasureItems("6:3D6*20", "4:1D6", "4:1D3")

    def __str__(self):
        return f"Gold: {self.value.gold}, Jewelery: {self.value.jewelery}, Magic items: {self.value.magic_items}"

    @staticmethod
    def roll_gold(treasure: TreasureItems) -> int:
        probability, dice_code = Treasure.parse_treasure_code(treasure.gold)
        has_gold = roll("d6") <= probability if probability else False
        if not has_gold:
            return 0
        return roll(dice_code)

    @staticmethod
    def parse_treasure_code(code: str) -> tuple[int, str] | tuple[int, None]:
        """
        Parse a treasure code.

        :param code: a code of the treasure.
        :type code: str.

        :return: tuple[int, str] | tuple[int, None] -- probability and dice code.
        """
        probability, treasure_code = code.split(":")
        return int(probability), treasure_code
