"""Scene module for the engine package."""

from citadel_of_blood.engine import dice
from citadel_of_blood.engine.heroes import Hero, Initiate
from citadel_of_blood.engine.monsters import Monster
from citadel_of_blood.engine.party import Party
from citadel_of_blood.engine.segment import Segment
from citadel_of_blood.engine.weapons import Weapon


class Scene:
    """Scene class for the engine package."""

    def __init__(
        self, party: Party, monsters: Party | list[Monster], segment: Segment
    ) -> None:
        """Initialize the Scene class."""
        self.party: Party = party

        _monsters_party = Party(monsters) if isinstance(monsters, list) else monsters

        self.monsters: Party = _monsters_party
        self.segment: Segment = segment

    def attack(
        self,
        attacker: Hero | Initiate | Monster,
        target: Hero | Initiate | Monster,
        weapon: Weapon,
    ) -> None:
        """Attack the target monster with the attacker monster.

        Args:
            attacker (Hero | Initiate | Monster): The monster attacking.
            target (Hero | Initiate | Monster): The monster being attacked.
            weapon (Weapon): The weapon being used to attack.

        """
        d6 = dice.roll("d6") - 1
        armor = 0
        if hasattr(target, "armor"):
            armor = target.armor.defense if target.armor else 0
        target.wound_points -= (
            d6 + weapon.attack_bonus
            if weapon
            else 0 + attacker.combat_bonus + weapon.damage_table[d6] - armor
        )
