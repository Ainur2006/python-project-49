import prompt
import random


def random_number() -> int:
    return random.randint(1, 100)


def is_even(number: int) -> bool:
    return number % 2 == 0


def generate_round() -> bool:
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    score_counter = 0
    while score_counter < 3:
        number = random_number()
        accuracy = is_even(number)
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == "yes" and accuracy == True:
            print("Correct!")
            score_counter += 1
        elif user_answer == "yes" and accuracy == False:
            print(
                f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!"
            )
            score_counter = 0
        elif user_answer == "no" and accuracy == False:
            print("Correct!")
            score_counter += 1
        elif user_answer == "no" and accuracy == True:
            print(
                f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!"
            )
            score_counter = 0
        else:
            print("Try again. Incorrect response format.")
            score_counter = 0
    print(f"Congratulations, {name}!")


def main():
    generate_round()


if __name__ == "__main__":
    main()
