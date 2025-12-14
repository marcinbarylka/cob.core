"""Module for treasures."""

import enum
from dataclasses import dataclass
from typing import Any

from citadel_of_blood.engine.armors import Armor
from citadel_of_blood.engine.dice import Dice, roll
from citadel_of_blood.engine.magic_items import (
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
from citadel_of_blood.engine.weapons import Ax, Bow, Dagger, Hammer, Sword, ThrowDagger

JEWELERY = [1, 5, 10, 15, 20, 25, 35, 50, 75, 100, 150]
MAGIC_ITEM_TYPES = ["weapon", "armor", "potion", "talisman", "medallion", "ring"]
WEAPON_BONUS = [1, 2, 2, 3, 3, 0]
ARMOR_BONUS = [1, 1, 1, 2, 2, 0]
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
    """Treasure items."""

    gold: str
    jewelery: str
    magic_items: str


class Treasure(enum.Enum):
    """Treasure enum."""

    A = TreasureItems("0:0", "0:0", "0:0")
    B = TreasureItems("6:1D6", "0:0", "0:0")
    C = TreasureItems("6:1D6", "0:0", "1:1")
    D = TreasureItems("1:3D6", "1:1D3", "0:0")
    E = TreasureItems("2:1D6*10", "1:1D6", "2:1")
    F = TreasureItems("3:1D6*5", "3:1D3", "1:1")
    G = TreasureItems("6:1D6*5", "3:1D6", "2:1")
    H = TreasureItems("6:2D6", "3:1D3", "1:1")
    I = TreasureItems("6:1D6*5", "2:1D6", "2:1")  # noqa: E741
    J = TreasureItems("6:1D6*20", "2:1D6", "3:1D3")
    K = TreasureItems("6:2D6*20", "3:1D6", "3:1D3")
    L = TreasureItems("6:3D6*20", "4:1D6", "4:1D3")

    def add(self, number: int = 0):
        """Move to the next treasure.

        Args:
            number (int, optional): number of treasures to move. Defaults to 0.

        Returns:
            Treasure: new treasure

        """
        if number == 0:
            return self
        treasure_list = list(Treasure)
        current_index = treasure_list.index(self)
        new_index = min(current_index + number, len(treasure_list) - 1)
        return treasure_list[new_index]

    def __str__(self):
        """Return the string representation of the treasure."""
        return f"Gold: {self.value.gold}, Jewelery: {self.value.jewelery}, Magic items: {self.value.magic_items}"

    def roll_gold(self) -> int:
        """Roll for gold.

        Returns:
            int: gold amount

        """
        probability, dice_code = Treasure.parse_treasure_code(self.value.gold)
        has_gold = roll("d6") <= probability if probability else False
        if not has_gold:
            return 0
        return roll(dice_code)

    def roll_jewelery(self) -> list[int]:
        """Roll for jewelery.

        Returns:
            list: list of jewelery

        """
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
        """Roll for magic items.

        Returns:
            dict: dictionary of magic items

        """
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
            if magic_item_type == "weapon" and not magic_item.attack_bonus:
                magic_item.attack_bonus = self._get_weapon_bonus()
            result[magic_item_type].append(magic_item)
        return result

    def roll_treasure(self) -> dict[str, Any]:
        """Get treasure.

        Returns:
            dict: treasure

        """
        return {
            "gold": self.roll_gold(),
            "jewelery": self.roll_jewelery(),
            "magic_items": self.roll_magic_items(),
        }

    def _get_weapon_bonus(self) -> int:
        """Get weapon bonus.

        Returns:
            int: weapon bonus

        """
        bonus = WEAPON_BONUS[roll("d6") - 1]
        if not bonus:
            return self._get_weapon_bonus() + self._get_weapon_bonus()
        return bonus

    def _get_armor_bonus(self) -> int:
        """Get armor bonus.

        Returns:
            int: armor bonus

        """
        bonus = ARMOR_BONUS[roll("d6") - 1]
        if not bonus:
            return self._get_armor_bonus() + self._get_armor_bonus()
        return bonus

    @staticmethod
    def parse_treasure_code(code: str) -> tuple[int, str] | tuple[int, None]:
        """Parse a treasure code.

        Args:
            code (str): treasure code

        Returns:
            tuple: probability and dice code

        """
        probability, treasure_code = code.split(":")
        return int(probability), treasure_code

    @staticmethod
    def empty_treasure() -> dict[str, Any]:
        """Empty treasure.

        Returns:
            dict: empty treasure

        """
        return {
            "gold": 0,
            "jewelery": [],
            "magic_items": {key: [] for key in MAGIC_ITEM_TYPES},
        }
