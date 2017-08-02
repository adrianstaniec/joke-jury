import requests
import bs4

filename = 'polish_jokes.tsv'
open(filename, 'w').close()

for id in range(0, 6000):
    res = requests.get('https://perelki.net/one.php?id={}'.format(id))
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.content, 'html.parser')

    label = soup.find_all('span')[1].contents[0].strip()

    if label != '':
            div = soup.find_all('div', {'class': 'container'})[1].contents[:-2]
            content = '<br>'.join([x.string.strip() for x in div if not x.string == None])

            with open(filename, 'a') as f:
                    f.write(label + ' & ' + str(id) + ' & ' + content + '\n')

