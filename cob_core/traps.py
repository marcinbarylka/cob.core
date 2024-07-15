from abc import abstractmethod, ABC

from cob_core import dice
from cob_core.heroes import Hero, Initiate


class Trap(ABC):
    def __init__(self, name: str):
        self.name: str = name

    @abstractmethod
    def detrap(self, detrapper: Hero | Initiate, party: list[Hero | Initiate]):
        """
        Detrap trap. This method should be implemented in child classes. It should contain all the logic of the detrap.
        """
        ...

    @abstractmethod
    def run(self, party: list[Hero | Initiate]):
        """
        Run trap. This method should be implemented in child classes. It should contain all the logic of the trap.
        """
        ...


class Arrow(Trap):
    """Arrow trap class."""

    def __init__(self):
        super().__init__("Arrow")

    def run(): ...
    def detrap(): ...


class PoisonedArrow(Trap):
    """Poisoned arrow trap class."""

    def __init__(self):
        super().__init__("Poisoned Arrow")

    def run(): ...
    def detrap(): ...


class PoisonGas(Trap):
    """Poison gas trap class."""

    def __init__(self):
        super().__init__("Poison Gas")

    def run(): ...
    def detrap(): ...


class Explosion(Trap):
    """Explosion trap class."""

    def __init__(self):
        super().__init__("Explosion")

    def run(): ...
    def detrap(): ...


class FlamingOil(Trap):
    """Flaming oil trap class."""

    def __init__(self):
        super().__init__("Flaming Oil")

    def run(): ...
    def detrap(): ...


def roll_trap() -> list[Trap]:
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
