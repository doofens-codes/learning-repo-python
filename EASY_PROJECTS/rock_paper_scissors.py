import random

userWins = 0
compWins = 0
gameOptions = ["rock", "paper", "scissors"]


# Function that gives out winning choice
def SupOption(_givenOption):
    superiorChoice = ""
    if _givenOption == "rock":
        superiorChoice = "paper"
    elif _givenOption == "paper":
        superiorChoice = "scissors"
    elif _givenOption == "scissors":
        superiorChoice = "rock"
    return superiorChoice


while True:
    userInput = input("Rock, Paper, Scissors or q/Q to quit: ").lower()
    if userInput == "q":
        break
    if userInput not in {"rock", "paper", "scissors"}:
        continue
    # This area means userInput is one of our options.
    compNo = random.randint(0, 2)
    # rock - 0; paper - 1; scissor - 2;
    compInput = gameOptions[compNo]
    # Computer number decides the choice taken up by computer for round.
    print(f"Your choice : {userInput}\nComputer choice : {compInput}")

    # First check if both entered same input; it is not handled in later parts
    # So it'll be done here properly

    if compInput == userInput:
        print("Both have done same! Redo!!")
        continue

    if compInput == SupOption(userInput):
        print("Computer wins! +1 to computer")
        compWins += 1
    else:
        print("You won the round! +1 to you")
        userWins += 1

    print(f"Your score is : {userWins}\nComputer score is : {compWins}")

print(f"Thanks for playing! Final scores\nYou -{userWins}\nPC -{compWins}")
