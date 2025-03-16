"""Magic spells module."""

import abc
import enum
from dataclasses import dataclass


class SpellType(enum.Enum):
    """Spell type enum."""

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
    """Spell class."""

    name: str
    code: str
    cost: int
    type: SpellType

    @staticmethod
    def get_spells_by_type(spell_type):
        """Return a list of instances of Spell subclasses that match the given spell_type.

        Args:
            spell_type: SpellType

        Returns:
            list: list of Spell instances

        """
        spell_classes = []
        for _, obj in globals().items():
            try:
                if issubclass(obj, Spell) and obj is not Spell and obj().type == spell_type:
                    spell_classes.append(obj())
            except TypeError:
                continue
        return spell_classes


### combat spells ###
class CombatSpell(Spell):
    """Combat spell class."""

    def __init__(self, name: str, code: str, cost: int) -> None:
        """Initialize the combat spell."""
        super().__init__(name, code, cost, SpellType.COMBAT)


class CharmSpell(CombatSpell):
    """Charm spell class."""

    def __init__(self) -> None:
        """Initialize the charm spell."""
        super().__init__("Charm", "Cm", 3)


class BlastSpell(CombatSpell):
    """Blast spell class."""

    def __init__(self) -> None:
        """Initialize the blast spell."""
        super().__init__("Blast", "Bl", 1)


class ExplosionSpell(CombatSpell):
    """Explosion spell class."""

    def __init__(self) -> None:
        """Initialize the explosion spell."""
        super().__init__("Explosion", "Ex", 1)


class LightningSpell(CombatSpell):
    """Lightning spell class."""

    def __init__(self) -> None:
        """Initialize the lightning spell."""
        super().__init__("Lightning", "Lt", 2)


class SleepSpell(CombatSpell):
    """Sleep spell class."""

    def __init__(self) -> None:
        """Initialize the sleep spell."""
        super().__init__("Sleep", "Sl", 2)


class RedemptionSpell(CombatSpell):
    """Redemption spell class."""

    def __init__(self) -> None:
        """Initialize the redemption spell."""
        super().__init__("Redemption", "Rd", 3)


class MagicShieldSpell(CombatSpell):
    """Magic shield spell class."""

    def __init__(self) -> None:
        """Initialize the magic shield spell."""
        super().__init__("Magic Shield", "Ms", 2)


class HesitateSpell(CombatSpell):
    """Hesitate spell class."""

    def __init__(self) -> None:
        """Initialize the hesitate spell."""
        super().__init__("Hesitate", "Hs", 2)


class CeaseFireSpell(CombatSpell):
    """Cease fire spell class."""

    def __init__(self) -> None:
        """Initialize the cease fire spell."""
        super().__init__("Cease Fire", "CF", 3)


class MentalAttackSpell(CombatSpell):
    """Mental attack spell class."""

    def __init__(self) -> None:
        """Initialize the mental attack spell."""
        super().__init__("Mental Attack", "MA", 4)


### non combat spells ###
class NonCombatSpell(Spell):
    """Non combat spell class."""

    def __init__(self, name: str, code: str, cost: int) -> None:
        """Initialize the non combat spell."""
        super().__init__(name, code, cost, SpellType.NON_COMBAT)


class LockSpell(NonCombatSpell):
    """Lock spell class."""

    def __init__(self) -> None:
        """Initialize the lock spell."""
        super().__init__("Lock", "Lk", 1)


class MageArmorSpell(NonCombatSpell):
    """Mage armor spell class."""

    def __init__(self) -> None:
        """Initialize the mage armor spell."""
        super().__init__("Mage Armor", "Mr", 1)


class NeutralizePoisonSpell(NonCombatSpell):
    """Neutralize poison spell class."""

    def __init__(self) -> None:
        """Initialize the neutralize poison spell."""
        super().__init__("Neutralize Poison", "NP", 1)


class StoneFleshSpell(NonCombatSpell):
    """Stone flesh spell class."""

    def __init__(self) -> None:
        """Initialize the stone flesh spell."""
        super().__init__("Stone Flesh", "SF", 3)


class StrengthSpell(NonCombatSpell):
    """Strength spell class."""

    def __init__(self) -> None:
        """Initialize the strength spell."""
        super().__init__("Strength", "St", 1)


class HealSpell(NonCombatSpell):
    """Heal spell class."""

    def __init__(self) -> None:
        """Initialize the heal spell."""
        super().__init__("Heal", "He", 1)


class RejuvenateSpell(NonCombatSpell):
    """Rejuvenate spell class."""

    def __init__(self) -> None:
        """Initialize the rejuvenate spell."""
        super().__init__("Rejuvenate", "Rj", 2)


class TeleportSpell(NonCombatSpell):
    """Teleport spell class."""

    def __init__(self) -> None:
        """Initialize the teleport spell."""
        super().__init__("Teleport", "Tl", 3)


class ThiefSpell(NonCombatSpell):
    """Thief spell class."""

    def __init__(self) -> None:
        """Initialize the thief spell."""
        super().__init__("Thief", "Tf", 1)


### negotiation spells ###


class NegotiationSpell(Spell):
    """Negotiation spell class."""

    def __init__(self, name: str, code: str, cost: int) -> None:
        """Initialize the negotiation spell."""
        super().__init__(name, code, cost, SpellType.NEGOTIATION)


class OratorySpell(NegotiationSpell):
    """Oratory spell class."""

    def __init__(self) -> None:
        """Initialize the oratory spell."""
        super().__init__("Oratory", "Or", 1)


class CowSpell(NegotiationSpell):
    """Cow spell class."""

    def __init__(self) -> None:
        """Initialize the cow spell."""
        super().__init__("Cow", "Cw", 2)


class DauntSpell(NegotiationSpell):
    """Daunt spell class."""

    def __init__(self) -> None:
        """Initialize the daunt spell."""
        super().__init__("Daunt", "Dn", 3)


### bribery spells ###
class BriberySpell(Spell):
    """Bribery spell class."""

    def __init__(self, name: str, code: str, cost: int) -> None:
        """Initialize the bribery spell."""
        super().__init__(name, code, cost, SpellType.BRIBERY)


class SwaySpell(BriberySpell):
    """Sway spell class."""

    def __init__(self) -> None:
        """Initialize the sway spell."""
        super().__init__("Sway", "Sw", 1)


class CajoleSpell(BriberySpell):
    """Cajole spell class."""

    def __init__(self) -> None:
        """Initialize the cajole spell."""
        super().__init__("Cajole", "Cj", 2)


### special spells ###
class SpecialSpell(Spell):
    """Special spell class."""

    def __init__(self, name: str, code: str, cost: int) -> None:
        """Initialize the special spell."""
        super().__init__(name, code, cost, SpellType.SPECIAL)


class WrathOfGodSpell(SpecialSpell):
    """Wrath of God spell class."""

    def __init__(self) -> None:
        """Initialize the wrath of god spell."""
        super().__init__("Wrath of God", "WG", 3)


class ResurrectSpell(SpecialSpell):
    """Resurrect spell class."""

    def __init__(self) -> None:
        """Initialize the resurrect spell."""
        super().__init__("Resurrect", "Rs", 5)
