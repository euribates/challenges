#!/usr/bin/env python3
#
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import random
from itertools import permutations
from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7
ALL_WORDS = [s.upper() for s in DICTIONARY]

# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def _validation(word, letters):
    global DICTIONARY
    word = word.upper()
    if word not in ALL_WORDS:
        raise ValueError('Word {} not in dictionary'.format(word))
    backup = letters[:]
    for letter in word:
        if letter not in backup:
            raise ValueError(
                'Word {} not a valid combination of'
                ' letters'.format(word)
                )
        backup.remove(letter)


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    word = ''
    while not word:
        word = input('Form a valid word:').strip()
        try:
            _validation(word, draw)
        except ValueError as err:
            print(err)
            print('Word {} is not valid'.format(word))
            word = ''
    return word


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    letters = [
        random.choice(POUCH)
        for _ in range(7)
        ]
    return letters


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    for n in range(1, NUM_LETTERS+1):
        for p in permutations(draw, n):
            yield ''.join(p)



def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    return [
        p 
        for p in _get_permutations_draw(draw) 
        if p in ALL_WORDS
        ]


def main():
    letters = draw_letters()
    print('Letters drawn: {}'.format(', '.join(letters)))
    word = input_word(letters)
    print('Word chosen: {} (value: {})'.format(word, calc_word_value(word)))
    possibles = get_possible_dict_words(letters)
    if possibles:
        best = max_word_value(possibles)
        print('Optimal word possible: {} (value: {})'.format(best,
            calc_word_value(best)))
    else:
        print("I can't think any word, you win")

if __name__ == "__main__":
    main()
