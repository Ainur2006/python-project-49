from random import randint

from brain_games.engine.game_engine import run_game


def random_number() -> int:
    return randint(1, 100)


def is_even(number: int):
    if number % 2 == 0:
        return "yes"
    return "no"


initian_line = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    question = random_number()
    correct_answer = is_even(question)
    return question, correct_answer


def main():
    run_game(initian_line, generate_round)


if __name__ == "__main__":
    main()
