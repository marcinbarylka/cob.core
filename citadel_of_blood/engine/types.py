"""Type definitions for the engine module."""

from typing import Literal

from citadel_of_blood.engine.heroes import Hero, Initiate
from citadel_of_blood.engine.monsters import Monster

type Race = Literal["Human", "Elf", "Dwarf", "Demi-Kronk", "Swamp Creature"]
type MagicPotential = tuple[int, int, int]
type Character = Hero | Initiate | Monster
type PartyPosition = tuple[int, int]
type PartyRank = list[Character | None]

# Validation constants
MAX_INITIATE_WEAPONS: int = 2
MIN_WOUND_POINTS: int = 0
MIN_RESISTANCE_VALUE: int = 0
MIN_COMBAT_BONUS: int = 0
MIN_RANDOM_HEROES: int = 1

# Party constants
MAX_CHARACTERS_IN_RANK: int = 3
MIN_RANK: int = 0
