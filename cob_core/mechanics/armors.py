"""Armor class for the player."""


class Armor:
    def __init__(self, defense):
        self.defense = defense

    def __str__(self):
        return f"Armor: (+{self.defense} defense)"

    def __repr__(self):
        return self.__str__()
