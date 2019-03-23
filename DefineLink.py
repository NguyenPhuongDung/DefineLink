from bs4 import BeautifulSoup
import urllib.request
import re
from pyvi import ViTokenizer # thư viện NLP tiếng Việt

def  not_relative_uri(href):
    return re.compile('^https://').search(href) is  not  None

url = 'https://vnexpress.net/bong-da/su-sup-do-cua-de-che-quyen-kien-thien-tan-o-bong-da-trung-quoc-3897791.html'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
new_feeds = soup.findAll(class_='title_news')
for nfeed in new_feeds:
    feed = nfeed.find("a")
    if feed==None or feed=="":
        continue
    title = feed.get('title')
    link = feed.get('href')
    if title==None or title=="" or link==None:
        continue
    subpage = urllib.request.urlopen(link)
    subsoup = BeautifulSoup(subpage, 'html.parser')
    contents = subsoup.findAll(class_='Normal')
    result = ""
    for deail in contents:
        content = deail.getText().strip().lower()
        content = re.sub('[!@#$".,()]', '', content)
        result += content
    result = ViTokenizer.tokenize(result)
    print(result)

