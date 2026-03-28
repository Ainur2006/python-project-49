from brain_games.engine.game_engine import run_game
from games.even import random_number


def search_gcd(a: int, b: int) -> str:
    while b != 0:
        a, b = b, a % b
    return a


initial_line = "Find the greatest common divisor of given numbers."


def generate_round():
    a = random_number()
    b = random_number()
    question = f"{a} {b}"
    correct_answer = str(search_gcd(a, b))
    return question, correct_answer


def start_gcd_game():
    return run_game(initial_line, generate_round)