from dataclasses import dataclass

from cob_core.skills import (
    Charm,
    DemonSkill,
    FireBreath,
    FleshToStone,
    HailHydra,
    Regenerate,
    Skill,
    Stench,
    XTheUnknownSkill,
)
from cob_core.spells import Lightning, Spell
from cob_core.treasures import Treasure
from cob_core.weapons import Hammer, Sword, Weapon


@dataclass
class Monster:
    name: str = ""
    resistance_value: int = 0
    negotiation_value: int | None = None
    weapon: Weapon | None = None
    spells: list[Spell] | None = None
    treasure: tuple[Treasure, Treasure | None] = (Treasure.A, None)
    special: Skill | None = None  # special skill for monster

    def fight(self):
        """
        The monster fights with the hero.
        """
        ...

    @property
    def is_alive(self) -> bool:
        """
        Check if the monster is alive.

        :return: bool.
        """
        ...


class Chimaera(Monster):
    def __init__(self):
        super().__init__(
            name="Chimaera",
            resistance_value=2,
            negotiation_value=7,
            treasure=(Treasure.I, None),
            special=FireBreath(),
        )


class Cronk(Monster):
    def __init__(self):
        super().__init__(
            name="Cronk",
            resistance_value=1,
            negotiation_value=9,
            treasure=(Treasure.E, Treasure.B),
            special=Stench(),
        )


class Demon(Monster):
    def __init__(self):
        super().__init__(
            name="Demon",
            resistance_value=4,
            negotiation_value=None,
            treasure=(Treasure.D, None),
            special=DemonSkill(),
        )


class DireWolf(Monster):
    def __init__(self):
        super().__init__(
            name="Dire Wolf",
            resistance_value=1,
            negotiation_value=9,
            treasure=(Treasure.A, None),
        )


class EvilHero(Monster):
    def __init__(self):
        super().__init__(
            name="Evil Hero",
            resistance_value=2,
            negotiation_value=5,
            weapon=Sword(),
            treasure=(Treasure.J, Treasure.C),
        )

    # TODO: Evil Hero has a 1d6 weapon skill, that gives him a proficiency with a sword


class EvilMage(Monster):
    def __init__(self):
        super().__init__(
            name="Evil Mage",
            resistance_value=2,
            negotiation_value=5,
            spells=[Lightning()],
            treasure=(Treasure.J, Treasure.C),
        )


class Gargoyle(Monster):
    def __init__(self):
        super().__init__(
            name="Gargoyle",
            resistance_value=3,
            negotiation_value=4,
            treasure=(Treasure.G, None),
        )


class Harpy(Monster):
    def __init__(self):
        super().__init__(
            name="Harpy",
            resistance_value=1,
            negotiation_value=5,
            treasure=(Treasure.A, None),
        )


class Hydra(Monster):
    def __init__(self):
        super().__init__(
            name="Hydra",
            resistance_value=3,
            negotiation_value=7,
            treasure=(Treasure.J, None),
            special=HailHydra(),
        )


class Medusa(Monster):
    def __init__(self):
        super().__init__(
            name="Medusa",
            resistance_value=2,
            negotiation_value=5,
            treasure=(Treasure.G, None),
            special=FleshToStone(),
        )


class Minotaur(Monster):
    def __init__(self):
        super().__init__(
            name="Minotaur",
            resistance_value=3,
            negotiation_value=7,
            treasure=(Treasure.J, Treasure.C),
        )


class Ogre(Monster):
    def __init__(self):
        super().__init__(
            name="Ogre",
            resistance_value=2,
            negotiation_value=2,
            weapon=Hammer(),
            treasure=(Treasure.J, Treasure.E),
        )


class Orc(Monster):
    def __init__(self):
        super().__init__(
            name="Orc",
            resistance_value=1,
            negotiation_value=0,
            weapon=Sword(),
            treasure=(Treasure.H, Treasure.B),
        )


class Skeleton(Monster):
    def __init__(self):
        super().__init__(
            name="Skeleton",
            resistance_value=1,
            negotiation_value=9,
            treasure=(Treasure.F, Treasure.A),
        )


class Troll(Monster):
    def __init__(self):
        super().__init__(
            name="Troll",
            resistance_value=3,
            negotiation_value=4,
            treasure=(Treasure.J, None),
            special=Regenerate(),
        )


class Vampire(Monster):
    def __init__(self):
        super().__init__(
            name="Vampire",
            resistance_value=4,
            negotiation_value=6,
            treasure=(Treasure.J, None),
            special=Charm(),
        )


class Warg(Monster):
    def __init__(self):
        super().__init__(
            name="Warg",
            resistance_value=1,
            negotiation_value=6,
            treasure=(Treasure.A, None),
        )


class Wight(Monster):
    def __init__(self):
        super().__init__(
            name="Wight",
            resistance_value=2,
            negotiation_value=4,
            treasure=(Treasure.H, None),
        )


class Wraith(Monster):
    def __init__(self):
        super().__init__(
            name="Wraith",
            resistance_value=1,
            negotiation_value=2,
            treasure=(Treasure.I, Treasure.D),
        )


class XTheUnknown(Monster):
    def __init__(self):
        super().__init__(
            name="X The Unknown",
            resistance_value=4,
            negotiation_value=None,
            weapon=Sword(),
            spells=[Lightning()],
            treasure=(Treasure.L, None),
            special=XTheUnknownSkill(),
        )
