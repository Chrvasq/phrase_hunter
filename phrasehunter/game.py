from phrasehunter.phrase import Phrase
from random import choice

class Game:
    def __init__(self):
        phrases = ['Time', 'Power', 'Soul', 'Reality', 'Space', 'Mind']
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

    def process_turn(self):
        guess = self.get_user_input()

        while guess is None:
            guess = self.get_user_input()

        if not self.active_phrase.check_guess(guess):
            self.lives -= 1
        self.active_phrase.print_phrase()
        self.active_phrase.guessed_phrase()
