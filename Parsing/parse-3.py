import requests
import csv
from bs4 import BeautifulSoup
import locale
locale.setlocale(locale.LC_ALL, '')

def makesoup(url):
    page = requests.get(url)
    soupdata = BeautifulSoup(page.text, 'html.parser')
    return soupdata

soup = makesoup('http://www.basketball-reference.com/players/a/')

data=[]
playee = []
playerdata = []
player = []
realplayerdata = []

for record in soup.findAll('tr'):
    # print(record.text)
    for players in record.findAll('th'):
        for play in players.findAll('a'):
            player.append(play.text)
            realplayer = [player[i:i + 1] for i in list(range(0, len(player), 1))]

    for data in record.findAll('td'):
        column = data.text

        playee.append(column)
        playlist = [playee[i:i + 7] for i in list(range(0, len(playee), 7))]

i = 0

while i < max(list(range(len(playlist)))) + 1:
    playlist[i].insert(0, realplayer[i][0])
    i += 1

print(*playlist, sep="\n")


#or

#for i in list(range(len(playlist))):
    #if i == max(list(range(len(playlist))))+ 1:
        #break
    #else:
        #for j in list(range(7)):
            #realplayer[i].insert(1, playlist[i][j])
# or
    # else:
        #playlist[i].insert(0, realplayer[i][0])  因為只有插入一項


#print(*realplayer, sep="\n")

#------------------------------
# print (list(zip(realplayer[i],playlist[i])))

#tmp = ""
# tmp += '{"From": "%s", "To": "%s", "Pos": "%s", "Ht": "%s", "Wt": "%s", "Birth": "%s", "College": "%s"}'\
# % (playlist[i][0], playlist[i][1], playlist[i][2],playlist[i][3],playlist[i][4],
# playlist[i][5],playlist[i][6])
# playerdata.append(tmp)

#for i  in ...
#{
   #print x[ i ] ;  print \n;
#}

# print(playerdata)
# print(playerdata[0])

# page+=1
# if len(playerdata)!=0:
# playerdatasave = playerdatasave + "\n" + playerdata[1:]

# header = "From,To,Pos,Ht,Wt,Birth Date,College"
with open('Basketball.csv','w') as f:
    file=csv.writer(f)
    for row in playlist:
        file.writerow(row)
f.close()


#print(data)
    #f = open("player.csv", "w")
    #w = csv.writer(f)
    #w.writerows(data)
    #f.close()
