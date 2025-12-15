"""Enumerations for the citadel_of_blood package."""

import enum


class Exit(enum.IntEnum):
    """Exit."""

    UNDEFINED = -1
    WALL = 0
    CORRIDOR = 1
    ROOM = 2
    ROOM_CLOSED = 3


class Direction(enum.IntEnum):
    """Direction."""

    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Axis(enum.IntEnum):
    """Axis."""

    X = 0
    Y = 1
    Z = 2


class FontMap(enum.StrEnum):
    """Font map."""

    # Room features
    FOUNTAIN = "F"
    STATUE = "S"
    TRAP_DOOR = "T"
    FURNITURE = "f"
    STAIRCASE = "s"
    MIRROR = "M"
    ARTWORK = "a"
    ALTAR = "A"

    PARTY = "@"
    ENTRANCE = "E"
    HELLGATE = "H"

    # Monsters
    CHIMAERA = "C"
    DEMON = "D"
    GARGOYLE = "G"
    OGRE = "O"
    UNKNOWN = "U"
    VAMPIRE = "V"
    WIGHT = "W"
    CRONK = "c"
    DIRE_WOLF = "d"
    EVIL_MAGE = "e"
    HARPY = "h"
    MINOTAUR = "m"
    ORC = "o"
    TROLL = "t"
    WARG = "v"
    WRAITH = "w"
    HYDRA = "x"
    SKELETON = "z"
    MEDUSA = "{"
    EVIL_HERO = "~"

    # Heroes & initiates
    GILITH = chr(0x100)
    GISLAN = chr(0x101)
    GWAIGILION = chr(0x102)
    LARRAKA = chr(0x103)
    LINFALAS = chr(0x104)
    LORD_DIL = chr(0x105)
    MAYTWIST = chr(0x106)
    PALADIN_GLADE = chr(0x107)
    RAMAN = chr(0x108)
    SLIGGOTH = chr(0x109)
    STEPHEN_PALADIN = chr(0x10A)
    THEREGOND = chr(0x10B)
    WELDRON = chr(0x10C)
    WENDOLYN = chr(0x10D)
    ZURIK = chr(0x10E)
    ZARETH = chr(0x10F)
    ALRIC = chr(0x110)
    CURVENOL = chr(0x111)
    DALMILANDRIL = chr(0x112)
    DIERDRA = chr(0x113)
    EODRED = chr(0x114)
    GERUDIRR = chr(0x115)
    ALMURIC = chr(0x116)
    HUMAN_A = chr(0x117)
    HUMAN_B = chr(0x118)
    HUMAN_C = chr(0x119)
    ELF_A = chr(0x11A)
    ELF_B = chr(0x11B)
    ELF_C = chr(0x11C)
    DWARF_A = chr(0x11D)
    DWARF_B = chr(0x11E)
    DWARF_C = chr(0x11F)
