from abc import ABC, abstractmethod

from cob_core import dice
from cob_core.heroes import Hero, Initiate, Party


class Trap(ABC):
    def __init__(self, name: str):
        self.name: str = name

    def detrap(self, detrapper: Hero | Initiate) -> bool:
        """
        Detrap trap. This method should be implemented in child classes. It should contain all the logic of the detrap.
        """
        if detrapper.skill is not None and detrapper.skill.skill_name == "Detrap":
            d6 = dice.roll("d6")
            if detrapper.skill.value <= d6:
                return True
        return False

    @abstractmethod
    def run(self, detrapper: Hero | Initiate, party: Party) -> None:
        """
        Run trap. This method should be implemented in child classes. It should contain all the logic of the trap.
        """
        ...


class Arrow(Trap):
    """Arrow trap class."""

    def __init__(self):
        super().__init__("Arrow")

    def run(self, detrapper: Hero | Initiate, party: Party):  # noqa
        from cob_core.weapons import Bow

        d6 = dice.roll("d6")
        wounds = Bow().get_damage(d6)
        detrapper.wound_points -= wounds


class PoisonedArrow(Trap):
    """Poisoned arrow trap class."""

    def __init__(self):
        super().__init__("Poisoned Arrow")

    def run(self, detrapper: Hero | Initiate, party: Party):
        from cob_core.weapons import Bow

        d6 = dice.roll("d6")
        wounds = Bow().get_damage(d6)
        d3 = dice.roll("d3")
        wounds += Bow().get_damage(d3)
        detrapper.wound_points -= wounds


class PoisonGas(Trap):
    """Poison gas trap class."""

    def __init__(self):
        super().__init__("Poison Gas")

    def run(self, detrapper: Hero | Initiate, party: Party):
        detrapper.wound_points -= dice.roll("d3")


class Explosion(Trap):
    """Explosion trap class."""

    def __init__(self):
        super().__init__("Explosion")

    def run(self, detrapper: Hero | Initiate, party: Party):
        for hero in party.heroes:
            hero.wound_points -= 1


class FlamingOil(Trap):
    """Flaming oil trap class."""

    def __init__(self):
        super().__init__("Flaming Oil")

    def run(self, detrapper: Hero | Initiate, party: Party):
        detrapper.wound_points -= dice.roll("d3")


def roll_trap() -> list[Trap]:  # noqa
    """Roll dice for trap."""
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
