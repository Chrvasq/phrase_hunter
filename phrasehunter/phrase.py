from phrasehunter.character import Character


class Phrase:
    def __init__(self, phrase):
        self.phrase = [Character(char) for char in phrase]
        self.phrase_guessed = False

    def print_phrase(self):
        for letter in self.phrase:
            print(letter.show(), end=' ')

    def check_guess(self, guess):
        for letter in self.phrase:
            letter.compare_guess(guess)

    def guessed_phrase(self):
        phrase_length = len(self.phrase)
        count = 0

        for letter in self.phrase:
            if letter.was_guessed:
                count += 1
        if count == phrase_length:
            self.phrase_guessed = True
        return self.phrase_guessed
