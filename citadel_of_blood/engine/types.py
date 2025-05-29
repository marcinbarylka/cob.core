"""Type definitions for the engine module."""

from typing import Literal

type Race = Literal["Human", "Elf", "Dwarf", "Demi-Kronk", "Swamp Creature"]
type MagicPotential = tuple[int, int, int]

# Validation constants
MAX_INITIATE_WEAPONS: int = 2
MIN_WOUND_POINTS: int = 0
MIN_RESISTANCE_VALUE: int = 0
MIN_COMBAT_BONUS: int = 0
MIN_RANDOM_HEROES: int = 1
