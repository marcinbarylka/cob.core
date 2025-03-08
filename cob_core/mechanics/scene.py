from cob_core.mechanics import dice
from cob_core.mechanics.heroes import Hero, Initiate
from cob_core.mechanics.monsters import Monster
from cob_core.mechanics.party import Party
from cob_core.mechanics.segment import Segment
from cob_core.mechanics.weapons import Weapon


class Scene:
    def __init__(self, party: Party, monsters: Party | list[Monster], segment: Segment) -> None:
        self.party: Party = party

        if isinstance(monsters, list):
            _monsters_party = Party(monsters)
        else:
            _monsters_party = monsters

        self.monsters: Party = _monsters_party
        self.segment: Segment = segment

    def attack(
        self,
        attacker: Hero | Initiate | Monster,
        target: Hero | Initiate | Monster,
        weapon: Weapon,
    ) -> None:
        """
        Attack the target monster with the attacker monster.
        """
        d6 = dice.roll("d6") - 1
        armor = 0
        if hasattr(target, "armor"):
            armor = target.armor.defense if target.armor else 0
        target.wound_points -= (
            d6 + weapon.attack_bonus if weapon else 0 + attacker.combat_bonus + weapon.damage_table[d6] - armor
        )
