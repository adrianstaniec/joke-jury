#!/usr/bin/env python
"""This script is for made to facilitate manual labelling process
It shows user the joke and asks for new rating.

Format for unlabbeled joke should be:
original_score & joke_id & joke_content

Format after labelling will be:
proper_label\tjoke_id\tjoke content
"""

import os
import shutil


def print_joke(content, number, score):
    print('\n'*100)
    print('----- Joke number : ' + number + ' Joke prev. score : ' + score + ' -----')
    print('')
    print(content.replace('<br>', '\n'))


def main():
    processing = True

    with open('polish_jokes.tsv', 'r') as fi:
        with open('polish_jokes.temp', 'w') as fo:
            for line in fi:
                if ('&' in line) and processing:
                    old_score, number, content = line.split('& ')

                    print_joke(content, number, old_score)
                    new_score = input('What is you new_score [0-9,q]? ')

                    if new_score in [str(n) for n in range(10)]:
                        fo.write(new_score + ' \t ' + number + ' \t ' + content)
                    else:
                        fo.write(line)
                        if new_score == 'q':
                            processing = False
                else:
                    fo.write(line)

    os.remove('polish_jokes.tsv')
    shutil.move('polish_jokes.temp', 'polish_jokes.tsv')


if __name__ == "__main__":
    main()
