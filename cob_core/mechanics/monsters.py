"""Module for monsters in the game."""

from dataclasses import dataclass
from typing import Any

from cob_core.mechanics.dice import roll
from cob_core.mechanics.skills import (
    Charm,
    DemonSkill,
    FireBreath,
    FleshToStone,
    HailHydra,
    Regenerate,
    Skill,
    Stench,
    SwordSkill,
    WeaponSkill,
    XTheUnknownSkill,
)
from cob_core.mechanics.spells import LightningSpell as Lightning
from cob_core.mechanics.spells import Spell
from cob_core.mechanics.treasures import Treasure
from cob_core.mechanics.weapons import Hammer, Sword, Weapon
from cob_core.mechanics.weapons import Monster as MonsterWeapon

LEVEL_CHART = [
    {
        "wound_points": "+0",
        "combat_bonus": "+0",
        "negotiation_value": "+0",
        "number_of_monsters": "x1",
        "treasure_type": "+0",
        "experience_points": "x1",
    },
    {
        "wound_points": "+2",
        "combat_bonus": "+1",
        "negotiation_value": "+1",
        "number_of_monsters": "x1",
        "treasure_type": "+1",
        "experience_points": "x1",
    },
    {
        "wound_points": "+4",
        "combat_bonus": "+3",
        "negotiation_value": "+2",
        "number_of_monsters": "x2",
        "treasure_type": "+2",
        "experience_points": "x2",
    },
]

ROOM_MONSTER_TABLE = [
    ["EvilMage", "EvilHero", "Cronk:d6", "Garogyle", "Chimaera", "Medusa"],
    ["Orc:d3", "Troll", "Vampire", "Harpy:d3+2", "Ogre", "Minotaur"],
    ["DireWolf:d6", "Wight", "Warg:d3", "EvilMage", "EvilHero", "Cronk:d6+1"],
    ["Gargoyle:2", "Chimaera:2", "Medusa", "Orc:d6+1", "Hydra", "Vampire"],
    ["Harpy:d6+2", "Ogre:2", "Minotaur", "DireWolf:d6", "Wight:2", "Warg:d6"],
    ["Skeleton:d3", "Wraith:d3", "Skeleton:d6", "Wraith:d3+2", "Troll", "Hydra"],
]

WANDERING_MONSTER_TABLE = [
    ["EvilHero", "EvilMage", "Chimaera"],
    ["Gargoyle", "Medusa", "Orc:d3"],
    ["Troll", "Vampire", "Harpy:d3+2"],
    ["Ogre", "Minotaur", "DireWolf:d6"],
    ["Wight", "Warg:d3", "Wraith:d3"],
    ["Hydra", "Warg:d3", "Wrath:d3"],
    ["Hydra", "Skeleton:d3", "Cronk:d6"],
]


