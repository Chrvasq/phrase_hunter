from .phrase import Phrase
from random import choice
from os import system, name, sys

PHRASES = ['Time', 'Power', 'Soul', 'Reality', 'Space', 'Mind']


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

    def won_game(self):
        self.playing = False
        print('You won! You guessed the phrase!')
        self.replay()

    def lost_game(self):
        self.playing = False
        print('You lost! Better luck next time!')
        self.replay()

    def replay(self):
        try:
            user_input = input('Would you like to play again? Y/N ')
            if user_input.lower() not in ['y', 'n']:
                raise ValueError
        except ValueError:
            print('Please enter in \'Y\' or \'N\'.')
            self.replay()
        else:
            if user_input.lower() == 'y':
                return Game().main()
            else:
                print('Thanks for playing! See you next time!\n')
                sys.exit()

    def get_user_input(self):
        try:
            user_input = input('Guess a letter: ')
            if len(user_input) == 0:
                raise ValueError('You didn\'t enter a letter. '
                                 'Please enter a letter between A-Z')
            if not user_input.isalpha():
                raise ValueError('You entered a number. '
                                 'Please enter a letter between A-Z.')
            if len(user_input) > 1:
                raise ValueError('Please enter one letter.')
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
                print(f'You have {self.lives} out of 5 lives remaining!')
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
