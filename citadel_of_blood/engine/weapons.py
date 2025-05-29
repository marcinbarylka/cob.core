"""Weapons used in the game."""


class Weapon:
    """Base class for all weapons."""

    def __init__(
        self,
        name: str = "",
        attack_bonus: int = 0,
        damage_table: list[int] = [],
        is_ranged_weapon: bool = False,
    ) -> None:
        """Initialize the weapon.

        Args:
            name (str): name of the weapon
            attack_bonus (int): attack bonus of the weapon
            damage_table (list[int]): damage table of the weapon
            is_ranged_weapon (bool): is the weapon a ranged weapon

        """
        if not name:
            name = self.__class__.__name__

        self.name: str = name
        self.damage_table: list[int] = damage_table
        self.attack_bonus: int = attack_bonus
        self.is_ranged_weapon: bool = is_ranged_weapon

    def get_damage(self, roll: int) -> int:
        """Get damage based on the roll.

        Args:
            roll (int): roll used to determine the index of the damage table.

        Returns:
            int: damage

        """
        if roll >= len(self.damage_table):
            return self.damage_table[-1]
        if roll < 0:
            return self.damage_table[0]
        return self.damage_table[roll]

    def __str__(self) -> str:
        """Return the string representation of the weapon."""
        if self.attack_bonus:
            return f"{self.name} (+{self.attack_bonus})"
        return self.name

    def __repr__(self) -> str:
        """Return the string representation of the weapon."""
        return self.__str__()


class Sword(Weapon):
    """Sword weapon class."""

    def __init__(self):
        """Initialize the sword weapon."""
        super().__init__()
        self.name = "Sword"
        self.damage_table = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5]


class Dagger(Weapon):
    """Dagger weapon class."""

    def __init__(self):
        """Initialize the dagger weapon."""
        super().__init__()
        self.name = "Dagger"
        self.damage_table = [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4]


class ThrowDagger(Weapon):
    """Throwing Dagger weapon class."""

    def __init__(self):
        """Initialize the throwing dagger weapon."""
        super().__init__()
        self.name = "Throwing Dagger"
        self.is_ranged_weapon = True
        self.damage_table = [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4]


class Bow(Weapon):
    """Bow weapon class."""

    def __init__(self):
        """Initialize the bow weapon."""
        super().__init__()
        self.name = "Bow"
        self.is_ranged_weapon = True
        self.damage_table = [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4]


class Hammer(Weapon):
    """Hammer weapon class."""

    def __init__(self):
        """Initialize the hammer weapon."""
        super().__init__()
        self.name = "Hammer"
        self.damage_table = [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]


class Ax(Weapon):
    """Ax weapon class."""

    def __init__(self):
        """Initialize the ax weapon."""
        super().__init__()
        self.name = "Ax"
        self.damage_table = [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]


class Monster(Weapon):
    """Monster weapon class."""

    def __init__(self):
        """Initialize the monster weapon."""
        super().__init__()
        self.name = "Monster"
        self.damage_table = [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 4, 5]
