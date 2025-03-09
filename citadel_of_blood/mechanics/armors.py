"""Armor class for the player."""


class Armor:
    """Armor class for the player.

    Attributes
    ----------
        defense: defense of the armor

    """

    def __init__(self, defense):
        """Initialize the Armor class.

        Args:
        ----
            defense: defense of the armor

        """
        self.defense = defense

    def __str__(self):
        """Return the string representation of the armor.

        Returns
        -------
            str: the string representation of the armor

        """
        return f"Armor: (+{self.defense} defense)"

    def __repr__(self):
        """Return the string representation of the armor.

        Returns
        -------
            str: the string representation of the armor

        """
        return self.__str__()
