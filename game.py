import itertools
import random
from collections import Counter

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7

def draw_letters():
    return random.sample(POUCH, NUM_LETTERS)

def input_word(draw):
    word = None

    while not _validation(word, draw):
        word = input("Syötä sana: ")

    return word

def _validation(word, draw):
    if word is None:
        return False

    # Count frequency of letters in both word and draw
    word_count = Counter(word.upper())
    draw_count = Counter(draw)

    # Check if the word uses more of any letter than is available in the draw
    for letter, count in word_count.items():
        if count > draw_count.get(letter, 0):
            print(f"Käytit liian monta '{letter}'-kirjainta. Vain {draw_count[letter]} käytettävissä.")
            return False

    return any(word.upper() == dict_word.upper() for dict_word in DICTIONARY)


def main():
    draw = draw_letters()
    print("Nostetut kirjaimet: {}".format(', '.join(draw)))

    word = input_word(draw)
    print(f"Syötit sanan: {word}")


if __name__ == "__main__":
    main()
