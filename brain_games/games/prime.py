from math import sqrt
from random import randint

from brain_games.engine.game_engine import run_game


def checking_divisors(number: int) -> bool:
    sqrt_number = sqrt(number)
    divisors = 3
    while divisors < sqrt_number:
        if number % divisors == 0:
            return False
        divisors += 1
    return True


def is_prime(number: int) -> str:
    if number % 2 != 0 and checking_divisors(number):
        return "yes"
    return "no"


initial_line = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    number = randint(1, 100)
    question = number
    correct_answer = is_prime(number)
    return question, correct_answer


def start_prime_game():
    return run_game(initial_line, generate_round)