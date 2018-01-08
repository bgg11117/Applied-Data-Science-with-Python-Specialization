from lxml import etree
import requests

def main():
    page = 1
    jsonData = []
    while True:
        result = requests.get("http://axe-level-1.herokuapp.com/lv2?page=%s" % str(page))
        result.encoding = 'utf8' #重要
        root = etree.fromstring(result.text, etree.HTMLParser())
        rows = root.xpath("//table[@class='table']/tr[position()>1]")
        if len(rows) == 0:
            break
        else:
            tmp = ""
            for row in rows:
                column = row.xpath("./td/text()")
                #print(column)
                tmp += '{"town": "%s", "village": "%s", "name": "%s",},' % (column[0], column[1], column[2])
            jsonData.append(tmp)
            page+=1
    # 刪除最後一個逗號
    print(*jsonData,sep='\n')

if __name__ == "__main__":
    main()