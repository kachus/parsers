import requests
from lxml import etree
import lxml.html
import csv
from bs4 import BeautifulSoup
import pandas as pd




data = []
def parse(html_text):
    soup = BeautifulSoup(html_text, "lxml")
    '''''
    name = soup.findAll(attrs={"class": "_title_1p2xe_9 _titleNoCredit_1p2xe_197"})
    '''''
    name = soup.findAll(attrs={"class": "_title_1p2xe_9"})


    genre = soup.findAll(attrs={"class":"_text_163gl_28"})
    description = soup.findAll('div', class_ = "_summary_1p2xe_21")
    print(len(name))


    for i in range(len(name)):
        film_name = name[i].text.split('.')[1]
        film_description = description[i].text
        rating_number = name[i].text.split('.')[0]
        if genre[i].text != 'Film':
            film_genre = genre[i].text
        else:
            film_genre = ' - '
        data.append([rating_number,film_name, film_genre, film_description])


def chart(header, data):
    df = pd.DataFrame(data, columns = header)
    df.to_csv('/Users/Evgenia/Desktop/timeout_chart.csv')









def main():
    url = "https://www.timeout.com/film/best-movies-of-all-time"
    html_text = requests.get(url).text
    parse(html_text)
    header = ['Rating number','Film name', 'Film genre', 'Film description']
    chart(header, data)


if __name__ == "__main__":
    main()
