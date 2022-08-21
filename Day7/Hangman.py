import random
import Hangman_art
import Hangaman_words
from replit import clear

chosen_word = random.choice(Hangaman_words.word_list)
word_length = len(chosen_word)
display = []
end_of_game =False
lives = 6

for _ in range(word_length):
    display += "_"

print(Hangman_art.logo)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(Hangman_art.stages[lives])
        if lives == 0:
            end_of_game = True
            print(f"The word is {' '.join(chosen_word)}")
            print("You lose.")

    if "_" not in display:
        end_of_game = True
        print("You win.")
        print(f"The word is {' '.join(display)}")

