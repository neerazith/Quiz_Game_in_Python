from quizQuestions import questionsOne, prizes


correctAnswer = 0
prize = []


#For better visuals.
def lines():
    print("----"*7)


#Working mechanism of game
def startGame(question):
    global prize
    global correctAnswer
    gameRunning = True
    while gameRunning:
        for i in range(len(question)):
            lines()
            print(f"Your question for Rs.{prizes[correctAnswer]}:\n")
            lines()
            print(f"{i+1}.{question[i][0]}")
            lines()
            print(f"""A){question[i][1]}
B){question[i][2]}
C){question[i][3]}
D){question[i][4]}""")
            lines()
            answer = (input("Please type your answer(a-d): ")).upper()     
            lines()
            if (answer == question[i][-1]):
                correctAnswer += 1 
                prize = prizes[correctAnswer]
                print(prize)
                if (i < len(question) - 1):
                    print(f"Correct Answer!\nYou won Rs.{prizes[i]}")
                if(i == len(question)-1):
                    gameRunning = False
                    break
            else:
                print(f"Incorrect! The correct answer is {question[i][-1]}")
                if (i == len(question) -1 ):
                    gameRunning = False
                    break
            lines()

    return prize, correctAnswer


#Welcome
lines()
print(f"Welcome to KBC.\nThere are {len(questionsOne)} questions for you.")
lines()
print("Your Balance: 0")
lines()


#Start game if want to play.
play = input("Do you want to start the game(y/n):").upper()
while True:
    if (play == "Y"):
        startGame(questionsOne)
        break
    elif (play == "N"):
        lines()
        print("See you again. Bye Bye")
        lines()
        quit()
    else:
       play = input("Please choose between(y/n): ").upper()



#Displaying score and asking to play again.
lines()
print(f"CONGRATULATIONS!\nYou got {correctAnswer} questions correct\nYou won: {prizes[correctAnswer-1]}")
lines()
lines()
playAgain = input("Do you want to play again(y/n): ").upper()
while True:
    if playAgain == "Y":
        startGame(questionsOne)
    elif playAgain == "N":
        lines()
        print("See you again. Bye Bye")
        lines()
        quit()
    else:
        playAgain = input("Please choose between(y/n): ")
