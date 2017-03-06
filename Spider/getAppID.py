import requests
from bs4 import BeautifulSoup as BS
import re

POPULAR_URL_CN = "https://itunes.apple.com/cn/genre/ios-games/id6014?mt=8"


def getAppID_most_popular():
    print("#正在获取热门app的id列表......")
    page = requests.get(url=POPULAR_URL_CN)
    html = BS(page.text,"lxml")
    div = html.find('div',{'id':"selectedcontent","class":"grid3-column"})
    href_list = div.find_all("a")
    id_list = []
    for a in href_list:
        # print(str(a['href']))
        id_str = re.findall("id[0-9]+\?",str(a['href']))[0]
        print(id_str[2:-1])
        id_list.append(id_str[2:-1])
    print("#共获取到%d个app的id." % len(id_list))
    return id_list


if(__name__=="__main__"):
    getAppID_most_popular()