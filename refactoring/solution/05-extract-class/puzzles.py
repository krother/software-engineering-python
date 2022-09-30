
from text_en import TEXT


credits, engines, copilot, game_end = range(4)


def buy_engine(flags):
    if engines not in flags:
        print(TEXT["HYPERDRIVE_SHOPPING_QUESTION"])
        if input() == "yes":
            if credits in flags:
                flags.add(engines)
            else:
                print(TEXT["HYPERDRIVE_TOO_EXPENSIVE"])


def stellar_quiz(flags):
    if credits not in flags:
        print(TEXT["SIRIUS_QUIZ_QUESTION"])
        answer = input()
        if answer == "2":
            print(TEXT["SIRIUS_QUIZ_CORRECT"])
            flags.add(credits)
        else:
            print(TEXT["SIRIUS_QUIZ_INCORRECT"])


def hire_copilot(flags):
    if copilot not in flags:
        print(TEXT["ORION_HIRE_COPILOT_QUESTION"])
        if input() == "42":
            print(TEXT["COPILOT_QUESTION_CORRECT"])
            flags.add(copilot)
        else:
            print(TEXT["COPILOT_QUESTION_INCORRECT"])


def black_hole(flags):
    if input() == "yes":
        if engines in flags and copilot in flags:
            print(TEXT["BLACK_HOLE_COPILOT_SAVES_YOU"])
            print(TEXT["END_CREDITS"])
        else:
            print(TEXT["BLACK_HOLE_CRUNCHED"])
        flags.add(game_end)