@dataclass
class Monster:
    """Monster class.

    Attributes
    ----------
        name (str): The name of the monster.
        resistance_value (int): The resistance value of the monster.
        negotiation_value (int): The negotiation value of the monster.
        weapon (Weapon): The weapon of the monster.
        spells (list[Spell]): The spells of the monster.
        treasure (tuple[Treasure, Treasure]): The treasure of the monster.
        special (Skill): The special skill of the monster.
        combat_bonus (int): The combat bonus of the monster.
        weapon_skill (WeaponSkill): The weapon skill of the monster.
        is_wandering (bool): True if the monster is a wandering monster.
        wound_points (int): The wound points of the monster.
        wound_points_code (str): The wound points code of the monster.
        experience_points (int): The experience points of the monster.
        actual_treasure (dict[str, Any]): The actual treasure of the monster.

    """

    name: str = ""
    resistance_value: int = 0
    negotiation_value: int | None = None
    weapon: Weapon | None = None
    spells: list[Spell] | None = None
    treasure: tuple[Treasure, Treasure | None] = (Treasure.A, None)
    special: Skill | None = None  # special skill for monster
    combat_bonus: int = 0
    weapon_skill: WeaponSkill | None = None
    is_wandering: bool = False
    wound_points: int = 0
    wound_points_code: str = ""
    experience_points: int = 0
    actual_treasure: dict[str, Any] | None = None

    def __post_init__(self):
        """Post initialization."""
        if not self.weapon:
            self.weapon = MonsterWeapon()
        self.wound_points = roll(self.wound_points_code)
        self._wound_points = self.wound_points
        self.experience_points = self._wound_points * 6

    @property
    def max_wound_points(self) -> int:
        """Get the maximum wound points of the monster.

        Returns
        -------
            int: The maximum wound points of the monster.

        """
        return self._wound_points

    @property
    def hold_treasure(self) -> Treasure:
        """Get the treasure of the monster.

        Returns
        -------
            Treasure: The treasure of the monster.

        """
        return self.treasure[1] if self.is_wandering else self.treasure[0]

    def get_treasure(self) -> Treasure:
        """Get the treasure of the monster.

        Returns
        -------
            Treasure: The treasure of the monster.

        """
        if self.is_wandering:
            return self.treasure[1]
        return self.treasure[0]

    def fight(self):
        """Fight the another Character."""
        # TODO: Implement the fight method.

    def cast_spell(self):
        """Cast a spell."""
        if not self.spells:
            return None

    @property
    def is_alive(self) -> bool:
        """Check if the monster is alive.

        Returns
        -------
            bool: True if the monster is alive.

        """
        return self.wound_points > 0


class Chimaera(Monster):
    """Chimaera class."""

    def __init__(self):
        """Initialize the Chimaera class."""
        super().__init__(
            name="Chimaera",
            resistance_value=2,
            negotiation_value=7,
            treasure=(Treasure.I, None),
            special=FireBreath(),
            combat_bonus=7,
            wound_points_code="2d6+2",
        )


class Cronk(Monster):
    """Cronk class."""

    def __init__(self):
        """Initialize the Cronk class."""
        super().__init__(
            name="Cronk",
            resistance_value=1,
            negotiation_value=9,
            treasure=(Treasure.E, Treasure.B),
            special=Stench(),
            combat_bonus=4,
            wound_points_code="d6+1",
        )


class Demon(Monster):
    """Demon class."""

    def __init__(self):
        """Initialize the Demon class."""
        super().__init__(
            name="Demon",
            resistance_value=4,
            negotiation_value=None,
            treasure=(Treasure.D, None),
            special=DemonSkill(),
            combat_bonus=5,
            wound_points_code="d6+2",
        )


class DireWolf(Monster):
    """DireWolf class."""

    def __init__(self):
        """Initialize the DireWolf class."""
        super().__init__(
            name="Dire Wolf",
            resistance_value=1,
            negotiation_value=9,
            treasure=(Treasure.A, None),
            combat_bonus=1,
            wound_points_code="d3+1",
        )


class EvilHero(Monster):
    """EvilHero class."""

    def __init__(self):
        """Initialize the EvilHero class."""
        super().__init__(
            name="Evil Hero",
            resistance_value=2,
            negotiation_value=5,
            weapon=Sword(),
            treasure=(Treasure.J, Treasure.C),
            combat_bonus=5,
            wound_points_code="d6+4",
        )
        self.weapon_skill = SwordSkill(roll("d6"))


class EvilMage(Monster):
    """EvilMage class."""

    def __init__(self):
        """Initialize the EvilMage class."""
        super().__init__(
            name="Evil Mage",
            resistance_value=2,
            negotiation_value=5,
            spells=[Lightning()],
            treasure=(Treasure.J, Treasure.C),
            combat_bonus=4,
            wound_points_code="d6+3",
        )


class Gargoyle(Monster):
    """Gargoyle class."""

    def __init__(self):
        """Initialize the Gargoyle class."""
        super().__init__(
            name="Gargoyle",
            resistance_value=3,
            negotiation_value=4,
            treasure=(Treasure.G, None),
            combat_bonus=9,
            wound_points_code="3d6+1",
        )


