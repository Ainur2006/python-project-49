from random import randint
from brain_games.engine.game_engine import run_game

def random_number() -> int:
    return randint(1, 100)


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


initian_line = "What is the result of the expression?"


def generate_round():
    a = random_number()
    b = random_number()
    operator = random_operator()
    question = f"{a} {operator} {b}"
    correct_answer = str(calculate(a, b, operator))
    return question, correct_answer


def main():
    run_game(initian_line, generate_round)


if __name__ == "__main__":
    main()
