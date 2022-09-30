"""
Space Travel Game

A simple text adventure written for a refactoring tutorial.
"""

from text_en import TEXT
from puzzles import buy_engine, hire_copilot, stellar_quiz, black_hole
from puzzles import credits, engines, copilot, game_end



class Planet:

    def __init__(self, name, connections, puzzle=None):
        self.name = name
        self.description = TEXT[name.upper() + "_DESCRIPTION"]
        self.connections = connections
        self.puzzle = puzzle

    def visit(self, flags):
        print(self.description)
        if self.puzzle:
            self.puzzle(flags)
        

PLANETS = {p.name: p for p in [
    Planet('earth', ["centauri", "sirius"]),
    Planet('centauri', ["earth", "orion"], buy_engine),
    Planet('sirius', ["orion", "earth", "black_hole"], stellar_quiz),
    Planet('orion', ["centauri", "sirius"], hire_copilot),
    Planet('black_hole', ["sirius"], black_hole)
]}


class SpaceGame:

    def __init__(self):
        self.flags = set()
        self.planet = PLANETS["earth"]

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
            inventory = inventory.strip(", ")
        return inventory

    def visit_planet(self):
        self.planet.visit(self.flags)

    def display_destinations(self):
        """Returns the planet selection menu"""
        result = "\nWhere do you want to travel?"
        for i, d in enumerate(self.planet.connections, 1):
            result += f"[{i}] {d}"
        return result
        
    def select_planet(self):
        choice = input()
        self.planet = PLANETS[self.planet.connections[int(choice) - 1]]


def travel():
    """main game function"""
    game = SpaceGame()

    print(TEXT["OPENING_MESSAGE"])
    game.visit_planet()

    while game.running:
        print(game.display_destinations())
        game.select_planet()
        print('-' * 79)
        print(game.display_inventory())
        game.visit_planet()


if __name__ == "__main__":
    travel()
