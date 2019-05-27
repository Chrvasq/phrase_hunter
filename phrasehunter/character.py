class Character:
    def __init__(self, char):
        self.original = char
        self.was_guessed = False

    def compare_guess(self, guess):
        if guess.lower() == self.original.lower():
            self.was_guessed = True
        return self.was_guessed

    def show(self):
        if self.was_guessed:
            return self.original
        else:
            return '_'

    def __str__(self):
        return str(self.original)
