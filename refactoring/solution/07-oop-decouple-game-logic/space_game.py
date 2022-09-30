"""
Space Travel Game

A simple text adventure written for a refactoring tutorial.
"""

from text_en import TEXT
from puzzles import StellarQuiz, BuyEngine, HireCopilot, BlackHole
from puzzles import credits, engines, copilot, game_end


class Planet:

    def __init__(self, name, connections, puzzle=None):
        self.name = name
        self.description = TEXT[name.upper() + "_DESCRIPTION"]
        self.connections = connections
        self.puzzle = puzzle

    def has_active_puzzle(self, flags):
        return self.puzzle and self.puzzle.is_active(flags)

    def get_puzzle_text(self, flags):
        return self.puzzle.get_question(flags)

    def answer_puzzle(self, flags, action):
        return self.puzzle.answer(flags, action)
        

PLANETS = {p.name: p for p in [
    Planet('earth', ["centauri", "sirius"]),
    Planet('centauri', ["earth", "orion"], BuyEngine()),
    Planet('sirius', ["orion", "earth", "black_hole"], StellarQuiz()),
    Planet('orion', ["centauri", "sirius"], HireCopilot()),
    Planet('black_hole', ["sirius"], BlackHole())
]}


class SpaceGame:

    def __init__(self):
        self.flags = set()
        self.planet = PLANETS["earth"]
        self.state = 'start'

    @property
    def running(self):
        return game_end not in self.flags

    def display_inventory(self):
        """Returns a string description of the inventory"""
        inventory = "\nYou have: "
        inventory += "plenty of credits, " if credits in self.flags else ""
        inventory += "a hyperdrive, " if engines in self.flags else ""
        inventory += "a skilled copilot, " if copilot in self.flags else ""
        if inventory.endswith(", "):
            return inventory.strip(", ")
        return ''

    def visit_planet(self):
        self.planet.visit(self.flags)
    
    @property
    def choices(self):
        if self.state == 'move':
            return self.planet.connections
        elif self.state == 'puzzle':
            return None

    def get_situation_text(self):
        result = ''
        if self.state == 'start':
            result = TEXT["OPENING_MESSAGE"]
            self.state = 'move'
        if self.state == 'move':
            result += self.display_inventory()
            result += "\n\nWhere do you want to travel?"
        if self.state == 'puzzle':
            result = self.planet.get_puzzle_text(self.flags)
        return result

    def take_action(self, action):
        """manages state transitions"""
        if self.state == 'move':
            self.planet = PLANETS[action]
            if self.planet.has_active_puzzle(self.flags):
                self.state = 'puzzle'
            return self.planet.description
            
        if self.state == 'puzzle':
            self.state = 'move'
            return(self.planet.answer_puzzle(self.flags, action))


#
# User Interface
#
# the only part of the program that knows about print() and input()
#
def display_options(choices):
    """Returns a generic selection menu"""
    if choices:
        for i, d in enumerate(choices, 1):
            print(f"[{i}] {d}")

def select_option(choices):
    """Returns keyboard input"""
    action = input()
    if choices:
        return choices[int(action) - 1]
    return action
    

def travel():
    """main game function"""
    game = SpaceGame()    
    while game.running:
        print('-' * 79)
        print(game.get_situation_text())
        display_options(game.choices)
        action = select_option(game.choices)
        print(game.take_action(action))


if __name__ == "__main__":
    travel()