class Harpy(Monster):
    """Harpy class."""

    def __init__(self):
        """Initialize the Harpy class."""
        super().__init__(
            name="Harpy",
            resistance_value=1,
            negotiation_value=5,
            treasure=(Treasure.A, None),
            combat_bonus=0,
            wound_points_code="d3",
        )


class Hydra(Monster):
    """Hydra class."""

    def __init__(self):
        """Initialize the Hydra class."""
        super().__init__(
            name="Hydra",
            resistance_value=3,
            negotiation_value=7,
            treasure=(Treasure.J, None),
            special=HailHydra(),
            combat_bonus=0,
            wound_points_code="2d6+3",
        )


class Medusa(Monster):
    """Medusa class."""

    def __init__(self):
        """Initialize the Medusa class."""
        super().__init__(
            name="Medusa",
            resistance_value=2,
            negotiation_value=5,
            treasure=(Treasure.G, None),
            special=FleshToStone(),
            combat_bonus=2,
            wound_points_code="2d6",
        )


class Minotaur(Monster):
    """Minotaur class."""

    def __init__(self):
        """Initialize the Minotaur class."""
        super().__init__(
            name="Minotaur",
            resistance_value=3,
            negotiation_value=7,
            treasure=(Treasure.J, Treasure.C),
            combat_bonus=10,
            wound_points_code="2d6+4",
        )


class Ogre(Monster):
    """Ogre class."""

    def __init__(self):
        """Initialize the Ogre class."""
        super().__init__(
            name="Ogre",
            resistance_value=2,
            negotiation_value=2,
            weapon=Hammer(),
            treasure=(Treasure.J, Treasure.E),
            combat_bonus=5,
            wound_points_code="d6+2",
        )


class Orc(Monster):
    """Orc class."""

    def __init__(self):
        """Initialize the Orc class."""
        super().__init__(
            name="Orc",
            resistance_value=1,
            negotiation_value=0,
            weapon=Sword(),
            treasure=(Treasure.H, Treasure.B),
            combat_bonus=3,
            wound_points_code="d6",
        )


class Skeleton(Monster):
    """Skeleton class."""

    def __init__(self):
        """Initialize the Skeleton class."""
        super().__init__(
            name="Skeleton",
            resistance_value=1,
            negotiation_value=9,
            treasure=(Treasure.F, Treasure.A),
            combat_bonus=2,
            wound_points_code="d6+1",
        )


class Troll(Monster):
    """Troll class."""

    def __init__(self):
        """Initialize the Troll class."""
        super().__init__(
            name="Troll",
            resistance_value=3,
            negotiation_value=4,
            treasure=(Treasure.J, None),
            special=Regenerate(),
            combat_bonus=6,
            wound_points_code="2d6+3",
        )


class Vampire(Monster):
    """Vampire class."""

    def __init__(self):
        """Initialize the Vampire class."""
        super().__init__(
            name="Vampire",
            resistance_value=4,
            negotiation_value=6,
            treasure=(Treasure.J, None),
            special=Charm(),
            combat_bonus=11,
            wound_points_code="3d6",
        )


class Warg(Monster):
    """Warg class."""

    def __init__(self):
        """Initialize the Warg class."""
        super().__init__(
            name="Warg",
            resistance_value=1,
            negotiation_value=6,
            treasure=(Treasure.A, None),
            combat_bonus=3,
            wound_points_code="d3+2",
        )


class Wight(Monster):
    """Wight class."""

    def __init__(self):
        """Initialize the Wight class."""
        super().__init__(
            name="Wight",
            resistance_value=2,
            negotiation_value=4,
            treasure=(Treasure.H, None),
            combat_bonus=6,
            wound_points_code="2d6",
        )


