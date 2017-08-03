"""This script allow to automatically download all the jokes from perelki.net
and store it in a text file, one joke per line. <br> is used as newline symbol.

Format for unlabbeled joke will be:
score & joke_id & joke_content
"""

import requests
import bs4


FILENAME = 'polish_jokes.tsv'


def main():
    open(FILENAME, 'w').close()

    for number in range(0, 6000):
        res = requests.get('https://perelki.net/one.php?id={}'.format(number))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.content, 'html.parser')

        label = soup.find_all('span')[1].contents[0].strip()

        if label != '':
            div = soup.find_all('div', {'class': 'container'})[1].contents[:-2]
            content = '<br>'.join([x.string.strip() for x in div if not x.string is None])

            with open(FILENAME, 'a') as f:
                f.write(label + ' & ' + str(number) + ' & ' + content + '\n')

if __name__ == "__main__":
    main()
