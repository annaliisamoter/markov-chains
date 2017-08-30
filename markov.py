"""Generate Markov text from text files."""

from random import choice
from pprint import pprint
import sys
input_path = sys.argv[1]
n = int(sys.argv[2])


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(input_path).read()

    return contents


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    word_list = input_text.split()

    for i in range(len(word_list) - n):
        key_elements = word_list[i:i + n]
        key = tuple(key_elements)

        if key in chains:
            value = chains[key]
            value.append(word_list[i + n])

        else:
            value = [word_list[i + n]]
            chains[key] = value

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    capitalized_keys = sorted(chains)
    capitalized_key_options = capitalized_keys[:2]
    pprint(capitalized_keys)

    new_key = choice(capitalized_key_options)
    value_list = chains[new_key]

    words.extend(new_key)

    while new_key in chains:

        random_word_to_add = choice(value_list)
        words.append(random_word_to_add)
        new_key_list = words[-n:]
        new_key = tuple(new_key_list)
        print new_key

        if new_key in chains:
            value_list = chains[new_key]

    return " ".join(words)


#input_path = "green-eggs.txt"
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n)

# Produce random text
random_text = make_text(chains)

print random_text
