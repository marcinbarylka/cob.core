"""Hero and Initiate data definitions."""

import enum

from citadel_of_blood import FontMap
from citadel_of_blood.engine.heroes import Hero, Initiate
from citadel_of_blood.engine.skills import (
    AxSkill,
    BowSkill,
    DaggerSkill,
    Detrap,
    HammerSkill,
    Hellgate,
    Negotiation,
    SwordSkill,
)
from citadel_of_blood.engine.weapons import Ax, Bow, Dagger, Hammer, Sword, ThrowDagger


class HeroesEnum(enum.Enum):
    """Available heroes in the game."""

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
        """Get a list of all available heroes.

        Returns:
            List of all heroes in the game
        """
        return list(HeroesEnum.__members__.values())


class InitiatesEnum(enum.Enum):
    """Available initiates in the game."""

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
        """Get a list of all available initiates.

        Returns:
            List of all initiates in the game
        """
        return list(InitiatesEnum.__members__.values())
