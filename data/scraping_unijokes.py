#!/usr/bin/env python
"""This script allows to automatically download all the jokes from unijokes.com
and store it in a text file, one joke per line. <br> is used as newline symbol.
"""

import requests
import bs4


FILENAME = 'jokes_unijokes.tsv'


def main():
    open(FILENAME, 'w').close()


    for page in range(1, 200): #, 12694):
        joke_id = str(page)

        res = requests.get('http://unijokes.com/send-joke-{}/'.format(page), verify=False)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.content, 'html.parser')

        joke = soup.find('div', {'class': 'joke'})

        content = joke.contents[0].strip().replace('\r\n', '<br>').replace('\n', '<br>')

        spans = joke.find_all('span')

        score = spans[0].text
        votes = spans[1].text

        with open(FILENAME, 'a') as f:
            f.write(score + '\t' + votes + '\t' + joke_id + '\t' + content + '\n')


if __name__ == "__main__":
    main()
