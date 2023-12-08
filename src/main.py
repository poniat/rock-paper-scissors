import random
import os

playerScore = 0
cpuScore = 0

rock = "rock"
paper = "paper"
scissors = "scissors"

os.system("cls")

while playerScore < 3 and cpuScore < 3:
    cpuChoice = random.choice([rock, paper, scissors]).lower()
    playerChoice = input(f"Pick one: {rock}, {paper} or {scissors}: ").lower()

    # rock > scissors > paper > rock
    if playerChoice == cpuChoice:
        print("TIE. No points.")
    elif (playerChoice == rock and cpuChoice == scissors) or (playerChoice == scissors and cpuChoice == paper) or (playerChoice == paper and cpuChoice == rock):
        playerScore += 1
        print(f"You win. It's {playerScore}:{cpuScore}.")
    else:
        cpuScore += 1
        print(f"CPU win. It's {playerScore}:{cpuScore}.")

if playerScore == 3:
    print(f"YOU WIN. Final score is {playerScore}:{cpuScore}")
else:
    print(f"CPU WIN. Final score is {playerScore}:{cpuScore}")