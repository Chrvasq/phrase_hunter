YELLOW = '\033[1;93m'  # Bold and yellow
END = '\033[0m'  # Reset formatting


class Character:
    def __init__(self, char):
        """Instantiate Character object

        Arguments:
            char {str} -- Single str character from A-Z (a-z)
        """
        self.original = char
        self.was_guessed = False

    def compare_guess(self, guess):
        """Takes 'guess' as an argument and compares 'guess' to the
        Character object

        Arguments:
            guess {str} -- Single str character from A-Z (a-z)

        Returns:
            Bool -- Returns True
        """
        if guess.lower() == self.original.lower():
            self.was_guessed = True
        return self.was_guessed

    def show(self):
        """Dictates what to return based on self.was_guessed status
        of Character object

        Returns:
            str -- Returns either '_' or self.original with formatting
        """
        if self.was_guessed:
            return YELLOW + self.original + END
        else:
            return '_'
