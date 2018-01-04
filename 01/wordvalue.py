from data import DICTIONARY, LETTER_SCORES

def load_words(filename=DICTIONARY):
    """Load dictionary into a list and return list"""
    with open(filename, 'r') as f:
        return [_.strip() for _ in f.readlines()]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    global LETTER_SCORES
    return sum([ LETTER_SCORES.get(c, 0) for c in word.upper() ])

def max_word_value(list_of_words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    l = load_words() if list_of_words is None else list(list_of_words)
    l.sort(key=calc_word_value, reverse=True)
    return l[0]

if __name__ == "__main__":
    pass # run unittests to validate
