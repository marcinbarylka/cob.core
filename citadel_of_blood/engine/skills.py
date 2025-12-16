"""Module with skills classes.

It contains all the skills that can be used by characters and monsters.
"""

from abc import ABC, abstractmethod

from citadel_of_blood.engine.weapons import Ax, Bow, Dagger, Hammer, Sword, Weapon


class Skill(ABC):
    """Represent a skill.

    It is used to represent a skill of a character or a monster.
    """

    def __init__(self, value: int):
        """Initialize the skill.

        Args:
            value: The value of the skill.

        """
        self.value: int = value
        self.skill_name: str = self.__class__.__name__

    @abstractmethod
    def run(self, *args, **kwargs):
        """Run skill.

        This method should be implemented in child classes.

        It should contain all the logic of the skill.
        """

    def __str__(self):
        """Return the string representation of the skill."""
        return f"+{self.value} {self.skill_name}"


class Hellgate(Skill):
    """Represent a hellgate skill. It is used to represent a skill of a character."""

    def run(self):
        """Run hellgate skill."""


class Detrap(Skill):
    """Represent a detrap skill. It is used to represent a skill of a character."""

    def run(self):
        """Run detrap skill."""


class Negotiation(Skill):
    """Represent a negotiation skill. It is used to represent a skill of a character."""

    def run(self):
        """Run negotiation skill."""


###### Weapon skills


class WeaponSkill(Skill):
    """Represent a weapon skill. It is used to represent a skill of a character."""

    weapon: Weapon
    """ Weapon of the skill."""

    def __init__(self, value: int):
        """Initialize the weapon skill."""
        super().__init__(value)
        self.skill_name = self.weapon.name

    def run(self):
        """Run weapon skill."""


class SwordSkill(WeaponSkill):
    """Represent a sword skill.

    It is used to represent a skill of a character.
    """

    weapon = Sword()


class BowSkill(WeaponSkill):
    """Represent a bow skill.

    It is used to represent a skill of a character.
    """

    weapon = Bow()


class HammerSkill(WeaponSkill):
    """Represent a hammer skill.

    It is used to represent a skill of a character.
    """

    weapon = Hammer()


class AxSkill(WeaponSkill):
    """Represent an ax skill.

    It is used to represent a skill of a character.
    """

    weapon = Ax()


class DaggerSkill(WeaponSkill):
    """Represent a dagger skill.

    It is used to represent a skill of a character.
    """

    weapon = Dagger()


###### Monster skills


class MonsterSkill(Skill):
    """Represent a monster skill.

    It is used to represent a skill of a monster.
    """

    def __init__(self):
        """Initialize the monster skill."""
        super().__init__(0)

    def __str__(self):
        """Return the string representation of the skill."""
        return self.skill_name

    def run(self):
        """Run monster skill."""


class FireBreath(MonsterSkill):
    """Represent a fire breath skill.

    It is used to represent a skill of a monster.
    """

    def run(self):
        """Run fire breath skill."""


class Stench(MonsterSkill):
    """Represent a stench skill.

    It is used to represent a skill of a monster.
    """

    def run(self):
        """Run stench skill."""


class DemonSkill(MonsterSkill):
    """Represent a demon skill.

    It is used to represent a skill of a monster.
    """

    def run(self):
        """Run demon skill."""


class HailHydra(MonsterSkill):
    """Represent a hail hydra skill.

    It is used to represent a skill of a monster.
    """

    def run(self):
        """Run hail hydra skill."""


class FleshToStone(MonsterSkill):
    """Represent a flesh to stone skill.

    It is used to represent a skill of a monster.
    """

    def run(self):
        """Run flesh to stone skill."""


class Regenerate(MonsterSkill):
    """Represent a regenerate skill. It is used to represent a skill of a monster."""

    def run(self):
        """Run regenerate skill."""


class Charm(MonsterSkill):
    """Represent a charm skill. It is used to represent a skill of a monster."""

    def run(self):
        """Run charm skill."""


class XTheUnknownSkill(MonsterSkill):
    """Represent a x the unknown skill. It is used to represent a skill of a monster."""

    def run(self):
        """Run x the unknown skill."""
