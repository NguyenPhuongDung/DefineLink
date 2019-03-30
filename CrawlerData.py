from bs4 import BeautifulSoup
import urllib.request
import re
import csv

def  not_relative_uri(href):
    return re.compile('^https://').search(href) is  not  None

url = 'https://vnexpress.net/'
category = [{'tag':'kinh-doanh','name':'Kinh Doanh'},{'tag':'the-thao','name':'The Thao'}, 
            {'tag':'giai-tri','name':'Giai Tri'}, {'tag':'du-lich', 'name':'Du Lich'}, {'tag':'so-hoa','name':'So Hoa'}]
for cate in category:
    for i in range(0, 20):
        page = urllib.request.urlopen(url+cate['tag'] +'/p'+ str(i))
        soup = BeautifulSoup(page, 'html.parser')
        new_feeds = soup.findAll(class_='title_news')
        with open(cate['name']+'.csv', 'a', encoding='utf8') as csv_file:
            writer = csv.writer(csv_file)
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
                writer.writerow([title, result])
