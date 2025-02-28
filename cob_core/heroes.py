"""Module for heroes and initiates."""

import enum
from dataclasses import dataclass, field
from typing import Any

from cob_core import dice, FontMap
from cob_core.armors import Armor
from cob_core.skills import (
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
from cob_core.spells import MAGIC_POTENTIAL_TABLE, Spell
from cob_core.weapons import Ax, Bow, Dagger, Hammer, Sword, ThrowDagger, Weapon


@dataclass
class Hero:
    """
    A hero. A character that can be played by a player.

    :param name: name of the hero
    :param name_short: short name of the hero
    :param race: a race of the hero (i.e. Human, Dwarf, Elf, Demi-Kronk, Swamp Creature)
    :param wound_points: wound points of the hero
    :param magic_potential: magic potential of the hero
    :param resistance_value: resistance value of the hero
    :param combat_bonus: combat bonus of the hero
    :param weapons: weapons of the hero
    :param weapon_skill: weapon skill of the hero
    :param skill: skill of the hero
    :param icon: icon of the hero
    :param armor: armor of the hero
    :param spells: spells of the hero
    :param jewels: jewels of the hero
    :param gold_marks: gold marks of the hero
    :param XP: experience points of the hero
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

    ALMURIC = Hero(
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
        FontMap.ALMURIC.value,
    )
    ALRIC = Hero(
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
        FontMap.ALRIC.value,
    )
    CURVENOL = Hero(
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
        FontMap.CURVENOL.value,
    )
    DALMILANDRIL = Hero(
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
        FontMap.DALMILANDRIL.value,
    )
    DIERDRA = Hero(
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
        FontMap.DIERDRA.value,
    )
    EODRED = Hero(
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
        FontMap.EODRED.value,
    )
    GERUDIRR = Hero(
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
        FontMap.GERUDIRR.value,
    )
    GILITH = Hero(
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
        FontMap.GILITH.value,
    )
    GISLAN = Hero(
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
        FontMap.GISLAN.value,
    )
    GWAIGILION = Hero(
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
        FontMap.GWAIGILION.value,
    )
    LARRAKA = Hero(
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
        FontMap.LARRAKA.value,
    )
    LINFALAS = Hero(
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
        FontMap.LINFALAS.value,
    )
    LORD_DIL = Hero(
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
        FontMap.LORD_DIL.value,
    )
    MAYTWIST = Hero(
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
        FontMap.MAYTWIST.value,
    )
    PALADIN_GLADE = Hero(
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
        FontMap.PALADIN_GLADE.value,
    )
    RAMAN = Hero(
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
        FontMap.RAMAN.value,
    )
    SLIGGOTH = Hero(
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
        FontMap.SLIGGOTH.value,
    )
    STEPHEN_PALADIN = Hero(
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
        FontMap.STEPHEN_PALADIN.value,
    )
    THEREGOND = Hero(
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
        FontMap.THEREGOND.value,
    )
    WELDRON = Hero(
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
        FontMap.WELDRON.value,
    )
    WENDOLYN = Hero(
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
        FontMap.WENDOLYN.value,
    )
    ZARETH = Hero(
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
        FontMap.ZARETH.value,
    )
    ZURIK = Hero(
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
        FontMap.ZURIK.value,
    )


class InitiatesEnum(enum.Enum):
    """
    Enum of initiates.
    """

    HUMAN_A = Initiate(
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
        icon=FontMap.HUMAN_A.value,
    )
    HUMAN_B = Initiate(
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
        icon=FontMap.HUMAN_B.value,
    )
    HUMAN_C = Initiate(
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
        icon=FontMap.HUMAN_C.value,
    )
    ELF_A = Initiate(
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
        icon=FontMap.ELF_A.value,
    )
    ELF_B = Initiate(
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
        icon=FontMap.ELF_B.value,
    )
    ELF_C = Initiate(
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
        icon=FontMap.ELF_C.value,
    )
    DWARF_A = Initiate(
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
        icon=FontMap.DWARF_A.value,
    )
    DWARF_B = Initiate(
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
        icon=FontMap.DWARF_B.value,
    )
    DWARF_C = Initiate(
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
        icon=FontMap.DWARF_C.value,
    )
