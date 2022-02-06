import string
from typing import List
from sandbox.action.action import Action
from sandbox.character.habit import Habit
from sandbox.location.location import Location
from sandbox.location.map import Map
from sandbox.schedule.schedule import Schedule


class Character:
    name: string
    currentAction: Action
    currentActionStarted: int
    location: Location
    habits: List[Habit]
    map: Map

    def update(self, time):
        if self.currentAction is not None:
            if self.currentActionStarted + self.currentAction.duration > time:
                return
            else:
                self.currentAction = None

        events = self.schedule.getCurrentEvents(time)
        if len(events) == 0:
            return
        
        self.currentAction = events[0].getNextAction(self)
        self.currentActionStarted = time
        self.currentAction.do(self)