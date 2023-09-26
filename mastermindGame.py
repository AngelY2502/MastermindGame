# This is A Master Mind Computer Game for CSC1024 Programming Principles.
# by Yap Yi Rou (20057055)

# Main lobby for the game.
# This is just to access the info and play functions, the exit will be at another place.
def main():
    global time
    import time
    intro()
    ingame()

# This is the guideline to brief the basics of the mastermind game to the user, I will try to make it as simple as possible.
# For this function, time.sleep is used to avoid large amounts of info to appear suddenly.
def guideline():
    print("Master mind is a code-breaking game.")
    time.sleep(1)
    print("Computer will be the code maker to generate a combination of 4 colours’ sequence, keep on mind that there could be the chance for repetition of thesame colour.")
    time.sleep(2.5)
    print("Then, the code breaker,")
    time.sleep(0.5)
    print("You")
    time.sleep(0.5)
    print("Will guess the colours’ patterns whether it is same with the set of colours defined by the code maker.")
    time.sleep(1)
    print("After each attempt of guessing, the correct colour in correct place and the correct colour in wrong place will be calculate to display. This will be your clue to guess the correct patterns of colours.")
    time.sleep(2.5)
    print("For my A.Y Master Mind, you will have 12 trials to guess the combination which has 8 possible of different colours, unless you will lose the game.")
    time.sleep(1.5)
    print("There are red, pink, orange yellow, green, blue, violet, and white colours in the selection colours. Only take the first capital letter of it for guessing, ensure there are spaces between each colour.")
    time.sleep(2)
    while True:
        try:
            print("Only {Y/N} or {y/n] are accepeted.")
            explaination = str(input("Do you need further explanation?{Y/N}: "))
            if explaination.upper() == 'Y':
                print("Let gives an example, first the computer will generates a sequence [ 'R', 'B', 'R', 'W' ] randomly and you would not knowing it.")
                time.sleep(1.5)
                print("Then you type ['B', 'W', 'R', 'G’] for guessing.")
                time.sleep(1)
                print("Now the computer will checking your attempted answer and display: Correct colour in correct place: 1; Correct colour in wrong place: 2")
                time.sleep(2.5)
                print("It is because the Blue and White are include in the guessing but the sequences are different; while there is a 'Red' in the same place.")
                time.sleep(2)
                print("Then you have to figure out the next possible sequence of the colours.")
                time.sleep(2)
                print("Hence, now you might have some ideas of the game. Let’s just start the game now!")
                time.sleep(1.5)
                print("Good luck!")
                break
            if explaination.upper() == 'N':
                print("Remember enter the guessing in the certain format.")
                time.sleep(1)
                print("Good luck!")
                time.sleep(1)
                break
        except:
            continue

# This is the intro function where user choose to skip or follow the guideline function.
# For user input, the try and except blocks within the while loops are used to ensure there are only valid input available.
def intro():
    print("Welcome to A.Y Master Mind game!")
    time.sleep(1)
    while True:
        try:
            print("Only {Y/N} or {y/n] are accepeted.")
            skip = str(input("Do you want to skip the tutorial session?Yes/ No {Y/N}: "))
            if skip.upper() == 'Y':
                print("Good luck!")
                break
            if skip.upper() == 'N':
                print("Let's start the tutorial session!")
                time.sleep(1)
                guideline()
                break
        except:
            continue

# Well, now we can start the game after the briefing.
# So this function is just for the computer to generate random patterns of colours.
# Global is used to make the local variable, so that the correct answer can be accessed even outside this function.
def ingame():
    import random
    global coranswer
    coranswer = []
    colours = ['Red', 'Pink', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'White']
    for i in range(1, 5):
        code = random.choice(colours)
        slicedcode = code[0:1]
        coranswer.append(slicedcode)
    print(coranswer)
    playing()

# After the code is done, it will call this function, where the user will input their guesses here.
# While-true loop is used again to let user only enter valid answers while Error message is not present.
def playing():
    global attempt
    global exactly
    print("Here are 'Red', 'Pink', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'White' colours")
    time.sleep(1)
    print("Only write the first letter only. (capital or small letter are both acceptable)")
    attempt = 1
    exactly = 0
    guess = ['R', 'P', 'O', 'Y', 'G', 'B', 'V', 'W']
    if exactly == 4:
        attempt = 14
        exitdoor()
    else:
        while attempt < 13:
            global answer
            answer = []
            print("This is your", attempt, "attempt.")
            for i in range(1, 5):
                guessing = str(input("Enter your guessing for " + str(i) + " place: "))
                guessing = guessing.upper()
                while guessing not in guess:
                    print("Please enter the valid characters.")
                    guessing = str(input("Enter your guessing for " + str(i) + " place: "))
                    guessing = guessing.upper()
                else:
                    answer.append(guessing)
            while len(answer) == 4:
                print("Your " + str(attempt) + "'s attempted answer is: " + str(answer))
                checking()
                attempt = attempt + 1
                break
            while exactly == 4:
                break
        else:
            print("Oops, you failed to break the code in given trials.")
            finish()





# After the attempt, it will call this function, where the code maker will check on the answer.
# This is the most difficult part within the program, which is to find the way to avoid duplicate counts of same colour.
# Therefore, we need to remove the counted colours before starting another count.
# It will tell the user how close their input is to the answer.
# When the colour pattern is correct, it will congratulate the user and tell he/she how many attempt(s) they took.
def checking():
    global exactly
    almost = 0
    exactly = 0
    for i in coranswer:
        j = 0
        while (j < len(answer)):
            if i in answer and i == answer[j]:
                exactly = exactly + 1
                answer.pop(j)
                break
            elif i in answer and i != answer[j]:
                almost = almost + 1
                break
            else:
                break
        j = j + 1
    print("Correct colour in correct place: " + str(exactly))
    print("Correct colour in wrong place: " + str(almost))

    while exactly == 4:
        print("Congratulation! You win the game.")
        time.sleep(1)
        print("You took " + str(attempt) + " attempt(s) to break the code.")
        attempt == 15
        finish()
        break

# This function will allow the user to choose whether he/she want to play again.
# If the answer is yes, the program will return back to generate code function and let the user play again.
# If the answer is no, the program will execute the exitdoor function to exit the whole program.
# It is also the most time-consuming attempt, which made me procrastinate until the last day.
# This is because the exitdoor function did not work as expected and will constantly return back to the playing function.
# The global of exactly(4) is another backup to ensure the guessing loops will end.
def finish():
    global exactly
    print("Hope you enjoy the game, thank you~")
    time.sleep(1)
    while True:
        try:
            print("Only {Y/N} or {y/n] are accepeted.")
            again = str(input("Do you want to play again? {Y/N}: "))
            if again.upper() == 'Y':
                print("Yes! Come on")
                ingame()
            if again.upper() == 'N':
                exactly == int(4)
                print("Alright... this is the end.")
                time.sleep(1)
                exitdoor()
                break
        except:
            continue

# The entrance to exit the game, it is like a cinema, you won't go back through the main lobby. 
# sys.exit is not enough, it will just raise SystemExit, therefore try, except blocks are used again.
def exitdoor():
    import sys
    try:
        sys.exit()
    except SystemExit:
        print("Bye~")

# This is the ticket to the main lobby.
main()