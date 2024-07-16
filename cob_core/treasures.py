import enum
from dataclasses import dataclass

from cob_core.dice import roll
from cob_core.weapons import Ax, Bow, Dagger, Hammer, Sword, ThrowDagger

JEWELERY = [0, 1, 5, 10, 15, 20, 25, 35, 50, 75, 100, 150]
MAGIC_ITEM_TYPES = ["weapon", "armor", "potion", "talisman", "medallion", "ring"]

# TODO: Implement magic items
MAGIC_ITEM = {
    "weapon": [Sword(), Hammer(), Ax(), Bow(), Dagger(), ThrowDagger()],
    "armor": [1, 1, 1, 2, 2, None],
    "potion": [
        "poison",
        "strength",
        "strength",
        "charm person",
        "charm monster",
        "healing",
    ],
    "talisman": ["mind", "yellow sun", "blue sun", "red sun", "all suns", "evil"],
    "medallion": [
        "neut poison",
        "potion appra",
        "oratory",
        "dexterity",
        "neut poison",
        "strangling",
    ],
    "ring": ["resist +1", "resist +2", "sleep", "neut poison", "heal", "resurrect"],
}


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

    def roll_gold(self) -> int:
        """Roll for gold."""
        probability, dice_code = Treasure.parse_treasure_code(self.value.gold)
        has_gold = roll("d6") <= probability if probability else False
        if not has_gold:
            return 0
        return roll(dice_code)

    def roll_jewelery(self) -> list[int]:
        """Roll for jewelery."""
        probability, dice_code = Treasure.parse_treasure_code(self.value.jewelery)
        has_jewelery = roll("d6") <= probability if probability else False
        if not has_jewelery:
            return []
        return (
            [JEWELERY[roll("2d6")] for _ in range(roll(dice_code))] if dice_code else []
        )

    def roll_magic_items(self): ...

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
