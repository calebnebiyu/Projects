import random
from hangman_art import stages
from hangman_art import logo

from hangman_words import word_list

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

print(logo)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
incorrect_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters or guess in incorrect_letters:
        print(f"You've already guessed '{guess}'! Try a different letter.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
            incorrect_letters += letter

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}'. Wrong letter, you lose a life!")

        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************\nThe correct word was {chosen_word}.")

    if "_" not in display:
        game_over = True
        print(f"****************************YOU WIN****************************")

    print(stages[lives])