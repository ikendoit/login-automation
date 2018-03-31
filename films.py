from bs4 import BeautifulSoup
import requests
from selenium import webdriver


# get films infos :
def getFilms(f):
    filmlist = dict()
    for line in f.readlines():
        if "films:" in line:
            filmlist[line[0: line.index("http")]] = line[line.index("http"): ].strip()
    return filmlist


# check films:
def checkfilms(dicty):
    for i,j in dicty.items():
        re = requests.get(j)

        parser = BeautifulSoup(re.text, 'lxml')

        print(i + parser.body.find('dd', attrs={'class': 'movie-dd status'}).text)


# watch a series
def watchfilms(dicty):
    choice = input("would i like to watch anything ? : ")
    if choice == 'y':
        name = str(input("input name of series to watch: "))
        web = (list(v for k, v in dicty.items() if name in k.lower())[0])
        wd = webdriver.Chrome(CHROME_PATH)
        wd.get(web)
