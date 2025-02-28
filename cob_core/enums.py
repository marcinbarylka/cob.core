"""Enumerations for the cob_core package."""

import enum


class Exit(enum.IntEnum):
    """Exit."""

    undefined = -1
    wall = 0
    corridor = 1
    room = 2
    room_closed = 3


class Direction(enum.IntEnum):
    """Direction."""

    north = 0
    east = 1
    south = 2
    west = 3


class Axis(enum.IntEnum):
    """Axis."""

    x = 0
    y = 1
    z = 2


class FontMap(enum.StrEnum):
    """Font map."""

    # Room features
    fountain = "F"
    statue = "S"
    trap_door = "T"
    furniture = "f"
    staircase = "s"
    mirror = "M"
    artwork = "a"
    altair = "A"

    party = "@"
    entrance = "E"
    hellgate = "H"

    # Monsters
    chimaera = "C"
    demon = "D"
    gargoyle = "G"
    ogre = "O"
    unknown = "U"
    vampire = "V"
    wight = "W"
    cronk = "c"
    dire_wolf = "d"
    evil_mage = "e"
    harpy = "h"
    minotaur = "m"
    orc = "o"
    troll = "t"
    warg = "v"
    wraith = "w"
    hydra = "x"
    skeleton = "z"
    medusa = "{"
    evil_hero = "~"

    # Heroes & initiates
    gilith = chr(0x100)
    gislan = chr(0x101)
    gwaigilion = chr(0x102)
    larraka = chr(0x103)
    linfalas = chr(0x104)
    lord_dil = chr(0x105)
    maytwist = chr(0x106)
    paladin_glade = chr(0x107)
    raman = chr(0x108)
    sliggoth = chr(0x109)
    stephen_paladin = chr(0x10A)
    theregond = chr(0x10B)
    weldron = chr(0x10C)
    wendolyn = chr(0x10D)
    zurik = chr(0x10E)
    zareth = chr(0x10F)
    alric = chr(0x110)
    curvenol = chr(0x111)
    dalmilandril = chr(0x112)
    dierdra = chr(0x113)
    eodred = chr(0x114)
    gerudirr = chr(0x115)
    almuric = chr(0x116)
    human_a = chr(0x117)
    human_b = chr(0x118)
    human_c = chr(0x119)
    elf_a = chr(0x11A)
    elf_b = chr(0x11B)
    elf_c = chr(0x11C)
    dwarf_a = chr(0x11D)
    dwarf_b = chr(0x11E)
    dwarf_c = chr(0x11F)
