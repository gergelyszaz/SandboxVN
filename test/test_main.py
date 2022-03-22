import unittest
from sandbox.character.character import Character
from sandbox.character.habit import Habit
from sandbox.schedule.calendarevent import CalendarEvent
from sandbox.schedule.schedule import Schedule
from sandbox.world.world import World

from sandbox.location.map import Map



class MyTestCase(unittest.TestCase):
    def test_run(self):
        world = World()
        map = Map()

        habit = Habit()
        habit.name = "test"
        habit.schedule = Schedule()
        habit.schedule.events = [
            CalendarEvent

        ]

        character = Character()
        character.map = map
        character.habits = [habit]

        world.map = map
        world.update()


if __name__ == '__main__':
    unittest.main()

