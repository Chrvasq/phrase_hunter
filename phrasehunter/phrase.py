from .character import Character


class Phrase:
    def __init__(self, phrase):
        """Instantiates a Phrase object and takes in a list as an argument
        
        Arguments:
            phrase {list} -- list of strings
        """
        self.phrase = [Character(letter) for letter in phrase]

    def print_phrase(self):
        """Prints out the letters in the Phrase depending on letter is guessed
        or not
        """
        for letter in self.phrase:
            print(letter.show(), end=' ')
        print('\n')

    def phrase_guessed(self):
        """Checks if the entire Phrase has been guessed
        
        Returns:
            bool -- Returns True if Phrase is guessed else returns False
        """
        count = 0

        for letter in self.phrase:
            if letter.was_guessed:
                count += 1
        if count == len(self.phrase):
            return True
        return False

    def __iter__(self):
        """Makes Phrase object iterable
        """
        yield from self.phrase
