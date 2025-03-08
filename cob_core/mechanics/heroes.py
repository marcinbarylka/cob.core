"""Module for heroes and initiates."""

import enum
from dataclasses import dataclass, field
import random
from typing import Any

from cob_core import FontMap
from cob_core.mechanics import dice
from cob_core.mechanics.armors import Armor
from cob_core.mechanics.skills import (
    AxSkill,
    BowSkill,
    DaggerSkill,
    Detrap,
    HammerSkill,
    Hellgate,
    Negotiation,
    Skill,
    SwordSkill,
    WeaponSkill,
)
from cob_core.mechanics.spells import MAGIC_POTENTIAL_TABLE, Spell
from cob_core.mechanics.weapons import Ax, Bow, Dagger, Hammer, Sword, ThrowDagger, Weapon


@dataclass
class Hero:
    """
    A hero. A character that can be played by a player.
    """

    name: str
    name_short: str
    race: str
    wound_points: int
    magic_potential: tuple[int, int, int]
    resistance_value: int
    combat_bonus: int
    weapons: list[Weapon]
    weapon_skill: WeaponSkill | None
    skill: Skill
    icon: str = ""
    armor: Armor | None = None
    spells: list[Spell] = field(default_factory=list)
    jewels: list[Any] = field(default_factory=list)
    gold_marks: int = 0
    XP: int = 0

    _wound_points: int = 0

    def __post_init__(self):
        """
        Post initialization method.

        It sets the wound points of the hero.

        """
        self._wound_points = self.wound_points

    @property
    def max_wound_points(self):
        """
        Maximum wound points of the hero.

        Returns:
            int: maximum wound points of the hero
        """
        return self._wound_points

    @property
    def is_alive(self) -> bool:
        """Check if the hero is alive.

        Returns:
            bool: True if the hero is alive, False otherwise

        """
        return self.wound_points > 0

    def fight(self, weapon: Weapon) -> int:
        """
        The hero fights with an opponent.

        A hero rolls a dice and adds a combat bonus to the result. If the hero has a weapon skill,
        the value of the skill is added to the result. The result is used to calculate the damage
        that the hero deals to the opponent.

        Args:
            weapon: weapon of the hero

        Returns:
            int: damage that the hero deals to the opponent

        Raises:
            ValueError: if the hero does not have the weapon

        """
        if weapon not in self.weapons:
            raise ValueError(f"{self.name} does not have this weapon.")

        if self.weapon_skill and self.weapon_skill.weapon == weapon:
            roll_dice = dice.roll(f"d6+{self.combat_bonus + self.weapon_skill.value}")
        else:
            roll_dice = dice.roll(f"d6+{self.combat_bonus}")
        return weapon.get_damage(roll_dice)


class Initiate(Hero):
    """
    An Initiate. A character that can be played by a player. It is a weaker version of a hero.
    """

    def __post_init__(self):
        super().__post_init__()
        self.magic_potential = MAGIC_POTENTIAL_TABLE[dice.roll("d6") - 1]

    def add_weapon(self, weapon: Weapon) -> None:
        """
        Add new weapon to the initiate.

        Args:
            weapon: weapon to add

        """
        if len(self.weapons) == 2:
            raise ValueError("The initiate already has two weapons.")
        weapons = list(self.weapons)
        while len(weapons) < 2:
            weapons.append(weapon)
        weapons.append(weapon)
        self.weapons = [weapons[0], weapons[1]]


