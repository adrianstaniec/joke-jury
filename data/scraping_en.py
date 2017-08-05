#!/usr/bin/env python
"""This script allows to automatically download all the jokes from laughtfactory.com
and store it in a text file, one joke per line. <br> is used as newline symbol.
"""

import requests
import bs4


FILENAME = 'jokes_en.tsv'


def main():
    open(FILENAME, 'w').close()

    joke_ids = set()

    for page in range(1, 350):
        res = requests.get('http://laughfactory.com/jokes/popular-jokes/all-time/{}'.format(page))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.content, 'html.parser')

        jokes = soup.find_all('div', {'class': 'jokes'})

        for joke in jokes:
            joke_paragraph = joke.find('div', {'class': 'joke-text'}).find('p')
            joke_id = joke_paragraph.attrs['id'][5:]
            content = joke_paragraph.text.strip().replace('\r\n', '<br>')

            thumbs_up = joke.find('a', {'class': 'like'}).find('span').text
            thumbs_down = joke.find('a', {'class': 'dislike'}).find('span').text

            if not joke_id in joke_ids:
                with open(FILENAME, 'a') as f:
                    f.write(thumbs_up + '\t' + thumbs_down + '\t' + joke_id + '\t' + content + '\n')
                joke_ids.add(joke_id)


if __name__ == "__main__":
    main()
