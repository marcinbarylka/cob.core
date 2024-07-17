"""Weapons used in the game."""


class Weapon:
    """Base class for all weapons."""

    def __init__(
        self,
        name: str = "",
        additional_damage: int = 0,
        damage_table: list[int] = [],
        is_ranged_weapon: bool = False,
    ) -> None:
        if not name:
            name = self.__class__.__name__

        self.name: str = name
        self.damage_table: list[int] = damage_table
        self.additional_damage: int = additional_damage
        self.is_ranged_weapon: bool = is_ranged_weapon

    def get_damage(self, roll: int) -> int:
        if roll >= len(self.damage_table):
            return self.damage_table[-1]
        if roll < 0:
            return self.damage_table[0]
        return self.damage_table[roll]

    def __str__(self) -> str:
        if self.additional_damage:
            return f"{self.name} (+{self.additional_damage})"
        return self.name

    def __repr__(self) -> str:
        return self.__str__()


class Sword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Sword"
        self.damage_table = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5]


class Dagger(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Dagger"
        self.damage_table = [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4]


class ThrowDagger(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Throwing Dagger"
        self.is_ranged_weapon = True
        self.damage_table = [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4]


class Bow(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Bow"
        self.is_ranged_weapon = True
        self.damage_table = [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4]


class Hammer(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Hammer"
        self.damage_table = [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]


class Ax(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Ax"
        self.damage_table = [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]


class Monster(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Monster"
        self.damage_table = [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 4, 5]
