import random

print("Welcome to the number guessing game!!!")

print("I'm thinking of a number between 1 and 100")

def guess_num():
    
    v = input("Choose a difficutly, Type 'easy' or 'hard': ").lower()
    num = random.randint(1, 100)
    if v == 'easy':
        attempts = 10
    else:
        attempts = 5

    while attempts > 0:
        print(f"You have {attempts} attempts remainting to guess the number")
        user_guess = int(input("Make a guess: "))
        if user_guess == num:
            print("You've guess the correct number")
            return
        elif user_guess > num:
            attempts -= 1
            print("Too high")
        else:
            attempts -= 1
            print("Too low")
        if attempts > 0:
            print("Guess again")
            continue
    print("\n" * 2)
    print(f"You have run out of guesses, you lose\nThe number was {num}")

guess_num()