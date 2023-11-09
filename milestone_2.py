import random
word_list = ["Strawberry", "Apple", "Cherry", "Banana", "Watermelon"]
word = random.choice(word_list)

guess = input("Guess a letter: ")


if len(guess) == 1 and guess.isdigit() == False:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")