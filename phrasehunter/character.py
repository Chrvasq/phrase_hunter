class Character():
    def __init__(self, char):
        self.original = char
        self.was_guessed = False

    def compare_guess(self, guess):
        if guess.lower() == self.original.lower():
            self.was_guessed = True
        else:
            self.was_guessed = False
        return self.was_guessed
    
    def show_original_character(self):
        if self.was_guessed:
            return self.original
        else:
            return '_'
    
