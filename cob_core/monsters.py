from dataclasses import dataclass
from typing import Any, Type

from cob_core.dice import roll
from cob_core.skills import (
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
from cob_core.spells import Lightning, Spell
from cob_core.treasures import Treasure
from cob_core.weapons import Hammer
from cob_core.weapons import Monster as MonsterWeapon
from cob_core.weapons import Sword, Weapon

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
        if not self.weapon:
            self.weapon = MonsterWeapon()
        self.wound_points = roll(self.wound_points_code)
        self._wound_points = self.wound_points
        self.experience_points = self._wound_points * 6

    @property
    def max_wound_points(self):
        return self._wound_points

    @property
    def hold_treasure(self):
        return self.treasure[1] if self.is_wandering else self.treasure[0]

    def get_treasure(self):
        if self.is_wandering:
            return self.treasure[1]
        return self.treasure[0]

    def fight(self):
        """
        The monster fights with the hero.
        """
        ...

    def cast_spell(self):
        if not self.spells:
            return None

    @property
    def is_alive(self) -> bool:
        """
        Check if the monster is alive.

        :return: bool.
        """
        return self.wound_points > 0


class Chimaera(Monster):
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
        super().__init__(
            name="Dire Wolf",
            resistance_value=1,
            negotiation_value=9,
            treasure=(Treasure.A, None),
            combat_bonus=1,
            wound_points_code="d3+1",
        )


class EvilHero(Monster):
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
        super().__init__(
            name="Gargoyle",
            resistance_value=3,
            negotiation_value=4,
            treasure=(Treasure.G, None),
            combat_bonus=9,
            wound_points_code="3d6+1",
        )


class Harpy(Monster):
    def __init__(self):
        super().__init__(
            name="Harpy",
            resistance_value=1,
            negotiation_value=5,
            treasure=(Treasure.A, None),
            combat_bonus=0,
            wound_points_code="d3",
        )


class Hydra(Monster):
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
        super().__init__(
            name="Minotaur",
            resistance_value=3,
            negotiation_value=7,
            treasure=(Treasure.J, Treasure.C),
            combat_bonus=10,
            wound_points_code="2d6+4",
        )


class Ogre(Monster):
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
        super().__init__(
            name="Skeleton",
            resistance_value=1,
            negotiation_value=9,
            treasure=(Treasure.F, Treasure.A),
            combat_bonus=2,
            wound_points_code="d6+1",
        )


class Troll(Monster):
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
        super().__init__(
            name="Warg",
            resistance_value=1,
            negotiation_value=6,
            treasure=(Treasure.A, None),
            combat_bonus=3,
            wound_points_code="d3+2",
        )


class Wight(Monster):
    def __init__(self):
        super().__init__(
            name="Wight",
            resistance_value=2,
            negotiation_value=4,
            treasure=(Treasure.H, None),
            combat_bonus=6,
            wound_points_code="2d6",
        )


class Wraith(Monster):
    def __init__(self):
        super().__init__(
            name="Wraith",
            resistance_value=1,
            negotiation_value=2,
            treasure=(Treasure.I, Treasure.D),
            combat_bonus=3,
            wound_points_code="d6+3",
        )


class XTheUnknown(Monster):
    def __init__(self):
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


def spawn_monster(monster_class: Type[Monster], level: int = 1, is_wandering: bool = False) -> list[Monster]:
    """
    Spawn a monster of the given class and level.

    :param monster_class: Type[Monster]: The class of the monster.
    :param level: int: The level of the maze.
    :param is_wandering: bool: True if the monster is a wandering monster.

    :return: list[Monster]: A list of monsters.
    """
    if level < 1 or level > 3:
        raise ValueError("Level must be between 1 and 3")

    modifiers = LEVEL_CHART[level - 1]
    monsters = []

    if monster_class.__name__ == "XTheUnknown":
        range_modifier = 1
    else:
        range_modifier = int(modifiers["number_of_monsters"][1:])

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
    """
    Roll a random monster.

    :param wandering: bool: True if the monster is a wandering monster.
    :param d1: int: The first die roll.
    :param d2: int: The second die roll.
    :param level: int: The level of the maze.

    :return: list[Monster]: A list of monsters.
    """
    if wandering:
        code = WANDERING_MONSTER_TABLE[d1][d2]
    else:
        code = ROOM_MONSTER_TABLE[d1][d2]
    if ":" in code:
        monster, number = code.split(":")
    else:
        monster = code
        number = "1"
    if "d" in number:
        number = roll(number)
    else:
        number = int(number)
    monsters = []
    for _ in range(number):
        monster_class = globals()[monster]
        monsters.append(spawn_monster(monster_class, level, wandering))
    return monsters


def roll_room_monster(level: int = 1):
    """
    Roll a random room monster.

    :param level: int: The level of the maze.

    :return: list[Monster]: A list of monsters.
    """
    d6_1 = roll("d6") - 1
    d6_2 = roll("d6") - 1
    return roll_monster(False, d6_1, d6_2, level)


def roll_wandering_monster(level: int = 1):
    """
    Roll a random wandering monster.

    :param level: int: The level of the maze.

    :return: list[Monster]: A list of monsters.
    """
    d3_1 = roll("d3") - 1
    d6_2 = roll("d6") - 1
    return roll_monster(True, d3_1, d6_2, level)
