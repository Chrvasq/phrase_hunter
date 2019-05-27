from .phrase import Phrase
from random import choice


class Game:
    def __init__(self, phrases):
        self.phrases = [Phrase(phrase) for phrase in phrases]
        self.active_phrase = choice(self.phrases)
        self.lives = 5
        self.playing = True

    def start_game(self):
        self.active_phrase.print_phrase()

    def end_game(self):
        self.playing = False

    def get_user_input(self):
        user_input = ''

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
        else:
            return user_input

    def process_guess(self, guess=None):
        while guess is None:
            guess = self.get_user_input()
        if guess.lower() in [letter.original.lower() for letter
                             in self.active_phrase]:
            for letter in self.active_phrase:
                letter.compare_guess(guess)
            self.active_phrase.print_phrase()
        else:
            self.lives -= 1
            print(f'You have {self.lives} out of 5 lives remaining!')
            self.active_phrase.print_phrase()
