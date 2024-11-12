# -----------------------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D: ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -----------------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("INCORRECT")
        return 0
    


# -----------------------------------------------

def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -----------------------------------------------
def play_again():
    resposne = input ("Do you want to play again? (y/n): ")
    resposne = resposne.upper()
    if resposne == "Y":
        return True
    else:
        return False
# -----------------------------------------------

questions = {
    "What shape is Earth?: ": "B",
    "How many years in a decade?: ":  "B",
    "Which color is sky?: ": "A",
    "What is the name of our Galaxy?: ": "D",
    "How many legs do whales have?:  ": "C"

}

options = [["A. Square", "B. Round", "C. Flat", "D. Hexagon"],
           ["A. 100", "B. 10", "C. 1", "D. 5"],
           ["A. Blue", "B. Red", "C. Yellow", "D. Black"],
           ["A. Andromeda", "B. Black hole", "C. CP151", "D. Milky Way"],
           ["A. 2", "B. 3", "C. Your Mom", "D. 5"]]

new_game()

while play_again():
    new_game()

print("Thanks for playing. Goodbye!")