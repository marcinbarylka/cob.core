"""Module for traps classes and functions."""

from abc import ABC, abstractmethod

from citadel_of_blood.mechanics import dice
from citadel_of_blood.mechanics.heroes import Hero, Initiate
from citadel_of_blood.mechanics.party import Party


class Trap(ABC):
    """Trap class. It is an abstract class for traps."""

    def __init__(self, name: str) -> None:
        """Initialize the trap.

        Args:
            name: The name of the trap.

        """
        self.name: str = name

    def detrap(self, detrapper: Hero | Initiate) -> bool:
        """Detrap trap. This method should be implemented in child classes.

        Args:
            detrapper: hero or initiate trying to detrap the trap

        Returns:
            bool: True if the trap is detrapped, False otherwise

        """
        if detrapper.skill is not None and detrapper.skill.skill_name == "Detrap":
            d6 = dice.roll("d6")
            if detrapper.skill.value <= d6:
                return True
        return False

    @abstractmethod
    def spring(self, detrapper: Hero | Initiate, party: Party) -> None:
        """Run trap. This method should be implemented in child classes. It should contain all the logic of the trap.

        Args:
            detrapper: hero or initiate that triggered the trap
            party: party of the heroes

        """


class Arrow(Trap):
    """Arrow trap class."""

    def __init__(self):
        """Initialize the arrow trap."""
        super().__init__("Arrow")

    def spring(self, detrapper: Hero | Initiate, party: Party) -> None:
        """Run arrow trap.

        Args:
            detrapper: hero or initiate that triggered the trap
            party: party of the heroes

        """
        from citadel_of_blood.mechanics.weapons import Bow

        d6 = dice.roll("d6")
        wounds = Bow().get_damage(d6)
        detrapper.wound_points -= wounds


class PoisonedArrow(Trap):
    """Poisoned arrow trap class."""

    def __init__(self):
        """Initialize the poisoned arrow trap."""
        super().__init__("Poisoned Arrow")

    def spring(self, detrapper: Hero | Initiate, party: Party):
        """Run poisoned arrow trap.

        Args:
            detrapper: hero or initiate that triggered the trap
            party: party of the heroes

        """
        from citadel_of_blood.mechanics.weapons import Bow

        d6 = dice.roll("d6")
        wounds = Bow().get_damage(d6)
        d3 = dice.roll("d3")
        wounds += d3
        detrapper.wound_points -= wounds


class PoisonGas(Trap):
    """Poison gas trap class."""

    def __init__(self):
        """Initialize the poison gas trap."""
        super().__init__("Poison Gas")

    def spring(self, detrapper: Hero | Initiate, party: Party):
        """Run poison gas trap.

        Args:
            detrapper: hero or initiate that triggered the trap
            party: party of the heroes

        """
        detrapper.wound_points -= dice.roll("d3")


class Explosion(Trap):
    """Explosion trap class."""

    def __init__(self):
        """Initialize the explosion trap."""
        super().__init__("Explosion")

    def spring(self, detrapper: Hero | Initiate, party: Party):
        """Run explosion trap.

        Args:
            detrapper: hero or initiate that triggered the trap
            party: party of the heroes

        """
        for hero in party.beings:
            hero.wound_points -= 1


class FlamingOil(Trap):
    """Flaming oil trap class."""

    def __init__(self):
        """Initialize the flaming oil trap."""
        super().__init__("Flaming Oil")

    def spring(self, detrapper: Hero | Initiate, party: Party):
        """Run flaming oil trap.

        Args:
            detrapper: hero or initiate that triggered the trap
            party: party of the heroes

        """
        detrapper.wound_points -= dice.roll("d3")


def roll_trap() -> list[Trap]:
    """Roll dice for trap.

    Returns:
        list: list of traps

    """
    roll = dice.roll("d6")
    match roll:
        case 1:
            return [Arrow()]
        case 2:
            return [PoisonedArrow()]
        case 3:
            return [PoisonGas()]
        case 4:
            return [Explosion()]
        case 5:
            return [FlamingOil()]
        case 6:
            return roll_trap() + roll_trap()
