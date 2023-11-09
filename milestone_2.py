import random
word_list = ["Strawberry", "Apple", "Cherry", "Banana", "Watermelon"]

print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Guess a letter: ")



if len(guess) == 1 and guess.isdigit() == False:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")