class Wraith(Monster):
    """Wraith class."""

    def __init__(self):
        """Initialize the Wraith class."""
        super().__init__(
            name="Wraith",
            resistance_value=1,
            negotiation_value=2,
            treasure=(Treasure.I, Treasure.D),
            combat_bonus=3,
            wound_points_code="d6+3",
        )


class XTheUnknown(Monster):
    """XTheUnknown class."""

    def __init__(self):
        """Initialize the XTheUnknown class."""
        super().__init__(
            name="X The Unknown",
            resistance_value=4,
            negotiation_value=None,
            weapon=Sword(),
            spells=[Lightning()],
            treasure=(Treasure.L, None),
            special=XTheUnknownSkill(),
            combat_bonus=5,
            wound_points_code="d6+6",
        )


def spawn_monster(monster_class: type[Monster], level: int = 1, is_wandering: bool = False) -> list[Monster]:
    """Spawn a monster of the given class and level.

    Args:
    ----
        monster_class (Type[Monster]): The class of the monster to spawn.
        level (int): The level of the maze.
        is_wandering (bool): True if the monster is a wandering monster.

    Returns:
    -------
        list[Monster]: A list of monsters.

    Raises:
    ------
        ValueError: If the level is not between 1 and 3.

    """
    if level < 1 or level > 3:
        msg = "Level must be between 1 and 3"
        raise ValueError(msg)

    modifiers = LEVEL_CHART[level - 1]
    monsters = []

    range_modifier = 1 if monster_class.__name__ == "XTheUnknown" else int(modifiers["number_of_monsters"][1:])

    for _ in range(range_modifier):
        monster = monster_class()
        monster.is_wandering = is_wandering
        monster.wound_points += int(modifiers["wound_points"][1:])
        monster.combat_bonus += int(modifiers["combat_bonus"][1:])
        if monster.negotiation_value:
            monster.negotiation_value += int(modifiers["negotiation_value"][1:])
        monster.treasure = (
            monster.treasure[0].add(int(modifiers["treasure_type"][1:])),
            (
                monster.treasure[1].add(int(modifiers["treasure_type"][1:] if monster.treasure[1] else 0))
                if monster.treasure[1]
                else None
            ),
        )
        monster.experience_points *= int(modifiers["experience_points"][1:])
        treasure = monster.hold_treasure
        if treasure:
            monster.actual_treasure = treasure.roll_treasure()
        monsters.append(monster)

    return monsters


def roll_monster(wandering: bool, d1: int, d2: int, level: int = 1) -> list[Monster]:
    """Roll a random monster.

    Args:
    ----
        wandering (bool): True if the monster is a wandering monster.
        d1 (int): The first die roll.
        d2 (int): The second die roll.
        level (int): The level of the maze.

    Returns:
    -------
        list[Monster]: A list of monsters.

    """
    code = WANDERING_MONSTER_TABLE[d1][d2] if wandering else ROOM_MONSTER_TABLE[d1][d2]
    if ":" in code:
        monster, number = code.split(":")
    else:
        monster = code
        number = "1"
    number = roll(number) if "d" in number else int(number)
    monsters = []
    for _ in range(number):
        monster_class = globals()[monster]
        monsters += spawn_monster(monster_class, level, wandering)
    return monsters


def roll_room_monster(level: int = 1):
    """Roll a random room monster.

    Args:
    ----
        level (int): The level of the maze.

    Returns:
    -------
        list[Monster]: A list of monsters.

    """
    d6_1 = roll("d6") - 1
    d6_2 = roll("d6") - 1
    return roll_monster(False, d6_1, d6_2, level)


def roll_wandering_monster(level: int = 1) -> list[Monster]:
    """Roll a random wandering monster.

    Args:
    ----
        level (int): The level of the maze.

    Returns:
    -------
        list[Monster]: A list of monsters.

    """
    d3_1 = roll("d3") - 1
    d6_2 = roll("d6") - 1
    return roll_monster(True, d3_1, d6_2, level)
