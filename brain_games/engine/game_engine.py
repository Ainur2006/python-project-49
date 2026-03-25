import prompt
# from prompt_toolkit import prompt

def run_game(initial_line: str, generate_round):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(initial_line)
    score_counter = 0
    while score_counter < 3:
        question, correct_answer = generate_round()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
            score_counter += 1
        else:
            print(
                f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}"
            )
            print(f"Let's try again, {name}!")
            score_counter = 0
    print(f"Congratulations, {name}!")
