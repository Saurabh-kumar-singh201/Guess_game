import random

print("Welcome to my game world!\n\n")

def numberGuesser():
    return random.randint(1, 100)

def judge(userInput, currentNo, nextNumber, score):
    if userInput == 'h' and nextNumber != currentNo:
        is_correct = nextNumber > currentNo
    elif userInput == 'l' and nextNumber != currentNo:
        is_correct = nextNumber < currentNo
    else:
        print(f"Next number is {nextNumber}\nWhat a coincidence, since you guessed no and current no is same so you gain or lose nothing")
        return score
    if is_correct:
        print(f"Next number is {nextNumber}\nYou are CORRECT! and thus WIN 10 points")
        return score + 10
    else:
        print(f"Next number is {nextNumber}\nYou are Wrong! and thus LOSE 10 points")
        return score - 10

answerForPlaying = input("Do you want to play a game? (press 'y' for yes and 'n' for no): ").lower()

if answerForPlaying == 'y':
    print("Okay let's get started!")
    print("\n\nYou are given 50 points and you have to guess a number if it's higher than the present number or if it's lower.\nIf you guess correctly, you gain 10 points, and if you fail, you lose 10 points.\nThis game will have a total of 5 rounds.\n\n")
    
    while True:
        score = 50
        for _ in range(5):
            currentNo = numberGuesser()
            userInput = input(f"\n\nCurrent number is {currentNo}, guess whether the next number will be higher or lower.\nPress 'h' for higher and 'l' for lower: ").lower()
            nextNo = numberGuesser()
            score = judge(userInput, currentNo, nextNo, score)
            print(f"\n\nYour current score is {score}")
        
        answer = input("\n\nDo you want to play again? (press 'y' for yes and 'n' for no): ").lower()
        if answer == 'n':
            print("\n\nThanks for playing this game!")
            break
