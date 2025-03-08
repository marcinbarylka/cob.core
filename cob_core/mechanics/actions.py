import abc

from cob_core.mechanics.scene import Scene
from cob_core.mechanics.spells import Spell


class Action(abc.ABC):
    def __init__(self, name: str, code: str, scene: Scene) -> None:
        self.name: str = name
        self.code: str = code
        self.scene: Scene = scene

    @abc.abstractmethod
    def before_action(self) -> None:
        """
        The action to be executed before the action is executed.
        """
        pass

    @abc.abstractmethod
    def after_action(self) -> None:
        """
        The action to be executed after the action is executed.
        """
        pass

    @abc.abstractmethod
    def execute(self) -> None:
        """
        The action to be executed.
        """
        pass

    def __str__(self) -> str:
        return f"{self.name} ({self.code})"


class CastSpell(Action):
    def __init__(self, scene: Scene, spell: Spell) -> None:
        super().__init__(name="cast spell", code="CS", scene=scene)
        self.spell: Spell = spell

    def before_action(self) -> None: ...

    def after_action(self) -> None: ...

    def execute(self) -> None:
        self.spell.cast(self.scene)


class Attack(Action):
    def __init__(self, scene: Scene) -> None:
        super().__init__(name="attack", code="AT", scene=scene)

    def before_action(self) -> None: ...

    def after_action(self) -> None: ...

    def execute(self) -> None:
        self.scene.attack()
