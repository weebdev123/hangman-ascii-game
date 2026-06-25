import random #imported random module to randomly pick a word

print("Welcome to Hangman!") #greeting

word_list = ["apple", "banana", "melon", "orange", "mango"] #list of word to choose from

word = random.choice(word_list) #chooses a random word

letters = list(word) #stores list of letters
lives = 5 #total lives
while True: #while loop runs until break
    guess = input("Guess a letter: ") #stores guess
    if guess in letters: #checks if guess is found in letters
        letters.remove(guess) #removes the letter's first occurence
        print("Your letter was found!")
    else:
        lives -= 1 #one life gone when incorrect guess
        print("Your letter was not found! One life gone")

    if lives == 0: #break condition when lives over
        print("Your Lives are gone. You Lose!")
        break
    elif not letters: #break condition when no letters remain
        print("You guessed all letters. You Win!")
        break