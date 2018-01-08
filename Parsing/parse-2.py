import requests
import csv
from bs4 import BeautifulSoup


def makesoup(url):
    page = requests.get(url)
    #page.encoding = 'utf-8'
    soupdata = BeautifulSoup(page.text.encode('utf-8'), 'html.parser')
    return soupdata


soup = makesoup('http://www.the-numbers.com/movie/records/All-Time-International-Box-Office')

playee = []
player = []
#playlist = []
#realplayer = []

for record in soup.findAll('tr'):
    # print(record.text)
    for players in record.findAll('td'):
        player.append(players.text)
        playlist = [player[i:i + 6] for i in list(range(0, len(player), 6))]
print(*playlist,sep='\n')
