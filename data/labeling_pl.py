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

BASENAME = 'jokes_pl'

def print_joke(content, joke_id, score):
    print('\n'*100)
    print('----- Joke joke_id : ' + joke_id + ' Joke prev. score : ' + score + ' -----')
    print('')
    print(content.replace('<br>', '\n'))


def main():
    processing = True

    with open(BASENAME + '.tsv', 'r') as fi:
        with open(BASENAME + '.temp', 'w') as fo:
            for line in fi:
                if ('&' in line) and processing:
                    old_score, joke_id, content = line.split('& ')

                    print_joke(content, joke_id, old_score)
                    new_score = input('What is you new_score [0-9,q]? ')

                    if new_score in [str(n) for n in range(10)]:
                        fo.write(new_score + ' \t ' + joke_id + ' \t ' + content)
                    else:
                        fo.write(line)
                        if new_score == 'q':
                            processing = False
                else:
                    fo.write(line)

    os.remove(BASENAME + '.tsv')
    shutil.move(BASENAME + '.temp', BASENAME + '.tsv')


if __name__ == "__main__":
    main()
