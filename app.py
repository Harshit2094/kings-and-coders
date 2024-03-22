import game

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word.lower():
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word  = game.generate_phrase()
    hint = game.get_hint(word)
    print(hint)
    guessed_letters = []
    attempts = 6
    print(HANGMANPICS[0])  
    while attempts > 0:
        # Display current status
        print(display_word(word, guessed_letters))
        print(f"Attempts left: {attempts}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        # Add the guessed letter to the list
        guessed_letters.append(guess)
        # Check if the guess is correct
        if guess not in word:
            print("Incorrect guess!")
            print(HANGMANPICS[len(HANGMANPICS) - attempts])
            attempts -= 1
        else:
            print("Correct guess!")
        # Check if the word has been completely guessed
        if all(letter in guessed_letters for letter in word.lower()):
            print("Congratulations! You've guessed the word:", word)
            break
    else:
        print("Sorry, you're out of attempts. The word was:", word)

# Run the game
hangman()
