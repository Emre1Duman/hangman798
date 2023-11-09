import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for i in range(len(self.word))]
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index in range(self.word):
                letter = self.word[index]
                if letter == guess:
                    self.list_of_guesses[index] = letter
            self.num_letters - 1
        else:
            self.num_lives - 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
        



    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
    

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list)
    game(word_list, num_lives)
    while True:
        if num_lives == 0:
            print("You lost!")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if num_lives != 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")

play_game(["strawberry", "apple", "cherry", "banana", "watermelon"])
