import itertools
import sys
from collections import Counter

from data import DICTIONARY, LETTER_SCORES, pouch

NUM_LETTERS = 7

def draw_letters():
    return pouch.draw(NUM_LETTERS)

def input_word(draw):
    word = None

    while True:
        word = input("Syötä sana (tai '0' palataksesi valikkoon): ")
        if word == "0":  # Check if the user wants to go back
            return None  # Returning None to signal going back
        if _validation(word, draw):
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

def remaining_letters():
    return pouch.remaining_letters()

def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calculate_word_value)

def display_start_menu():
    print("\n--- Scrabble ---")
    print("(1) Aloita uusi peli")
    print("(2) Lue ohjeet")
    print("(3) Lopeta")

    choice = None
    while True:
        try:
            choice = int(input("Syötä valinta (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Virheellinen syöte, yritä uudelleen.")
        except ValueError:
            print("Virheellinen syöte, yritä uudelleen.")

def display_menu():
    print("(1) Syötä sana")
    print("(2) Vaihda kirjaimia")
    print("(3) Lue ohjeet")
    print("(4) Lopeta")

    choice = None
    while True:
        try:
            choice = int(input("Syötä valinta (1-4): "))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Virheellinen syöte, yritä uudelleen.")
        except ValueError:
            print("Virheellinen syöte, yritä uudelleen.")

def display_end_menu():
    print("(1) Uusi peli")
    print("(2) Lopeta")

    choice = None
    while True:
        try:
            choice = int(input("Syötä valinta (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Virheellinen syöte, yritä uudelleen.")
        except ValueError:
            print("Virheellinen syöte, yritä uudelleen.")

def display_manual():
    print("Tervetuloa Scrabbleen.\n\n")
    print("Sinulla on käytettävissä 7 kirjainta. Tehtävänäsi on keksiä niistä")
    print("mahdollisimman arvokas sana. Harvinaisemmat kirjaimet ja pitkät sanat")
    print("antavat parhaan mahdollisuuden tähän. Halutessasi, voit myös vaihtaa")
    print("kirjaimia. Tällöin saat määrittää, mitkä kirjaimet haluat vaihtaa. Sitten")
    print("pussukasta nostetaan niin monta uutta kirjainta, ja vanhat kirjaimet")
    print("palautetaan pussukkaan. Kun olet keksinyt mielestäsi hyvän sanan, voit")
    print("valita sen syöttämisen. Sana tarkistetaan, ja jos se löytyy sanakirjasta,")
    print("pistemäärä kerrotaan. Halutessasi voit myös saada tietoosi, mikä olisi")
    print("ollut arvokkain mahdollinen sana niistä kirjaimista, mitä sinulla oli käytössäsi.")

def main():
    game_state = "not_started"  # Initialize the game state
    draw = None

    while True:
        if game_state == "not_started":
            choice = display_start_menu()
            match choice:
                case 1:
                    draw = draw_letters()
                    print(f"Nostetut kirjaimet: {', '.join(draw)}")
                    game_state = "in_progress"  # Change the state to in progress
                case 2:
                    display_manual()
                case 3:
                    print("Kiitos pelistä!")
                    sys.exit()
                case _:
                    print("Virheellinen valinta.")

        if game_state == "in_progress":
            choice = display_menu()
            print(f"Käytössäsi olevat kirjaimet: {', '.join(draw)}")

            match choice:
                case 1:
                    word = input_word(draw)
                    if word is None:  # If the player chose to go back to the menu
                        continue  # Skip the rest and display the menu again
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

                        game_state = "ended"
                case 2:
                    pass
                case 3:
                    display_manual()
                case 4:
                    print("Kiitos pelistä!")
                    sys.exit()
                case _:
                    print("Virheellinen valinta")

        if game_state == "ended":
            choice = display_end_menu()

            match choice:
                case 1:
                    print("Aloitetaan uusi peli!")
                    game_state = "not_started"
                case 2:
                    print("Kiitos pelistä!")
                    sys.exit()

if __name__ == "__main__":
    main()
