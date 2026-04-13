"""Magic items module."""

import abc
from dataclasses import dataclass


@dataclass
class MagicItem(abc.ABC):
    """Magic item class."""

    type: str
    name: str
    description: str

    def __str__(self):
        """Return the name of the magic item."""
        return f"{self.name}"

    @abc.abstractmethod
    def effect(self):
        """Effect of the magic item."""


### Potions ###


class Potion(MagicItem):
    """Potion class."""

    def __init__(self, name: str, description: str) -> None:
        """Initialize the Potion class.

        Args:
            name (str): The name of the potion.
            description (str): The description of the potion.

        """
        super().__init__("potion", name, description)

    def effect(self):
        """Effect of the potion."""
        return f"{self.name} has been used."


class Poison(Potion):
    """Poison class."""

    def __init__(self):
        """Initialize the Poison class."""
        super().__init__("Poison", "A vile liquid that can be used to poison Heroes.")

    def effect(self):
        """Effect of the poison."""
        return f"{self.name} has been used."


class Strength(Potion):
    """Strength class."""

    def __init__(self):
        """Initialize the Strength class."""
        super().__init__(
            "Strength Potion", "A magical potion that increases the drinker's strength."
        )

    def effect(self):
        """Effect of the strength potion."""
        return f"{self.name} has been used."


class CharmPerson(Potion):
    """CharmPerson class."""

    def __init__(self):
        """Initialize the CharmPerson class."""
        super().__init__(
            "Charm Person", "A magical potion that can be used to charm people."
        )

    def effect(self):
        """Effect of the charm person potion."""
        return f"{self.name} has been used."


class CharmMonster(Potion):
    """CharmMonster class."""

    def __init__(self):
        """Initialize the CharmMonster class."""
        super().__init__(
            "Charm Monster", "A magical potion that can be used to charm monsters."
        )

    def effect(self):
        """Effect of the charm monster potion."""
        return f"{self.name} has been used."


class Healing(Potion):
    """Healing class."""

    def __init__(self):
        """Initialize the Healing class."""
        super().__init__("Healing", "A magical potion that can be used to heal wounds.")

    def effect(self):
        """Effect of the healing potion."""
        return f"{self.name} has been used."


### Talismans ###


class Talisman(MagicItem):
    """Talisman class."""

    def __init__(self, name, description):
        """Initialize the Talisman class."""
        super().__init__("talisman", name, description)

    def effect(self):
        """Effect of the talisman."""
        return f"{self.name} has been used."


class Mind(Talisman):
    """Mind class."""

    def __init__(self):
        """Initialize the Mind class."""
        super().__init__(
            "Talisman of Mind",
            "A talisman that can be used to increase the wearer's intelligence.",
        )

    def effect(self):
        """Effect of the mind talisman."""
        return f"{self.name} has been used."


class YellowSun(Talisman):
    """YellowSun class."""

    def __init__(self):
        """Initialize the YellowSun class."""
        super().__init__(
            "Talisman of the Yellow Sun",
            "A talisman that can be used to increase the wearer's wisdom.",
        )

    def effect(self):
        """Effect of the yellow sun talisman."""
        return f"{self.name} has been used."


class BlueSun(Talisman):
    """BlueSun class."""

    def __init__(self):
        """Initialize the BlueSun class."""
        super().__init__(
            "Talisman of the Blue Sun",
            "A talisman that can be used to increase the wearer's charisma.",
        )

    def effect(self):
        """Effect of the blue sun talisman."""
        return f"{self.name} has been used."


class RedSun(Talisman):
    """RedSun class."""

    def __init__(self):
        """Initialize the RedSun class."""
        super().__init__(
            "Talisman of the Red Sun",
            "A talisman that can be used to increase the wearer's strength.",
        )

    def effect(self):
        """Effect of the red sun talisman."""
        return f"{self.name} has been used."


class AllSuns(Talisman):
    """AllSuns class."""

    def __init__(self):
        """Initialize the AllSuns class."""
        super().__init__(
            "Talisman of All Suns",
            "A talisman that can be used to increase all of the wearer's stats.",
        )

    def effect(self):
        """Effect of the all suns talisman."""
        return f"{self.name} has been used."


