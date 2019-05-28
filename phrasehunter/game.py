from .phrase import Phrase
from random import choice
from os import system, name, sys

PHRASES = ['Time', 'Power', 'Soul', 'Reality', 'Space', 'Mind']
RED = '\033[1;91m'  # Bold and red
YELLOW = '\033[1;93m'  # Bold and yellow
GREEN = '\033[1;92m'  # Bold and green
UNDERLINE = '\033[4m'  # Add underline
END = '\033[0m'  # Reset formatting


class Game:
    def __init__(self, phrases=PHRASES):
        self.phrases = [Phrase(phrase) for phrase in phrases]
        self.active_phrase = choice(self.phrases)
        self.lives = 5
        self.playing = True

    def clear_screen(self):
        system('cls' if name == 'nt' else 'clear')

    def welcome_message(self):
        welcome_message = ' Phrase Hunter '
        print('#' * (len(welcome_message) + 2))
        print(f'#{welcome_message}#')
        print('#' * (len(welcome_message) + 2))
        print(YELLOW + '\nWelcome to Phrase Hunter!\n' + END)
        print(GREEN + UNDERLINE + 'Instructions' + END + ': Try to guess the '
              'phrase by entering in a single letter from A-Z. '
              'You have 5 lives.\n')

    def won_game(self):
        self.playing = False
        print(YELLOW + 'You won! You guessed the phrase!\n' + END)
        self.replay()

    def lost_game(self):
        self.playing = False
        print(RED + 'You lost! Better luck next time!\n' + END)
        self.replay()

    def replay(self):
        try:
            user_input = input('Would you like to play again? (Y/N) > ')
            if user_input.lower() not in ['y', 'n']:
                raise ValueError
        except ValueError:
            print(YELLOW + 'Please enter in \'Y\' or \'N\'.\n' + END)
            self.replay()
        else:
            if user_input.lower() == 'y':
                return Game().main()
            else:
                print(YELLOW + '\nThanks for playing! See you '
                      'next time!\n' + END)
                sys.exit()

    def get_user_input(self):
        try:
            user_input = input('Guess a letter: ')
            print('\n')
            if len(user_input) == 0:
                raise ValueError(YELLOW + 'You didn\'t enter a letter. '
                                 'Please enter a letter between A-Z\n' + END)
            if not user_input.isalpha():
                raise ValueError(YELLOW + 'You entered a number. '
                                 'Please enter a letter between A-Z.\n' + END)
            if len(user_input) > 1:
                raise ValueError(YELLOW + 'Please enter one letter.\n' + END)
        except ValueError as error:
            print(error)
            self.get_user_input()
        else:
            if user_input.lower() in [letter.original.lower() for letter
                                      in self.active_phrase]:
                for letter in self.active_phrase:
                    letter.compare_guess(user_input)
                self.active_phrase.print_phrase()
            else:
                self.lives -= 1
                print(f'You have {self.lives} out of 5 lives remaining!\n')
                self.active_phrase.print_phrase()

    def main(self):
        self.clear_screen()
        self.welcome_message()
        self.active_phrase.print_phrase()

        while self.playing:
            self.get_user_input()
            if self.active_phrase.phrase_guessed():
                self.won_game()
            if self.lives == 0:
                self.lost_game()
