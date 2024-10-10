from collections import Counter
import random

class Pouch:
    def __init__(self, distribution):
        # Initialize pouch with given letter distribution
        self.initial_distribution = distribution  # Store the original distribution
        self.letter_values = {letter.name: int(letter.value) for letter in distribution}
        self.reset()

    def draw(self, num_letters):
        drawn_letters = []
        for _ in range(num_letters):
            letter = random.choice(list(self.pouch.elements()))
            self.pouch[letter] -= 1
            if self.pouch[letter] == 0:
                del self.pouch[letter]
            drawn_letters.append(letter)
        return drawn_letters

    def return_letters(self, discarded_letters):
        for letter in discarded_letters:
            self.pouch[letter] += 1

    def remaining_letters(self):
        return dict(self.pouch)  # Return a dictionary of remaining letters and counts

    def reset(self):
        """Reset the pouch to its original state for a new game."""
        self.pouch = Counter({letter.name: int(letter.amount) for letter in self.initial_distribution})

    def format_letters(self, letters):
        """Return a string with letters and their values formatted as 'A:1, B:2, C:1'."""
        return ', '.join(f"{letter}:{self.letter_values.get(letter, 0)}" for letter in letters)
