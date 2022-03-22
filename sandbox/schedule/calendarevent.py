import string

from sandbox.action.action import Action
from sandbox.action.gotolocationaction import GotoLocationAction
from sandbox.character.character import Character
from sandbox.schedule.timeframe import TimeFrame
from sandbox.target.locationselector import LocationSelector


class CalendarEvent:
    name: string
    action: Action
    locationSelector: LocationSelector
    timeframe: TimeFrame

    def __init__(self, action: Action) -> None:
        self.actions = action

    def getNextAction(self, character: Character) -> Action:
        if self.locationSelector.check(character.location):
            return self.action

        return GotoLocationAction(locationSelector=self.locationSelector)