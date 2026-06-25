import random #imported random module to randomly pick a word

print("Welcome to Hangman!") #greeting

hangman_ascii_art = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\\  |
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
  |   |
      |
      |
=========''',  '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', ]

word_list = ["apple", "banana", "melon", "orange", "mango"] #list of word to choose from

word = random.choice(word_list) #chooses a random word

letters = list(word) #stores list of letters
display = ["_"] * len(word) #stores guessed word progress
lives = 6 #total lives
while True: #while loop runs until break
    print(hangman_ascii_art[lives])
    print("Word: " + " ".join(display))
    guess = input("Guess a letter: ").strip().lower() #stores guess
    if not guess or (len(guess) > 1) or not guess.isalpha():
        print("Invalid guess!")
        continue
    if guess in letters: #checks if guess is found in letters
        for position in range(len(word)):
            if word[position] == guess:
                display[position] = guess

        while guess in letters:
            letters.remove(guess) #removes all occurrences of the letter

        print("Your letter was found!")
    else:
        lives -= 1 #one life gone when incorrect guess
        print("Your letter was not found! One life gone")

    print(f"Lives left: {lives}")

    if lives == 0: #break condition when lives over
        print(hangman_ascii_art[lives])
        print("Your Lives are gone. You Lose!")
        break
    elif not letters: #break condition when no letters remain
        print("Final Word: " + " ".join(display))
        print("You guessed all letters. You Win!")
        break
