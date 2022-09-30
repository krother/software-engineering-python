"""
Space Travel Game

A simple text adventure written for a refactoring tutorial.
"""

from text_en import TEXT
from puzzles import buy_engine, hire_copilot, stellar_quiz, black_hole
from puzzles import credits, engines, copilot, game_end


def display_inventory(flags): 
    print("-" * 79)
    inventory = "\nYou have: "
    inventory += "plenty of credits, " if credits in flags else ""
    inventory += "a hyperdrive, " if engines in flags else ""
    inventory += "a skilled copilot, " if copilot in flags else ""
    if inventory.endswith(", "):
        print(inventory.strip(", "))


def select_planet(destinations):
    print("\nWhere do you want to travel?")
    for i, d in enumerate(destinations, 1):
        print(f"[{i}] {d}")

    choice = input()
    return PLANETS[destinations[int(choice) - 1]]


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


def travel():
    """main game function"""
    planet = PLANETS["earth"]
    flags = set()

    print(TEXT["OPENING_MESSAGE"])
    planet.visit(flags)

    while game_end not in flags:
        planet = select_planet(planet.connections)
        display_inventory(flags)
        planet.visit(flags)


if __name__ == "__main__":
    travel()
