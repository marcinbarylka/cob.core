"""Magic spells module."""

import abc
import enum
from dataclasses import dataclass


class SpellType(enum.Enum):
    COMBAT = "C"
    NON_COMBAT = "NC"
    NEGOTIATION = "N"
    BRIBERY = "B"
    SPECIAL = "S"


MAGIC_POTENTIAL_TABLE = [
    (0, 0, 0),
    (0, 0, 0),
    (2, 1, 0),
    (0, 1, 2),
    (1, 1, 1),
    (2, 2, 2),
]


@dataclass
class Spell(abc.ABC):
    name: str
    code: str
    cost: int
    type: SpellType

    @staticmethod
    def get_spells_by_type(spell_type):
        """
        Returns a list of instances of Spell subclasses that match the given spell_type.
        :param spell_type: SpellType Enum value indicating the type of spells to retrieve.
        :return: List of instances of subclasses of Spell that match the spell_type.
        """
        spell_classes = []
        for _, obj in globals().items():
            try:
                if issubclass(obj, Spell) and obj is not Spell:
                    if obj().type == spell_type:  # noqa
                        spell_classes.append(obj())  # noqa
            except TypeError:
                continue
        return spell_classes


### combat spells ###
class CombatSpell(Spell):
    def __init__(self, name: str, code: str, cost: int) -> None:
        super().__init__(name, code, cost, SpellType.COMBAT)


class CharmSpell(CombatSpell):
    def __init__(self) -> None:
        super().__init__("Charm", "Cm", 3)


class BlastSpell(CombatSpell):
    def __init__(self) -> None:
        super().__init__("Blast", "Bl", 1)


class ExplosionSpell(CombatSpell):
    def __init__(self) -> None:
        super().__init__("Explosion", "Ex", 1)


class LightningSpell(CombatSpell):
    def __init__(self) -> None:
        super().__init__("Lightning", "Lt", 2)


class SleepSpell(CombatSpell):
    def __init__(self) -> None:
        super().__init__("Sleep", "Sl", 2)


class RedemptionSpell(CombatSpell):
    def __init__(self) -> None:
        super().__init__("Redemption", "Rd", 3)


class MagicShieldSpell(CombatSpell):
    def __init__(self) -> None:
        super().__init__("Magic Shield", "Ms", 2)


class HesitateSpell(CombatSpell):
    def __init__(self) -> None:
        super().__init__("Hesitate", "Hs", 2)


class CeaseFireSpell(CombatSpell):
    def __init__(self) -> None:
        super().__init__("Cease Fire", "CF", 3)


class MentalAttackSpell(CombatSpell):
    def __init__(self) -> None:
        super().__init__("Mental Attack", "MA", 4)


### non combat spells ###
class NonCombatSpell(Spell):
    def __init__(self, name: str, code: str, cost: int) -> None:
        super().__init__(name, code, cost, SpellType.NON_COMBAT)


class LockSpell(NonCombatSpell):
    def __init__(self) -> None:
        super().__init__("Lock", "Lk", 1)


class MageArmorSpell(NonCombatSpell):
    def __init__(self) -> None:
        super().__init__("Mage Armor", "Mr", 1)


class NeutralizePoisonSpell(NonCombatSpell):
    def __init__(self) -> None:
        super().__init__("Neutralize Poison", "NP", 1)


class StoneFleshSpell(NonCombatSpell):
    def __init__(self) -> None:
        super().__init__("Stone Flesh", "SF", 3)


class StrengthSpell(NonCombatSpell):
    def __init__(self) -> None:
        super().__init__("Strength", "St", 1)


class HealSpell(NonCombatSpell):
    def __init__(self) -> None:
        super().__init__("Heal", "He", 1)


class RejuvenateSpell(NonCombatSpell):
    def __init__(self) -> None:
        super().__init__("Rejuvenate", "Rj", 2)


class TeleportSpell(NonCombatSpell):
    def __init__(self) -> None:
        super().__init__("Teleport", "Tl", 3)


class ThiefSpell(NonCombatSpell):
    def __init__(self) -> None:
        super().__init__("Thief", "Tf", 1)


### negotiation spells ###


class NegotiationSpell(Spell):
    def __init__(self, name: str, code: str, cost: int) -> None:
        super().__init__(name, code, cost, SpellType.NEGOTIATION)


class OratorySpell(NegotiationSpell):
    def __init__(self) -> None:
        super().__init__("Oratory", "Or", 1)


class CowSpell(NegotiationSpell):
    def __init__(self) -> None:
        super().__init__("Cow", "Cw", 2)


class DauntSpell(NegotiationSpell):
    def __init__(self) -> None:
        super().__init__("Daunt", "Dn", 3)


### bribery spells ###
class BriberySpell(Spell):
    def __init__(self, name: str, code: str, cost: int) -> None:
        super().__init__(name, code, cost, SpellType.BRIBERY)


class SwaySpell(BriberySpell):
    def __init__(self) -> None:
        super().__init__("Sway", "Sw", 1)


class CajoleSpell(BriberySpell):
    def __init__(self) -> None:
        super().__init__("Cajole", "Cj", 2)


### special spells ###
class SpecialSpell(Spell):
    def __init__(self, name: str, code: str, cost: int) -> None:
        super().__init__(name, code, cost, SpellType.SPECIAL)


class WrathOfGodSpell(SpecialSpell):
    def __init__(self) -> None:
        super().__init__("Wrath of God", "WG", 3)


class ResurrectSpell(SpecialSpell):
    def __init__(self) -> None:
        super().__init__("Resurrect", "Rs", 5)