class HeroesEnum(enum.Enum):
    """
    Enum of heroes.
    """

    almuric = Hero(
        "Almuric",
        "",
        "Human",
        8,
        (1, 1, 2),
        2,
        3,
        [Sword(), Dagger()],
        SwordSkill(1),
        Hellgate(1),
        FontMap.almuric.value,
    )
    alric = Hero(
        "Alric",
        "",
        "Human",
        6,
        (2, 3, 4),
        2,
        0,
        [Sword(), ThrowDagger()],
        None,
        Hellgate(1),
        FontMap.alric.value,
    )
    curvenol = Hero(
        "Curvenol",
        "Curvnol",
        "Human",
        5,
        (5, 5, 5),
        1,
        0,
        [Sword(), ThrowDagger()],
        None,
        Hellgate(2),
        FontMap.curvenol.value,
    )
    dalmilandril = Hero(
        "Dalmilandril",
        "Dalmilan",
        "Elf",
        5,
        (3, 4, 5),
        3,
        2,
        [Bow(), Dagger()],
        BowSkill(2),
        Negotiation(2),
        FontMap.dalmilandril.value,
    )
    dierdra = Hero(
        "Dierdra",
        "",
        "Human",
        7,
        (0, 0, 0),
        1,
        4,
        [Hammer(), Sword()],
        HammerSkill(1),
        Hellgate(1),
        FontMap.dierdra.value,
    )
    eodred = Hero(
        "Eodred",
        "",
        "Human",
        6,
        (3, 4, 5),
        2,
        0,
        [Bow(), ThrowDagger()],
        None,
        Hellgate(2),
        FontMap.eodred.value,
    )
    gerudirr = Hero(
        "Gerudirr",
        "",
        "Dwarf",
        6,
        (0, 0, 0),
        2,
        6,
        [Ax(), Dagger()],
        AxSkill(3),
        Detrap(3),
        FontMap.gerudirr.value,
    )
    gilith = Hero(
        "Gilith",
        "",
        "Elf",
        8,
        (0, 0, 0),
        3,
        4,
        [Bow(), Dagger()],
        BowSkill(2),
        Negotiation(2),
        FontMap.gilith.value,
    )
    gislan = Hero(
        "Gislan",
        "",
        "Dwarf",
        10,
        (4, 4, 4),
        3,
        4,
        [Ax(), Hammer()],
        AxSkill(2),
        Detrap(3),
        FontMap.gislan.value,
    )
    gwaigilion = Hero(
        "Gwaigilion",
        "Gwg Eln",
        "Elf",
        7,
        (4, 3, 2),
        3,
        4,
        [Bow(), Dagger()],
        BowSkill(2),
        Negotiation(1),
        FontMap.gwaigilion.value,
    )
    larraka = Hero(
        "Larraka",
        "",
        "Human",
        5,
        (6, 5, 4),
        3,
        0,
        [Bow(), Dagger()],
        None,
        Hellgate(1),
        FontMap.larraka.value,
    )
    linfalas = Hero(
        "Linfalas",
        "",
        "Elf",
        9,
        (0, 0, 0),
        2,
        5,
        [Bow(), Sword()],
        BowSkill(2),
        Negotiation(3),
        FontMap.linfalas.value,
    )
    lord_dil = Hero(
        "Lord Dil",
        "",
        "Human",
        10,
        (0, 0, 0),
        3,
        5,
        [Sword(), Dagger()],
        SwordSkill(2),
        Hellgate(2),
        FontMap.lord_dil.value,
    )
    maytwist = Hero(
        "Maytwist",
        "Maytwst",
        "Elf",
        7,
        (3, 3, 3),
        2,
        0,
        [ThrowDagger(), Bow()],
        BowSkill(2),
        Negotiation(2),
        FontMap.maytwist.value,
    )
    paladin_glade = Hero(
        "Paladin Glade",
        "Pl Glade",
        "Human",
        10,
        (0, 0, 0),
        2,
        4,
        [Sword(), ThrowDagger()],
        SwordSkill(2),
        Hellgate(2),
        FontMap.paladin_glade.value,
    )
    raman = Hero(
        "Raman",
        "Rm Crnk",
        "Demi-Kronk",
        9,
        (0, 0, 0),
        3,
        4,
        [Sword(), Dagger()],
        SwordSkill(1),
        Detrap(1),
        FontMap.raman.value,
    )
    sliggoth = Hero(
        "Sliggoth",
        "",
        "Swamp Creature",
        8,
        (1, 2, 3),
        2,
        4,
        [Ax(), Bow()],
        AxSkill(1),
        Detrap(1),
        FontMap.sliggoth.value,
    )
    stephen_paladin = Hero(
        "Stephen Paladin",
        "Stphn Pl",
        "Human",
        10,
        (0, 0, 0),
        2,
        5,
        [Sword(), Dagger()],
        SwordSkill(2),
        Hellgate(2),
        FontMap.stephen_paladin.value,
    )
    theregond = Hero(
        "Theregond",
        "Thrgond",
        "Human",
        8,
        (4, 3, 2),
        2,
        1,
        [Sword(), ThrowDagger()],
        SwordSkill(3),
        Hellgate(3),
        FontMap.theregond.value,
    )
    weldron = Hero(
        "Weldron",
        "Wldron",
        "Human",
        9,
        (0, 0, 0),
        2,
        5,
        [Sword(), Bow()],
        SwordSkill(2),
        Hellgate(3),
        FontMap.weldron.value,
    )
    wendolyn = Hero(
        "Wendolyn",
        "Wndlyn",
        "Human",
        7,
        (4, 3, 2),
        2,
        1,
        [Sword(), Dagger()],
        DaggerSkill(2),
        Hellgate(4),
        FontMap.wendolyn.value,
    )
    zareth = Hero(
        "Zareth",
        "",
        "Human",
        9,
        (0, 0, 0),
        4,
        4,
        [Sword(), ThrowDagger()],
        SwordSkill(1),
        Hellgate(3),
        FontMap.zareth.value,
    )
    zurik = Hero(
        "Zurik",
        "",
        "Dwarf",
        8,
        (3, 4, 5),
        2,
        3,
        [Ax(), Dagger()],
        AxSkill(2),
        Detrap(3),
        FontMap.zurik.value,
    )

    @staticmethod
    def to_list() -> list[Hero]:
        """
        Get a list of heroes.
        """
        return list(HeroesEnum.__members__.values())


