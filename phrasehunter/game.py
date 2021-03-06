from .phrase import Phrase
from random import choice
from os import system, name, sys

# list of phrase choices
PHRASES = ['Time Stone',
           'Power Stone',
           'Soul Stone',
           'Reality Stone',
           'Space Stone',
           'Mind Stone']
# ANSI escape sequence variables to add color
RED = '\033[1;91m'  # Bold and red
YELLOW = '\033[1;93m'  # Bold and yellow
GREEN = '\033[1;92m'  # Bold and green
UNDERLINE = '\033[4m'  # Add underline
END = '\033[0m'  # Reset formatting


class Game:
    def __init__(self, phrases=PHRASES):
        """Instantiates a Game object and takes in a list of strings

        Keyword Arguments:
            phrases {list} -- list of strings (default: {PHRASES})
        """
        self.phrases = [Phrase(phrase) for phrase in phrases]
        self.active_phrase = choice(self.phrases)
        self.lives = 5
        self.playing = True
        self.already_guessed = []

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
        """Prompts user to replay and creates new instance of Game if yes

        Raises:
            ValueError: Error if user_input is not "y" or "n"

        Returns:
            object -- Game object
        """
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

    def print_previous_guesses(self):
        print('Previous guesses: ')
        for index, letter in enumerate(self.already_guessed):
            if index != len(self.already_guessed) - 1:
                print(GREEN + letter + END, end=', ')
            else:
                print(GREEN + letter + END, end='\n')
        print('\n')

    def get_user_input(self):
        """Prompts user for guess input and processes input. Handles logic for
        checking guesses against active phrase.

        Raises:
            ValueError: Guess is in already_guessed list
            ValueError: Empty input
            ValueError: Guess is not a letter
            ValueError: Guess is more than one letter
        """
        try:
            user_input = input('Guess a letter: ')
            print('\n')
            if user_input.lower() in self.already_guessed:
                raise ValueError(YELLOW + 'You already guessed '
                                 f'{user_input.lower()}.\n' + END)
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
            if len(self.already_guessed) > 0:  # prints previous guesses
                self.print_previous_guesses()
            if user_input.lower() in [letter.original.lower() for letter in
                                      self.active_phrase if letter != ' ']:
                for letter in self.active_phrase:
                    if letter != ' ':
                        letter.compare_guess(user_input)  # checks guess
                self.active_phrase.print_phrase()
            else:
                self.lives -= 1
                print(f'You have {self.lives} out of 5 lives remaining!\n')
                if user_input.lower() not in self.already_guessed:
                    self.already_guessed.append(user_input.lower())
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
