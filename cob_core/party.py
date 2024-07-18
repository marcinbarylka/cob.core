from cob_core.heroes import Initiate, Hero
from cob_core.monsters import Monster


class Party:
    def __init__(self, beings: list[Hero | Initiate | Monster]):
        self.ranks: list[list[Hero | Initiate | Monster | None]] = [
            [None, None, None],
            [None, None, None],
        ]
        for being in beings:
            self.add_being(being)

    def add_being(self, being: Hero | Initiate | Monster, position: tuple[int, int] | None = None):
        """
        Add a hero to the party.

        :param being: a hero to add
        :param position: a position where to add the hero (row, column) (optional)
        """
        if position:
            self.ranks[position[0]][position[1]] = being
            return

        for rank in self.ranks:
            if None in rank:
                rank[rank.index(None)] = being
                break

    def remove_being(
        self, being: Hero | Initiate|Monster, position: tuple[int, int] | None = None
    ):
        """
        Remove a hero from the party.

        :param being: a hero to remove
        :param position: a position where to remove the hero (row, column) (optional)

        """
        if position:
            self.ranks[position[0]][position[1]] = None
            return being

        for rank in self.ranks:
            if being in rank:
                rank[rank.index(being)] = None
                break

    def swap_beings(self, being1: Hero | Initiate | Monster, being2: Hero | Initiate | Monster):
        """
        Swap two heroes in the party.

        :param being1: a hero to swap
        :param being2: a hero to swap
        """
        for rank in self.ranks:
            if being1 in rank and being2 in rank:
                rank[rank.index(being1)], rank[rank.index(being2)] = being2, being1
                break

    def get_being(self, position: tuple[int, int]) -> Hero | Initiate | Monster | None:
        """
        Get a hero from the party.

        :param position: a position of the hero (row, column)
        """
        return self.ranks[position[0]][position[1]]

    def get_being_position(self, being: Hero | Initiate | Monster) -> tuple[int, int] | None:
        """
        Get a position of the hero in the party.

        :param being: a hero to get a position
        """
        for i, rank in enumerate(self.ranks):
            if being in rank:
                return i, rank.index(being)

    def add_rank(self):
        """
        Add a rank to the party.
        """
        self.ranks.append([None, None, None])

    @property
    def beings(self) -> list[Hero | Initiate | Monster]:
        return [being for rank in self.ranks for being in rank if being]
