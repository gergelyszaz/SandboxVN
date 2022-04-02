import string
from typing import List
from sandbox.action.action import Action
from sandbox.character.character import Character
from sandbox.character.habit import Habit
from sandbox.location.location import Location
from sandbox.location.map import Map
from sandbox.schedule.schedule import Schedule


class CharacterImpl(Character):
    name: string = None
    current_action: Action = None
    current_action_started_at_time: int = 0
    location: Location = Location()
    habits: list[Habit] = []
    map: Map = Map()
    schedule: Schedule = Schedule()

    def update(self, time: int) -> None:
        # if an action is in progress do nothing,
        # otherwise clear the current action
        if self.current_action is not None:
            if (
                self.current_action_started_at_time + self.current_action.duration
                > time
            ):
                return
            self.current_action = None

        # find the next top priority event
        events = self.schedule.get_current_events(time)
        if not events or len(events) == 0:
            return

        # get the next action from the top priority event and execute it
        self.current_action = events[0].get_next_action(self)
        self.current_action_started_at_time = time
        self.current_action.do(self)
