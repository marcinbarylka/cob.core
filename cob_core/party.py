from cob_core.heroes import Hero, Initiate
from cob_core.monsters import Monster


class Party:
    def __init__(self, beings: list[Hero | Initiate | Monster]):
        self.ranks: list[list[Hero | Initiate | Monster | None]] = [
            [None, None, None],
        ]
        self.add_beings(beings)

    def add_beings(self, beings: list[Hero | Initiate | Monster]) -> None:
        """
        Add a being to the party.

        :param beings: a hero, initiate or monster to add
        """
        for rank in self.ranks:
            for position, slot in enumerate(rank):
                if slot is None and beings:
                    rank[position] = beings.pop(0)
        if len(beings) > 0:
            for _ in beings:
                self.add_rank()
                self.add_beings(beings)
        self.remove_empty_ranks()

    def add_being(
        self, being: Hero | Initiate | Monster, position: tuple[int, int], force=False
    ) -> None:
        """
        Add a single being to the party at a specific position.

        :param being: a being to add
        :param position: a position where to add the being (row, column)
        :param force: a flag to force add the being (optional)
        """
        if position[0] > 2:
            raise ValueError("Position X out of range")
        if position[1] > len(self.ranks[0]):
            for _ in range(position[1] - len(self.ranks[0])):
                self.add_rank()

        if self.ranks[position[0]][position[1]] and not force:
            raise ValueError(f"Position {position} already taken")

        self.ranks[position[0]][position[1]] = being

        if force:
            self.remove_empty_ranks()

    def remove_being(
        self, being: Hero | Initiate | Monster, position: tuple[int, int] | None = None
    ) -> Hero | Initiate | Monster | None:
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

    def swap_beings(
        self, being1: Hero | Initiate | Monster, being2: Hero | Initiate | Monster
    ):
        """
        Swap two heroes in the party.

        :param being1: a hero to swap
        :param being2: a hero to swap
        """
        for rank in self.ranks:
            if being1 in rank and being2 in rank:
                rank[rank.index(being1)], rank[rank.index(being2)] = being2, being1
                break

    def find_being(self, name: str) -> Hero | Initiate | Monster | None:
        """
        Find a hero in the party by name.

        :param name: a name of the hero
        """
        for rank in self.ranks:
            for being in rank:
                if being and being.name == name:
                    return being

    def get_being(self, position: tuple[int, int]) -> Hero | Initiate | Monster | None:
        """
        Get a hero from the party.

        :param position: a position of the hero (row, column)
        """
        return self.ranks[position[0]][position[1]]

    def get_being_position(
        self, being: Hero | Initiate | Monster
    ) -> tuple[int, int] | None:
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

    def remove_empty_ranks(self):
        """
        Remove empty ranks from the party.
        """
        self.ranks = [rank for rank in self.ranks if any(being for being in rank)]

    @property
    def beings(self) -> list[Hero | Initiate | Monster]:
        return [being for rank in self.ranks for being in rank if being]

    def __len__(self):
        return len(self.beings)
