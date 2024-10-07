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

def calculate_word_value(word):
    return(sum(LETTER_SCORES.get(char.upper(), 0) for char in word))

def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""

    dictionary_set = {word.upper() for word in DICTIONARY}
    perm_set = _get_permutations_draw(draw)
    possible_words = list(perm_set & dictionary_set)

    return possible_words


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    permutations = set(
        ''.join(perm).upper()  # Join tuples into strings and convert to uppercase
        for length in range(1, 8)  # Generate permutations for lengths 1 to 7
        for perm in itertools.permutations(draw, length)
    )

    return permutations

def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calculate_word_value)

def main():
    draw = draw_letters()
    print("Nostetut kirjaimet: {}".format(', '.join(draw)))

    word = input_word(draw)
    word_value = calculate_word_value(word)
    print(f"Syötit sanan: {word}, sen arvo on: {word_value}")

    print_max_word = input("Haluatko nähdä optimaalisen sanan (k/e)?")
    if print_max_word.lower() == 'k':
        possible_words = get_possible_dict_words(draw)

        max_word = max_word_value(possible_words)
        max_word_score = calculate_word_value(max_word)
        if max_word_score == word_value:
            print("Onnistuit jo löytämään optimaalisen sanan, onnittelut!")
        else:
            print(f"Optimaalinen sana olisi ollut {max_word}, jonka pistearvo on {max_word_score}.")


if __name__ == "__main__":
    main()
