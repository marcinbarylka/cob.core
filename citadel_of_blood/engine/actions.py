"""Actions module. It contains the classes to represent the actions of a character."""

import abc

from citadel_of_blood.engine.scene import Scene
from citadel_of_blood.engine.spells import Spell


class Action(abc.ABC):
    """Action base class. It is used to represent an action of a character."""

    def __init__(self, name: str, code: str, scene: Scene) -> None:
        """Initialize the Action class.

        Args:
         name: name of the action
         code: code of the action
         scene: scene of the action

        """
        self.name: str = name
        self.code: str = code
        self.scene: Scene = scene

    @abc.abstractmethod
    def before_action(self) -> None:
        """Execute the method before the action is executed. For example, to check if the action can be executed or if
        the character has enough resources, etc.
        """

    @abc.abstractmethod
    def after_action(self) -> None:
        """Execute the method after the action is executed. For example, to update character state,
        apply post-action effects, or clean up resources.
        """

    @abc.abstractmethod
    def execute(self) -> None:
        """Execute the action. This is the main method that implements the specific behavior of the action."""

    def __str__(self) -> str:
        """Return the string representation of the action.

        Returns:
            str: the string representation of the action

        """
        return f"{self.name} ({self.code})"


class CastSpell(Action):
    """CastSpell class. It is used to represent a spell casting action of a character."""

    def __init__(self, scene: Scene, spell: Spell) -> None:
        """Initialize the CastSpell class.

        Args:
            scene: scene in which the spell is cast
            spell: spell to cast

        """
        super().__init__(name="cast spell", code="CS", scene=scene)
        self.spell: Spell = spell

    def before_action(self) -> None:
        """Execute the method before the action is executed."""

    def after_action(self) -> None:
        """Execute the method after the action is executed."""

    def execute(self) -> None:
        """Execute the spell casting action by calling the cast method of the spell object."""
        self.spell.cast(self.scene)


class Attack(Action):
    """Attack class. It is used to represent an attack action of a character."""

    def __init__(self, scene: Scene) -> None:
        """Initialize the Attack class.

        Args:
            scene: scene in which the attack is executed

        """
        super().__init__(name="attack", code="AT", scene=scene)

    def before_action(self) -> None:
        """Execute the method before the action is executed."""

    def after_action(self) -> None:
        """Execute the method after the action is executed."""

    def execute(self) -> None:
        """Execute the attack action by calling the attack method of the scene object."""
        self.scene.attack()
