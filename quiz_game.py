def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter Your Answer (A, B, C, or D): ").upper()
        guesses.append(guess)
        question_num += 1

        correct_guesses += check_answer(questions.get(key),guess)

    display_score(correct_guesses,guesses)

# ------------------
def check_answer(answer,guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print('WRONG!')
        return 0
# ------------------
def display_score(correct_guesses,guesses):
    print("------------------")
    print("RESULTS")
    print("------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: ", str(score), "%")
# ------------------
def play_again():

    response = input("Would you like to play again? (yes/no): ").upper()
    if response == "YES":
        return True
    else:
        return False
# ------------------

questions = {
    "What is Mohammed Thamul Kabir's favorite color?: ": "A",
    "What year was Mohammed Thamul Kabir born?: ": "A",
    "What is Mohammed Thamul Kabir's favorite snack?: ": "B",
    "What does Mohammed Thamul Kabir love most in life?: ": "C",
    "What does Mohammed Thamul Kabir hate most in life?: ": "D",
}

options = [["A. Red","B. Blue","C. Violet","D. Black"],
           ["A. 2004","B. 2003","C. 2005","D. 2002"],
           ["A. Chips", "B. Coconut meat", "C. Brownies", "D. Cookies"],
           ["A. Friends","B. Family","C. All of the above","D. Money"],
           ["A. Tranquility","B. Quiet","C. Peace","D. Noise"]]

new_game()

while play_again():
    new_game()

print("Buh-Byeee!")
