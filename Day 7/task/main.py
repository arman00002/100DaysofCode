import random
import hangman_art
import hangman_words
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
# TODO-2: - Update the code below to use the stages List from the file hangman_art.py
stages=hangman_art.stages
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
word_list=hangman_words.word_list
lives = 6
chosen_word = random.choice(word_list)
display = ["_"]*len(chosen_word)
print("Word to guess: " + " ".join(display))
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()
     # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed {guess}\n")
        continue
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i]==guess:
                display[i]=guess
    else:
        lives-=1
        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        #  e.g. You guessed d, that's not in the word. You lose a life.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stages[6-lives])
    if '_' in display:
        print("Word to guess: " + " ".join(display))
        # TODO-6: - Update the code below to tell the user how many lives they have left.
        print(f"****************************{'❤️ ' * lives}{'💔 ' * (6 - lives)} ({lives} LIVES LEFT)****************************")

    if lives == 0:
        game_over = True
        print(stages[6])
        # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
        print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print(f"You guessed the word correctly. IT WAS {chosen_word}!\n")
        print("****************************YOU WIN****************************")

