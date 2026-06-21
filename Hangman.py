import random

word_list = ["gemini", "camel", "java", "python", "ruby", "javascript", "html", "css", "sql", "csharp"]
chosen_word = random.choice(word_list)
print(chosen_word)

place_holder = ""
word_length = len(chosen_word)
for position in range(1, 6):
    place_holder += "_"
print(place_holder)

game_over = False
correct_guess = []
while not game_over:
    guess = input("Guess a letter: ").lower()
    print(guess)
    display = ""
    for letter in chosen_word:
        if letter == guess:
           display += letter
           correct_guess.append(letter)
        elif letter in correct_guess:
            display += letter
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
        game_over = True
        print("You lose!")
    if "_" not in display:
        game_over = True
        print("You win!")

