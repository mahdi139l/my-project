
import random
choices = ["rock", "paper", "scissors"]
user_score = 0
pc_score = 0
while True:
    user = input("rock / paper / scissors ? (type 'exit' to quit): ")
    if user == "exit":
        break
    pc = random.choice(choices)
    print(f"Computer chose: {pc}")
    if user == pc:
        print("It's a tie!")
    elif (user == "rock" and pc == "scissors") or \
         (user == "paper" and pc == "rock") or \
         (user == "scissors" and pc == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        pc_score += 1
    print(f"Your score: {user_score} | Computer score: {pc_score}\n")

