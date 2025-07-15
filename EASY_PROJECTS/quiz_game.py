# Regex class, strings stuff.
import re

print("Welcome to Foxy's Quiz with Marshall D Teach - Blackbeard Zehahahahaha!")

yes_responses = {"yes", "y", "yeah", "yep", "ye", "sure", "ok", "okay"}
no_responses = {"no", "n", "nah", "nope" "wont" "cant"}

playing = input("Do you want to play? (Yes/No): ").casefold().strip()

while playing not in yes_responses and playing not in no_responses:
    print("It's not a yes or not, you trying me? Zehahahaha")
    playing = input("Just say yes/no: ").casefold().strip()

if playing in no_responses:
    print("Zehahahaha! Make sure to come back with a spine!")
    exit()


print("Zehahaha! I bet you'll lose brat!! Zehahahahah \n Now let's begin! Zehahahahaha")
userScore = 0

# Question - 1
answer1 = input("What does N.A.S.A. stand for? ")
answer1Words = re.findall(r"[a-z]+", answer1.casefold())
answer1Seq = ["national", "aeronautics", "space", "administration"]

index = 0
for word in answer1Words:
    if word == answer1Seq[index]:
        index += 1
        if index == len(answer1Seq):
            break

if index == len(answer1Seq):
    print("Correct answer! Zehahah not bad brat!")
    userScore += 1
else:
    print("Zehahha 1st question, wasted - you're pathetic!!")

# Question - 2
answer2 = input("Who are the 4 emperors? ")
answer2Words = set(re.findall(r"[a-z]+", answer2.casefold()))
answer2Seq = {"luffy", "shanks", "blackbeard", "buggy"}

if all(word in answer2Words for word in answer2Seq):
    print("Not bad! Zehahahah you know I'm one so be careful!!")
    userScore += 1
else:
    print(
        "Zehahahaha! Wrong again. I'm taking you into as my chore boy!! It's over. Last chance Zehahahhaha"
    )

# Question - 3
answer3 = input(
    "Name six or more titanic commanders of my crew? Blackbeard Crew Zehahahahahah!"
)
answer3Words = re.sub(r"[^a-z ]+", " ", answer3.casefold())
answer3Words = re.sub(r"\s+", " ", answer3Words.strip())
answer3Seq = {
    "jesus burgess",
    "shiryu",
    "van augur",
    "avalo pizzaro",
    "lafitte",
    "catarina devon",
    "sanjuan wolf",
    "vasco shot",
    "doc q",
    "kuzan",
}

answerCount = sum(1 for name in answer3Seq if name in answer3Words)
if answerCount >= 6:
    print(f"That's it. You said {answerCount} correct!")
    userScore += 1
else:
    print("Pathetic - you're mine Zehahahhaha!!")

if answerCount == 10:
    print("Wait, you've reminded all my captains! Zehahahah!! Bonus point +1")
    userScore += 1

print(f"Your final score is {userScore}/4")
match userScore:
    case 4:
        print("Zehahhaha - only a few legends could get this score. Join my crew!!!")
    case 3:
        print("Zehahaha - you're good! Join my crew!!")
    case 2:
        print("Zehahahah better than most - not bad!!")
    case 1:
        print("If there's pathetic there's you Zehahahahah!!")
    case 0:
        print("You're worse that Celestial scum Zehahahaha!!")
