"""
Puzzle classes that work with decoupled UI / game logic

implements the Strategy Pattern (puzzle objects combine with any planet)
"""
from text_en import TEXT
from abc import ABC, abstractmethod

credits, engines, copilot, game_end = range(4)


class Puzzle(ABC):
    """Abstract Base Class (ABC) for puzzles"""

    @abstractmethod
    def is_active(self, flags):
        pass

    @abstractmethod
    def get_question(self, flags):
        pass

    @abstractmethod
    def answer(self, flags, answer):
        pass


class BuyEngine(Puzzle):

    def is_active(self, flags):
        return engines not in flags

    def get_question(self, flags):
        return TEXT["HYPERDRIVE_SHOPPING_QUESTION"]

    def answer(self, flags, answer):
        if answer == "yes":
            if credits in flags:
                flags.add(engines)
                return ''
            else:
                return TEXT["HYPERDRIVE_TOO_EXPENSIVE"]
        return ''


class StellarQuiz(Puzzle):

    def is_active(self, flags):
        return credits not in flags
    
    def get_question(self, flags):
        return TEXT["SIRIUS_QUIZ_QUESTION"]

    def answer(self, flags, answer):
        if answer == "2":
            flags.add(credits)
            return TEXT["SIRIUS_QUIZ_CORRECT"]
        else:
            return TEXT["SIRIUS_QUIZ_INCORRECT"]


class HireCopilot(Puzzle):

    def is_active(self, flags):
        return copilot not in flags

    def get_question(self, flags):
        return TEXT["ORION_HIRE_COPILOT_QUESTION"]

    def answer(self, flags, answer):
        if answer == "42":
            flags.add(copilot)
            return TEXT["COPILOT_QUESTION_CORRECT"]
        else:
            return TEXT["COPILOT_QUESTION_INCORRECT"]


class BlackHole(Puzzle):

    def is_active(self, flags):
        return True

    def get_question(self, flags):
        return ''
    
    def answer(self, flags, answer):        
        if answer == "yes":
            flags.add(game_end)
            if engines in flags and copilot in flags:
                return TEXT["BLACK_HOLE_COPILOT_SAVES_YOU"] + TEXT["END_CREDITS"]
            else:
                return TEXT["BLACK_HOLE_CRUNCHED"]
        return ''
