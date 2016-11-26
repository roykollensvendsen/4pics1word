#!/usr/bin/env python3
# -*- coding: utf-8 -*-'''

"""Usage: 4pics1word.py LETTERS NUMBER_OF_LETTERS
          4pics1word.py (-h | --help)
Arguments:
  LETTERS            What letters does the word contain?
  NUMBER_OF_LETTERS  How many letters does the word have?
Options:
    -h,--help  	     Show this screen and exit.
"""

from docopt import docopt
from nltk.corpus import words

word_list = words.words()

def main(docopt_args):
    """Our main method"""
    # Retrieve arguments
    letters = docopt_args['LETTERS']
    number_of_letters = int(docopt_args['NUMBER_OF_LETTERS'])
    for word in word_list:
        if len(word) == number_of_letters:
            for letter in word:
                if letter not in letters:
                    break
            if letter in letters:
                print(word)

if __name__ == "__main__":
    arguments = docopt(__doc__)
    main(arguments)
