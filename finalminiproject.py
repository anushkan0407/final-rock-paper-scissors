import random
def round(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif((user_choice=="rock" and computer_choice=="scissors") or 
         (user_choice=="paper" and computer_choice=="rock") or 
         (user_choice=="scissors" and computer_choice=="paper")):
        return "user"

    else:
        return "computer"

def main():
    choices = ["rock","paper","scissors"]
    user_score = 0
    computer_score = 0

    print("Welcome to Rock,Paper,Scissors game!🤗")
    print("🪨📰✂")
    print("-" * 40)

    rounds = input("How many rounds do you want to play?⏯️")

    if rounds.isalpha() or  int(rounds) <= 0:
        print(" Invalid number of rounds. Please run the game again.🤷🏻‍♀️")
        return

    rounds = int(rounds)
    print("-" * 40)

    for round_num in range(1, rounds + 1):
        print("rounds:",round_num,"/", rounds)
        user_choice = input("Enter rock, paper, or scissors: ").lower()

        if user_choice not in choices:
            print(" Invalid choice entered, round is skipped.🤷🏻‍♀️")
            print("-" * 40)
            continue

        computer_choice = random.choice(choices)
        print("computer chose:",computer_choice)

        result = round(user_choice, computer_choice)

        if result == "user":
            print("You win this round!🎊")
            user_score = user_score+1
        elif result == "computer":
            print(" Computer wins this round!💻")
            computer_score = computer_score+1
        else:
            print("It's a tie!🪢")

        print(f"Current Score → You: {user_score} | Computer: {computer_score}")
        print("-" * 40)

  
    print("Final Results:")
    print("Your Score:",user_score)
    print("Computer Score:",computer_score)

    if user_score > computer_score:
        print(" Congratulations! You won the game!🎉🎉")
    elif computer_score > user_score:
        print("Computer won the game!! Try again!👩‍💻😓")
    else:
        print("It's an overall tie!🪢")


main()





