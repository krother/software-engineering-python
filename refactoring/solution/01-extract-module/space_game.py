"""
Space Travel Game

A simple text adventure written for a refactoring tutorial.
"""

from text_en import TEXT


def travel():

    print(TEXT["OPENING_MESSAGE"])

    planet = "earth"
    engines = False
    copilot = False
    credits = False
    game_end = False

    while not game_end:

        # display inventory
        print("-" * 79)
        inventory = "\nYou have: "
        inventory += "plenty of credits, " if credits else ""
        inventory += "a hyperdrive, " if engines else ""
        inventory += "a skilled copilot, " if copilot else ""
        if inventory.endswith(", "):
            print(inventory.strip(", "))

        #
        # interaction with planets
        #
        if planet == "earth":
            destinations = ["centauri", "sirius"]
            print(TEXT["EARTH_DESCRIPTION"])

        if planet == "centauri":
            print(TEXT["CENTAURI_DESCRIPTION"])
            destinations = ["earth", "orion"]

            if not engines:
                print(TEXT["HYPERDRIVE_SHOPPING_QUESTION"])
                if input() == "yes":
                    if credits:
                        engines = True
                    else:
                        print(TEXT["HYPERDRIVE_TOO_EXPENSIVE"])

        if planet == "sirius":
            print(TEXT["SIRIUS_DESCRIPTION"])
            destinations = ["orion", "earth", "black_hole"]

            if not credits:
                print(TEXT["SIRIUS_QUIZ_QUESTION"])
                answer = input()
                if answer == "2":
                    print(TEXT["SIRIUS_QUIZ_CORRECT"])
                    credits = True
                else:
                    print(TEXT["SIRIUS_QUIZ_INCORRECT"])

        if planet == "orion":
            destinations = ["centauri", "sirius"]
            if not copilot:
                print(TEXT["ORION_DESCRIPTION"])
                print(TEXT["ORION_HIRE_COPILOT_QUESTION"])
                if input() == "42":
                    print(TEXT["COPILOT_QUESTION_CORRECT"])
                    copilot = True
                else:
                    print(TEXT["COPILOT_QUESTION_INCORRECT"])
            else:
                print(TEXT["ORION_DESCRIPTION"])

        if planet == "black_hole":
            print(TEXT["BLACK_HOLE_DESCRIPTION"])
            destinations = ["sirius"]
            if input() == "yes":
                if engines and copilot:
                    print(TEXT["BLACK_HOLE_COPILOT_SAVES_YOU"])
                    game_end = True
                else:
                    print(TEXT["BLACK_HOLE_CRUNCHED"])
                    return

        if not game_end:
            # select next planet
            print("\nWhere do you want to travel?")
            position = 1
            for d in destinations:
                print(f"[{position}] {d}")
                position += 1

            choice = input()
            planet = destinations[int(choice) - 1]

    print(TEXT["END_CREDITS"])


if __name__ == "__main__":
    travel()
