from .character import Character


class Phrase:
    def __init__(self, phrase):
        self.phrase = [Character(letter) for letter in phrase]

    def print_phrase(self):
        for letter in self.phrase:
            print(letter.show(), end=' ')
        print('\n')

    def phrase_guessed(self):
        count = 0

        for letter in self.phrase:
            if letter.was_guessed:
                count += 1
        if count == len(self.phrase):
            return True
        return False

    def __iter__(self):
        yield from self.phrase
