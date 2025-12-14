"""Module for heroes and initiates."""

import random
from dataclasses import dataclass, field
from typing import Any, ClassVar

from pydantic import NonNegativeInt, PositiveInt

from citadel_of_blood.engine import dice
from citadel_of_blood.engine.armors import Armor
from citadel_of_blood.engine.skills import (
    Skill,
    WeaponSkill,
)
from citadel_of_blood.engine.spells import MAGIC_POTENTIAL_TABLE, Spell
from citadel_of_blood.engine.types import MagicPotential, Race
from citadel_of_blood.engine.weapons import Weapon
from citadel_of_blood.errors.engine_errors import (
    MaxWeaponsReachedError,
    WeaponNotFoundError,
)


@dataclass
class Hero:
    """A hero that can be played by a player.

    A hero is a character with various attributes and abilities that can be used in the game_gui.
    Heroes can fight using weapons, cast spells, and use skills.

    Attributes:
        name: The hero's full name
        name_short: Abbreviated name for display purposes
        race: The hero's race (Human, Elf, etc.)
        wound_points: Maximum health points
        magic_potential: Tuple of three values representing magic abilities
        resistance_value: Defense against attacks
        combat_bonus: Additional damage in combat
        weapons: List of weapons the hero can use
        weapon_skill: Optional specialized weapon skill
        skill: Special ability
        icon: Character representation
        armor: Optional protective equipment
        spells: List of known spells
        jewels: List of collected jewels
        gold_marks: Amount of gold owned
        XP: Experience points

    """

    name: str
    name_short: str
    race: Race
    wound_points: PositiveInt
    magic_potential: MagicPotential
    resistance_value: NonNegativeInt
    combat_bonus: NonNegativeInt
    weapons: list[Weapon]
    weapon_skill: WeaponSkill | None
    skill: Skill
    icon: str = ""
    armor: Armor | None = None
    spells: list[Spell] = field(default_factory=list)
    jewels: list[Any] = field(default_factory=list)
    gold_marks: NonNegativeInt = 0
    XP: NonNegativeInt = 0

    _wound_points: PositiveInt = field(init=False)

    def __post_init__(self) -> None:
        """Initialize the hero's current wound points to maximum."""
        self._wound_points = self.wound_points

    @property
    def max_wound_points(self) -> int:
        """Get the hero's maximum wound points.

        Returns:
            The maximum number of wound points the hero can have

        """
        return self._wound_points

    @property
    def is_alive(self) -> bool:
        """Check if the hero is still alive.

        Returns:
            True if the hero has more than 0 wound points

        """
        return self.wound_points > 0

    def fight(self, weapon: Weapon) -> int:
        """Calculate damage dealt with a weapon.

        Rolls a die and adds combat bonus and weapon skill (if applicable)
        to determine the damage dealt to an opponent.

        Args:
            weapon: The weapon to use in combat

        Returns:
            The amount of damage dealt

        Raises:
            WeaponNotFoundError: If the hero doesn't have the specified weapon

        """
        if weapon not in self.weapons:
            raise WeaponNotFoundError(self.name)

        bonus = self.combat_bonus
        if self.weapon_skill and self.weapon_skill.weapon == weapon:
            bonus += self.weapon_skill.value

        roll_result = dice.roll(f"d6+{bonus}")
        return weapon.get_damage(roll_result)


class Initiate(Hero):
    """A novice hero with more limited capabilities.

    Initiates are weaker versions of heroes, with randomly determined magic potential
    and a limit of two weapons.
    """

    MAX_WEAPONS: ClassVar[int] = 2

    def __post_init__(self) -> None:
        """Initialize the initiate with random magic potential."""
        super().__post_init__()
        self.magic_potential = MAGIC_POTENTIAL_TABLE[dice.roll("d6") - 1]

    def add_weapon(self, weapon: Weapon) -> None:
        """Add a new weapon to the initiate's inventory.

        Args:
            weapon: The weapon to add

        Raises:
            MaxWeaponsReachedError: If the initiate already has the maximum number of weapons

        """
        if len(self.weapons) >= self.MAX_WEAPONS:
            raise MaxWeaponsReachedError()

        self.weapons = [*self.weapons, weapon][: self.MAX_WEAPONS]


def random_heroes(how_many: PositiveInt = 3) -> list[Hero]:
    """Select random heroes from the available pool.

    Args:
        how_many: Number of heroes to select

    Returns:
        List of randomly selected heroes

    """
    return random.sample(HeroesEnum.to_list(), how_many)


# Hero and Initiate definitions moved to separate configuration files
from citadel_of_blood.engine.hero_data import HeroesEnum  # noqa: E402
