from random import randint

from games.even import random_number
from brain_games.engine.game_engine import run_game


def random_operator():
    symbols = ["+", "-", "*"]
    return symbols[randint(0, 2)]


def calculate(a: int, b: int, operator: str) -> int:
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b


initial_line = "What is the result of the expression?"


def generate_round():
    a = random_number()
    b = random_number()
    operator = random_operator()
    question = f"{a} {operator} {b}"
    correct_answer = str(calculate(a, b, operator))
    return question, correct_answer

def start_calc_game():
    return run_game(initial_line, generate_round)