import enum
from dataclasses import dataclass
from typing import Any

from cob_core.armors import Armor
from cob_core.dice import Dice, roll
from cob_core.magic_items import (
    AllSuns,
    BlueSun,
    CharmMonster,
    CharmPerson,
    DexterityMedallion,
    Evil,
    Heal,
    Healing,
    Mind,
    NeutralizePoisonMedallion,
    NeutralizePoisonRing,
    Oratory,
    Poison,
    PotionAppraisal,
    RedSun,
    Resistance,
    Resurrect,
    Sleep,
    Strangling,
    Strength,
    YellowSun,
)
from cob_core.weapons import Ax, Bow, Dagger, Hammer, Sword, ThrowDagger

JEWELERY = [1, 5, 10, 15, 20, 25, 35, 50, 75, 100, 150]
MAGIC_ITEM_TYPES = ["weapon", "armor", "potion", "talisman", "medallion", "ring"]
WEAPON_BONUS = [1, 2, 2, 3, 3, 0]
ARMOR_BONUS = [1, 1, 1, 2, 2, 0]

# TODO: Implement magic items
MAGIC_ITEMS = {
    "weapon": [Sword(), Hammer(), Ax(), Bow(), Dagger(), ThrowDagger()],
    "armor": [Armor(1), Armor(1), Armor(1), Armor(2), Armor(2), Armor(0)],
    "potion": [
        Poison(),
        Strength(),
        Strength(),
        CharmPerson(),
        CharmMonster(),
        Healing(),
    ],
    "talisman": [Mind(), YellowSun(), BlueSun(), RedSun(), AllSuns(), Evil()],
    "medallion": [
        NeutralizePoisonMedallion(),
        PotionAppraisal(),
        Oratory(),
        DexterityMedallion(),
        NeutralizePoisonMedallion(),
        Strangling(),
    ],
    "ring": [
        Resistance(1),
        Resistance(2),
        Sleep(),
        NeutralizePoisonRing(),
        Heal(),
        Resurrect(),
    ],
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
    I = TreasureItems("6:1D6*5", "2:1D6", "2:1")  # noqa
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
            [JEWELERY[roll("2d6") - 2] for _ in range(roll(dice_code))]
            if dice_code
            else []
        )

    def roll_magic_items(self) -> dict[str, list[Any]]:
        """Roll for magic items."""

        result = {key: [] for key in MAGIC_ITEM_TYPES}
        probability, code = Treasure.parse_treasure_code(self.value.magic_items)

        # Try to parse dice code. If it fails, that means there is arbitrary value.
        arbitrary_value = 0

        if not code:
            return result

        has_magic_items = roll("d6") <= probability if probability else False
        if not has_magic_items:
            return result

        try:
            _ = Dice(code)
        except ValueError:
            arbitrary_value = int(code)
            code = None

        if code:
            arbitrary_value = roll(code)

        for _ in range(arbitrary_value):
            magic_item_type = MAGIC_ITEM_TYPES[roll("d6") - 1]
            magic_item = MAGIC_ITEMS[magic_item_type][roll("d6") - 1]
            if magic_item_type == "armor" and not magic_item.defense:
                magic_item.defense = self._get_armor_bonus()
            if magic_item_type == "weapon" and not magic_item.additional_damage:
                magic_item.additional_damage = self._get_weapon_bonus()
            result[magic_item_type].append(magic_item)
        return result

    def roll_treasure(self) -> dict[str, Any]:
        """Get treasure."""
        return {
            "gold": self.roll_gold(),
            "jewelery": self.roll_jewelery(),
            "magic_items": self.roll_magic_items(),
        }

    def _get_weapon_bonus(self) -> int:
        """Get weapon bonus."""
        bonus = WEAPON_BONUS[roll("d6") - 1]
        if not bonus:
            return self._get_weapon_bonus() + self._get_weapon_bonus()
        return bonus

    def _get_armor_bonus(self) -> int:
        """Get armor bonus."""
        bonus = ARMOR_BONUS[roll("d6") - 1]
        if not bonus:
            return self._get_armor_bonus() + self._get_armor_bonus()
        return bonus

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
