import random #imported random module to randomly pick a word

print("Welcome to Hangman!") #greeting

word_list = ["apple", "banana", "melon", "orange", "mango"] #list of word to choose from

word = random.choice(word_list) #chooses a random word
print(word) #prints to showcase for now
