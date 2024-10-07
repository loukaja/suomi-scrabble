import csv
from collections import namedtuple

Letter = namedtuple('Letter', 'name amount value')


def load_words():
    word_set = set()

    with open('nykysuomensanalista2024.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')

        for row in csv_reader:
            word = row[0].strip()
            if '-' not in word:
                word_set.add(word)

    return word_set

DICTIONARY = load_words()

distribution = [
    Letter(name='A', amount='10', value='1'),
    Letter(name='B', amount='1', value='8'),
    Letter(name='C', amount='1', value='10'),
    Letter(name='D', amount='1', value='7'),
    Letter(name='E', amount='8', value='1'),
    Letter(name='F', amount='1', value='8'),
    Letter(name='G', amount='1', value='8'),
    Letter(name='H', amount='2', value='4'),
    Letter(name='I', amount='10', value='1'),
    Letter(name='J', amount='2', value='4'),
    Letter(name='K', amount='5', value='2'),
    Letter(name='L', amount='5', value='2'),
    Letter(name='M', amount='3', value='3'),
    Letter(name='N', amount='9', value='1'),
    Letter(name='O', amount='5', value='2'),
    Letter(name='P', amount='2', value='4'),
    Letter(name='R', amount='2', value='4'),
    Letter(name='S', amount='7', value='1'),
    Letter(name='T', amount='9', value='1'),
    Letter(name='U', amount='4', value='3'),
    Letter(name='V', amount='2', value='4'),
    Letter(name='W', amount='1', value='8'),
    Letter(name='Y', amount='2', value='4'),
    Letter(name='Ä', amount='5', value='2'),
    Letter(name='Ö', amount='1', value='7')
]

POUCH = list(''.join(
        list(Letter.name * int(Letter.amount)
            for Letter in distribution))
    )

LETTER_SCORES = dict(zip(
        [letter.name for letter in distribution],
        [int(letter.value) for letter in distribution]
    ))
