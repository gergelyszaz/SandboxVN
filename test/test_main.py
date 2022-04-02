import unittest
from sandbox.character.character import Character
from sandbox.character.character_impl import CharacterImpl
from sandbox.character.habit import Habit
from sandbox.schedule.calendarevent import CalendarEvent
from sandbox.schedule.schedule import Schedule
from sandbox.world.world import World

from sandbox.location.map import Map


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_run():

        world_map = Map()

        habit = Habit()
        habit.name = "test"
        habit.schedule = Schedule()
        habit.schedule.events = [
            CalendarEvent
        ]

        character: Character = CharacterImpl()
        character.map = world_map
        character.habits = [habit]

        characters = [character]

        world = World(world_map, characters)
        world.map = world_map
        world.update()


if __name__ == '__main__':
    unittest.main()
