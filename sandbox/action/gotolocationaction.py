from sandbox.action.action import Action
from sandbox.character.character import Character
from sandbox.target.locationselector import LocationSelector


class GotoLocationAction(Action):
    location_selector: LocationSelector

    def __init__(self, location_selector: LocationSelector) -> None:
        super().__init__()
        self.location_selector = location_selector

    def do(self, character: Character) -> None:
        if self.location_selector.check(character.location):
            return

        super().do(character)
