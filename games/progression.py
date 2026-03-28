from random import randint, random

from brain_games.engine.game_engine import run_game


def current_element(start: int, index: int, step: int) -> int:
    return start + index * step


def progression_lenght() -> int:
    if random() < 0.5:
        return 10
    return randint(5, 9)


def progression_array() -> list:
    len_arr = progression_lenght()
    prog_arr = []
    start = randint(1, 20)
    step = randint(1, 5)
    index = 0
    while index < len_arr:
        prog_arr.append(current_element(start, index, step))
        index += 1
    return prog_arr


initial_line = "What number is missing in the progression?"


def generate_round():
    array = progression_array()
    pass_number_index = randint(0, len(array) - 1)
    correct_answer = str(array[pass_number_index])
    array[pass_number_index] = ".."
    question = " ".join(map(str, array))
    return question, correct_answer


def start_progression_game():
    return run_game(initial_line, generate_round)