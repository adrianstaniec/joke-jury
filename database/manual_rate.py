import os
import shutil


def print_joke(content: str):
    print('\n'*100)
    print('----- Joke number : ' + id + ' Joke prev. score : ' + old_score + ' -----')
    print('')
    print(content.replace('<br>', '\n'))


processing = True

with open('polish_jokes.tsv', 'r') as fi:
    with open('polish_jokes.temp', 'w') as fo:
        for line in fi:
            if ('&' in line) and processing:
                old_score, id, content = line.split('& ')

                print_joke(content)
                score = input('What is you score [0-9,q]? ')

                if score in [str(n) for n in range(10)]:
                    fo.write(score + ' \t ' + id + ' \t ' + content)
                elif score == 'q':
                    fo.write(line)
                    processing = False
                else:
                    fo.write(line)
            else:
                fo.write(line)

os.remove('polish_jokes.tsv')
shutil.move('polish_jokes.temp', 'polish_jokes.tsv')


