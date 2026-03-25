from brain_games.engine.game_engine import run_game
from brain_games.scripts.brain_even import random_number


def search_gcd(a: int, b: int) -> str:
    while b != 0:
        a, b = b, a % b
    return a


initian_line = "Find the greatest common divisor of given numbers."


def generate_round():
    a = random_number()
    b = random_number()
    question = f"{a} {b}"
    correct_answer = str(search_gcd(a, b))
    return question, correct_answer


def main():
    run_game(initian_line, generate_round)


if __name__ == "__main__":
    main()
