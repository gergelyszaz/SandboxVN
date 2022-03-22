from sandbox.character.character import Character

class Action:
    duration: int
    def do(self, character: Character):
        #TODO
        print(character.name + type(self))