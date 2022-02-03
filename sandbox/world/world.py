from typing import List
from sandbox.character.character import Character
from sandbox.location.map import Map


class World:
    currentTime: int
    characters: List[Character]
    map: Map

    def __init__(self, map: Map, characters: List[Character]) -> None:
        self.characters = characters
        self.map = map
        pass

    def update(self):
        self.currentTime += 1
        for character in self.characters:
            character.update()
