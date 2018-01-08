import requests
from bs4 import BeautifulSoup

url = 'http://www.yellowpages.com/los-angeles-ca/coffee?g=los%20angeles%2C%20ca&q=coffee'
url_page_2 = url + '&page=' + str(2) + '&s=relevance'

r = requests.get(url)
print(r.content) #醜

soup = BeautifulSoup(r.content,'lxml')
links = soup.find_all('a')
    #print(link.get('href'))
for link in links :
    #print (link.text.encode() , link.get('href'))
    print ("<a href =' %s '>%s </a>" %(link.get('href'),link.text))

g_data = soup.find_all('div',{'class':"info"})
for item in g_data:
    #print (item.text)
    business_name = item.contents[0].find_all('a',{"class":"business-name"})[0].text
    try:
        print (item.contents[1].find_all('span',{'itemprop':'streetAddress'})[0].text)
    except:
        pass
    try:
        print (item.contents[1].find_all('span',{'itemprop':'addressLocality'})[0].text.replace(',',''))
    except:
        pass
    try:
        print (item.contents[1].find_all('span',{'itemprop':'addressRegion'})[0].text)
    except:
        pass
    try:
        print (item.contents[1].find_all('span',{'itemprop':'postalCode'})[0].text)
    except:
        pass
    try:
        print (item.contents[1].find_all('li',{'class':'primary'})[0].text)
    except:
        pass