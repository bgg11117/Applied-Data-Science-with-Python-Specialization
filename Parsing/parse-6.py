import requests
import string
import csv
from bs4 import BeautifulSoup


def makesoup(url):
    page = requests.get(url)
    soupdata = BeautifulSoup(page.text, 'html.parser')
    return soupdata

playerdatasaved = ""

for letter in string.ascii_lowercase:
    soup = makesoup('http://www.basketball-reference.com/players/%s' %letter)


    for record in soup.findAll('tr'):
        playerdata = ""
        player=""
        for players in record.findAll('th'):
            for play in players.findAll('a'):
                player += ""+play.text + ","+ play['href']

    #print(player)
        for data in record.findAll('td'):
            playerdata += ","+ data.text
    #print(playerdata)
        playerdatasaved += "\n" + player + playerdata
    print(playerdatasaved)

header = "Player,Url,From,To,Pos,Ht,Wt,date,year,College"

with open('Basketball-4.csv','w') as f:
    file=csv.writer(f, delimiter=" ", quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    file.writerow(header)
    file.writerow(playerdatasaved)
f.close()
