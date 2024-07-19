"""Magic items module."""

import abc
from dataclasses import dataclass


@dataclass
class MagicItem(abc.ABC):
    type: str
    name: str
    description: str

    def __str__(self):
        return f"{self.name}"

    @abc.abstractmethod
    def effect(self): ...


### Potions ###


class Potion(MagicItem):
    def __init__(self, name, description):
        super().__init__("potion", name, description)

    def effect(self):
        return f"{self.name} has been used."


class Poison(Potion):
    def __init__(self):
        super().__init__("Poison", "A vile liquid that can be used to poison Heroes.")

    def effect(self):
        return f"{self.name} has been used."


class Strength(Potion):
    def __init__(self):
        super().__init__("Strength Potion", "A magical potion that increases the drinker's strength.")

    def effect(self):
        return f"{self.name} has been used."


class CharmPerson(Potion):
    def __init__(self):
        super().__init__("Charm Person", "A magical potion that can be used to charm people.")

    def effect(self):
        return f"{self.name} has been used."


class CharmMonster(Potion):
    def __init__(self):
        super().__init__("Charm Monster", "A magical potion that can be used to charm monsters.")

    def effect(self):
        return f"{self.name} has been used."


class Healing(Potion):
    def __init__(self):
        super().__init__("Healing", "A magical potion that can be used to heal wounds.")

    def effect(self):
        return f"{self.name} has been used."


### Talismans ###


class Talisman(MagicItem):
    def __init__(self, name, description):
        super().__init__("talisman", name, description)

    def effect(self):
        return f"{self.name} has been used."


class Mind(Talisman):
    def __init__(self):
        super().__init__(
            "Talisman of Mind",
            "A talisman that can be used to increase the wearer's intelligence.",
        )

    def effect(self):
        return f"{self.name} has been used."


class YellowSun(Talisman):
    def __init__(self):
        super().__init__(
            "Talisman of the Yellow Sun",
            "A talisman that can be used to increase the wearer's wisdom.",
        )

    def effect(self):
        return f"{self.name} has been used."


class BlueSun(Talisman):
    def __init__(self):
        super().__init__(
            "Talisman of the Blue Sun",
            "A talisman that can be used to increase the wearer's charisma.",
        )

    def effect(self):
        return f"{self.name} has been used."


class RedSun(Talisman):
    def __init__(self):
        super().__init__(
            "Talisman of the Red Sun",
            "A talisman that can be used to increase the wearer's strength.",
        )

    def effect(self):
        return f"{self.name} has been used."


class AllSuns(Talisman):
    def __init__(self):
        super().__init__(
            "Talisman of All Suns",
            "A talisman that can be used to increase all of the wearer's stats.",
        )

    def effect(self):
        return f"{self.name} has been used."


class Evil(Talisman):
    def __init__(self):
        super().__init__("Talisman of Evil", "A talisman that can be used to curse the wearer.")

    def effect(self):
        return f"{self.name} has been used."


### Medallions ###


class Medallion(MagicItem):
    def __init__(self, name, description):
        super().__init__("medallion", name, description)

    def effect(self):
        return f"{self.name} has been used."


class NeutralizePoisonMedallion(Medallion):
    def __init__(self):
        super().__init__(
            "Medallion of Neutralize Poison",
            "A medallion that can be used to neutralize poisons.",
        )

    def effect(self):
        return f"{self.name} has been used."


class PotionAppraisal(Medallion):
    def __init__(self):
        super().__init__(
            "Medallion of Potion Appraisal",
            "A medallion that can be used to appraise potions.",
        )

    def effect(self):
        return f"{self.name} has been used."


class Oratory(Medallion):
    def __init__(self):
        super().__init__(
            "Medallion of Oratory",
            "A medallion that can be used to increase the wearer's charisma.",
        )

    def effect(self):
        return f"{self.name} has been used."


class DexterityMedallion(Medallion):
    def __init__(self):
        super().__init__(
            "Medallion of Dexterity",
            "A medallion that can be used to increase the wearer's dexterity.",
        )

    def effect(self):
        return f"{self.name} has been used."


class Strangling(Medallion):
    def __init__(self):
        super().__init__(
            "Medallion of Strangling",
            "A medallion that can be used to strangle enemies.",
        )

    def effect(self):
        return f"{self.name} has been used."


### Rings ###
class Ring(MagicItem):
    def __init__(self, name, description):
        super().__init__("ring", name, description)

    def effect(self):
        return f"{self.name} has been used."


class Resistance(Ring):
    def __init__(self, resistance):
        super().__init__(
            f"Ring of Resistance +{resistance}",
            f"A ring that can be used to resist {resistance}.",
        )
        self.resistance = resistance

    def effect(self):
        return f"{self.name} (+{self.resistance} has been used."


class Sleep(Ring):
    def __init__(self):
        super().__init__("Ring of Sleep", "A ring that can be used to put enemies to sleep.")

    def effect(self):
        return f"{self.name} has been used."


class NeutralizePoisonRing(Ring):
    def __init__(self):
        super().__init__(
            "Ring of Neutralize Poison",
            "A ring that can be used to neutralize poisons.",
        )

    def effect(self):
        return f"{self.name} has been used."


class Heal(Ring):
    def __init__(self):
        super().__init__("Ring of Heal", "A ring that can be used to heal wounds.")

    def effect(self):
        return f"{self.name} has been used."


class Resurrect(Ring):
    def __init__(self):
        super().__init__("Ring of Resurrect", "A ring that can be used to resurrect the dead.")

    def effect(self):
        return f"{self.name} has been used."
