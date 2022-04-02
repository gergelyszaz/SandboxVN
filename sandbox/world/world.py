from typing import List
from sandbox.character.character import Character
from sandbox.location.map import Map


class World:
    current_time: int = 0
    characters: List[Character]
    map: Map

    def __init__(self, world_map: Map, characters: List[Character]) -> None:
        self.characters = characters
        self.map = world_map

    def update(self):
        self.current_time += 1
        for character in self.characters:
            character.update(self.current_time)
