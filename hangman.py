import random as r
import sys


class HangMan:
    def __init__(self):
        self.guessed_letters = None
        self.validated = None
        self.menu_choice = None
        self.computer_choice = None
        self.guessed_word = None
        self.greeting = "H A N G M A N"
        self.words_list = ["python", "java", "swift", "javascript"]
        self.user_guess = ""
        self.mistakes = 0
        self.wins = 0
        self.losses = 0

    def get_user_guess(self):
        self.validated = False
        while not self.validated:
            print()
            print(''.join(self.guessed_word))
            self.user_guess = input(f"Input a letter: ")
            self.validate_input()

    def get_computer_choice(self):
        self.computer_choice = r.choice(self.words_list)
        self.guessed_word = ["-"] * len(self.computer_choice)

    def check_win_condition(self):
        if ''.join(self.guessed_word) == self.computer_choice:
            return True
        else:
            return False

    def validate_input(self):
        if len(self.user_guess) == 1:
            if self.user_guess.isalpha() and self.user_guess.islower():
                self.validated = True
                return
            print("Please, enter a lowercase letter from the English alphabet.")
        else:
            print("Please, input a single letter.")
        self.validated = False

    def check_user_guess(self):
        if self.user_guess in self.computer_choice and self.user_guess not in self.guessed_word:
            for i in range(len(self.computer_choice)):
                if self.computer_choice.startswith(self.user_guess, i):
                    self.guessed_word[i] = self.user_guess
            return True
        elif self.user_guess in self.guessed_word or self.user_guess in self.guessed_letters:
            print("You've already guessed this letter.")
            return True
        else:
            print("That letter doesn't appear in the word.")
            return False

    def game_loop(self):
        self.get_computer_choice()
        self.guessed_letters = set()
        while self.mistakes < 8:
            if self.check_win_condition():
                print()
                print(f"You guessed the word {''.join(self.guessed_word)}!")
                print("You survived!")
                self.wins += 1
                break
            self.get_user_guess()
            if not self.check_user_guess():
                self.mistakes += 1
            self.guessed_letters.add(self.user_guess)
        if not self.check_win_condition():
            print()
            print("You lost!")
            self.losses += 1

    def menu_selection(self):
        print(self.greeting)
        while True:
            self.menu_choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
            if self.menu_choice == "play":
                self.game_loop()
            elif self.menu_choice == "results":
                print(f"You won: {self.wins} times")
                print(f"You lost: {self.losses} times")
            elif self.menu_choice == "exit":
                sys.exit()

g1 = HangMan()
g1.menu_selection()
