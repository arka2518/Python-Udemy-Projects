import random
user_choice = int(input("What will you choose?\nPress:\n0 for Rock\n1 for Paper\n2 for Scissors\n"))
x = random.randint(0, 2)
print(f"You chose: {user_choice}\nComputer chose: {x}")
if user_choice == 0 and x == 1:
    print("You lose!")
elif user_choice == 1 and x == 2:
    print("You lose!")
elif user_choice == 0 and x == 2:
    print("You win!")
elif user_choice == 1 and x == 0:
    print("You win!")
elif user_choice == 2 and x == 0:
    print("You lose!")
elif user_choice == 2 and x == 1:
    print("You win!")
elif user_choice >= 3 or user_choice < 0:
    print("Invalid input! You lose!")
else:
    print("It's a draw!")
