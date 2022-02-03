from sandbox.action.action import Action
from sandbox.character.character import Character
from sandbox.target.locationselector import LocationSelector


class GotoLocationAction(Action):
    locationSelector: LocationSelector

    def __init__(self, locationSelector: LocationSelector) -> None:
        super().__init__()
        self.locationSelector = locationSelector

    def do(self, character: Character):
        if self.locationSelector.check(character.location):
            return

        

        #TODO
        return super().do(character)