class Evil(Talisman):
    """Evil class."""

    def __init__(self):
        """Initialize the Evil class."""
        super().__init__(
            "Talisman of Evil", "A talisman that can be used to curse the wearer."
        )

    def effect(self):
        """Effect of the evil talisman."""
        return f"{self.name} has been used."


### Medallions ###


class Medallion(MagicItem):
    """Medallion class."""

    def __init__(self, name, description):
        """Initialize the Medallion class."""
        super().__init__("medallion", name, description)

    def effect(self):
        """Effect of the medallion."""
        return f"{self.name} has been used."


class NeutralizePoisonMedallion(Medallion):
    """NeutralizePoisonMedallion class."""

    def __init__(self):
        """Initialize the NeutralizePoisonMedallion class."""
        super().__init__(
            "Medallion of Neutralize Poison",
            "A medallion that can be used to neutralize poisons.",
        )

    def effect(self):
        """Effect of the neutralize poison medallion."""
        return f"{self.name} has been used."


class PotionAppraisal(Medallion):
    """PotionAppraisal class."""

    def __init__(self):
        """Initialize the PotionAppraisal class."""
        super().__init__(
            "Medallion of Potion Appraisal",
            "A medallion that can be used to appraise potions.",
        )

    def effect(self):
        """Effect of the potion appraisal medallion."""
        return f"{self.name} has been used."


class Oratory(Medallion):
    """Oratory class."""

    def __init__(self):
        """Initialize the Oratory class."""
        super().__init__(
            "Medallion of Oratory",
            "A medallion that can be used to increase the wearer's charisma.",
        )

    def effect(self):
        """Effect of the oratory medallion."""
        return f"{self.name} has been used."


class DexterityMedallion(Medallion):
    """DexterityMedallion class."""

    def __init__(self):
        """Initialize the DexterityMedallion class."""
        super().__init__(
            "Medallion of Dexterity",
            "A medallion that can be used to increase the wearer's dexterity.",
        )

    def effect(self):
        """Effect of the dexterity medallion."""
        return f"{self.name} has been used."


class Strangling(Medallion):
    """Strangling class."""

    def __init__(self):
        """Initialize the Strangling class."""
        super().__init__(
            "Medallion of Strangling",
            "A medallion that can be used to strangle enemies.",
        )

    def effect(self):
        """Effect of the strangling medallion."""
        return f"{self.name} has been used."


### Rings ###
class Ring(MagicItem):
    """Ring class."""

    def __init__(self, name, description):
        """Initialize the Ring class."""
        super().__init__("ring", name, description)

    def effect(self):
        """Effect of the ring."""
        return f"{self.name} has been used."


class Resistance(Ring):
    """Resistance class."""

    def __init__(self, resistance):
        """Initialize the Resistance class."""
        super().__init__(
            f"Ring of Resistance +{resistance}",
            f"A ring that can be used to resist {resistance}.",
        )
        self.resistance = resistance

    def effect(self):
        """Effect of the resistance ring."""
        return f"{self.name} (+{self.resistance}) has been used."


class Sleep(Ring):
    """Sleep class."""

    def __init__(self):
        """Initialize the Sleep class."""
        super().__init__(
            "Ring of Sleep", "A ring that can be used to put enemies to sleep."
        )

    def effect(self):
        """Effect of the sleep ring."""
        return f"{self.name} has been used."


class NeutralizePoisonRing(Ring):
    """NeutralizePoisonRing class."""

    def __init__(self):
        """Initialize the NeutralizePoisonRing class."""
        super().__init__(
            "Ring of Neutralize Poison",
            "A ring that can be used to neutralize poisons.",
        )

    def effect(self):
        """Effect of the neutralize poison ring."""
        return f"{self.name} has been used."


class Heal(Ring):
    """Heal class."""

    def __init__(self):
        """Initialize the Heal class."""
        super().__init__("Ring of Heal", "A ring that can be used to heal wounds.")

    def effect(self):
        """Effect of the heal ring."""
        return f"{self.name} has been used."


class Resurrect(Ring):
    """Resurrect class."""

    def __init__(self):
        """Initialize the Resurrect class."""
        super().__init__(
            "Ring of Resurrect", "A ring that can be used to resurrect the dead."
        )

    def effect(self):
        """Effect of the resurrect ring."""
        return f"{self.name} has been used."