class InitiatesEnum(enum.Enum):
    """
    Enum of initiates.
    """

    human_a = Initiate(
        name="",
        name_short="Human A",
        race="Human",
        wound_points=7,
        resistance_value=1,
        weapons=[],
        weapon_skill=SwordSkill(1),
        skill=Hellgate(1),
        combat_bonus=0,
        magic_potential=(0, 0, 0),
        icon=FontMap.human_a.value,
    )
    human_b = Initiate(
        name="",
        name_short="Human B",
        race="Human",
        wound_points=7,
        resistance_value=1,
        weapons=[],
        weapon_skill=SwordSkill(1),
        skill=Hellgate(1),
        combat_bonus=0,
        magic_potential=(0, 0, 0),
        icon=FontMap.human_b.value,
    )
    human_c = Initiate(
        name="",
        name_short="Human C",
        race="Human",
        wound_points=7,
        resistance_value=1,
        weapons=[],
        weapon_skill=SwordSkill(1),
        skill=Hellgate(1),
        combat_bonus=0,
        magic_potential=(0, 0, 0),
        icon=FontMap.human_c.value,
    )
    elf_a = Initiate(
        name="",
        name_short="Elf A",
        race="Elf",
        wound_points=5,
        resistance_value=2,
        weapons=[],
        weapon_skill=BowSkill(1),
        skill=Negotiation(1),
        combat_bonus=0,
        magic_potential=(0, 0, 0),
        icon=FontMap.elf_a.value,
    )
    elf_b = Initiate(
        name="",
        name_short="Elf B",
        race="Elf",
        wound_points=5,
        resistance_value=2,
        weapons=[],
        weapon_skill=BowSkill(1),
        skill=Negotiation(1),
        combat_bonus=0,
        magic_potential=(0, 0, 0),
        icon=FontMap.elf_b.value,
    )
    elf_c = Initiate(
        name="",
        name_short="Elf C",
        race="Elf",
        wound_points=5,
        resistance_value=2,
        weapons=[],
        weapon_skill=BowSkill(1),
        skill=Negotiation(1),
        combat_bonus=0,
        magic_potential=(0, 0, 0),
        icon=FontMap.elf_c.value,
    )
    dwarf_a = Initiate(
        name="",
        name_short="Dwarf A",
        race="Dwarf",
        wound_points=6,
        resistance_value=2,
        weapons=[],
        weapon_skill=AxSkill(1),
        skill=Detrap(1),
        combat_bonus=0,
        magic_potential=(0, 0, 0),
        icon=FontMap.dwarf_a.value,
    )
    dwarf_b = Initiate(
        name="",
        name_short="Dwarf B",
        race="Dwarf",
        wound_points=6,
        resistance_value=2,
        weapons=[],
        weapon_skill=AxSkill(1),
        skill=Detrap(1),
        combat_bonus=0,
        magic_potential=(0, 0, 0),
        icon=FontMap.dwarf_b.value,
    )
    dwarf_c = Initiate(
        name="",
        name_short="Dwarf C",
        race="Dwarf",
        wound_points=6,
        resistance_value=2,
        weapons=[],
        weapon_skill=AxSkill(1),
        skill=Detrap(1),
        combat_bonus=0,
        magic_potential=(0, 0, 0),
        icon=FontMap.dwarf_c.value,
    )

    @staticmethod
    def to_list() -> list[Initiate]:
        """
        Get a list of heroes.
        """
        return list(InitiatesEnum.__members__.values())


def random_heroes(how_many: int = 3) -> list[Hero]:
    """
    Get random heroes.

    Args:
        how_many: number of heroes to get

    Returns:
        list: list of random heroes

    """
    if how_many > 3:
        raise ValueError(f"Too many heroes requested. Maximum is 3, but {how_many} requested.")
    if how_many < 1:
        raise ValueError(f"Too few heroes requested. Minimum is 1, but {how_many} requested.")
    return random.sample(HeroesEnum.to_list(), how_many)
