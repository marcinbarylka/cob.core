from abc import ABC, abstractmethod

from cob_core.weapons import Ax, Bow, Dagger, Hammer, Sword, Weapon


class Skill(ABC):
    """
    This class represents a skill. It is used to represent a skill of a character.

    :param value: value of the skill
    """

    def __init__(self, value: int):
        self.value: int = value
        self.skill_name: str = self.__class__.__name__

    @abstractmethod
    def run(self, *args, **kwargs):
        """
        Run skill. This method should be implemented in child classes. It should contain all the logic of the skill.
        """
        ...

    def __str__(self):
        return f"+{self.value} {self.skill_name}"


class Hellgate(Skill):
    """
    This class represents a hellgate skill. It is used to represent a skill of a character.
    """

    def run(self): ...


class Detrap(Skill):
    """
    This class represents a detrap skill. It is used to represent a skill of a character.
    """

    def run(self): ...


class Negotiation(Skill):
    """
    This class represents a negotiation skill. It is used to represent a skill of a character.
    """

    def run(self): ...


###### Weapon skills


class WeaponSkill(Skill):
    """
    This class represents a weapon skill. It is used to represent a skill of a character.

    :param value: value of the skill
    """

    weapon: Weapon
    """ Weapon of the skill."""

    def __init__(self, value: int):
        super().__init__(value)
        self.skill_name = self.weapon.name

    def run(self): ...


class SwordSkill(WeaponSkill):
    """
    This class represents a sword skill. It is used to represent a skill of a character.
    """

    weapon = Sword()


class BowSkill(WeaponSkill):
    """
    This class represents a bow skill. It is used to represent a skill of a character.
    """

    weapon = Bow()


class HammerSkill(WeaponSkill):
    """
    This class represents a hammer skill. It is used to represent a skill of a character.
    """

    weapon = Hammer()


class AxSkill(WeaponSkill):
    """
    This class represents an ax skill. It is used to represent a skill of a character.
    """

    weapon = Ax()


class DaggerSkill(WeaponSkill):
    """
    This class represents a dagger skill. It is used to represent a skill of a character.
    """

    weapon = Dagger()


###### Monster skills


class MonsterSkill(Skill):
    def __init__(self):
        super().__init__(0)

    def __str__(self):
        return self.skill_name

    def run(self): ...


class FireBreath(MonsterSkill):
    """
    This class represents a fire breath skill. It is used to represent a skill of a monster.
    """

    def run(self): ...


class Stench(MonsterSkill):
    """
    This class represents a stench skill. It is used to represent a skill of a monster.
    """

    def run(self): ...


class DemonSkill(MonsterSkill):
    """
    This class represents a demon skill. It is used to represent a skill of a monster.
    """

    def run(self): ...


class HailHydra(MonsterSkill):
    """
    This class represents a hydra skill. It is used to represent a skill of a monster.
    """

    def run(self): ...


class FleshToStone(MonsterSkill):
    """
    This class represents a flesh to stone skill. It is used to represent a skill of a monster.
    """

    def run(self): ...


class Regenerate(MonsterSkill):
    """
    This class represents a regenerate skill. It is used to represent a skill of a monster.
    """

    def run(self): ...


class Charm(MonsterSkill):
    """
    This class represents a charm skill. It is used to represent a skill of a monster.
    """

    def run(self): ...


class XTheUnknownSkill(MonsterSkill):
    """
    This class represents a XTheUnknown skill. It is used to represent a skill of a monster.
    """

    def run(self): ...
