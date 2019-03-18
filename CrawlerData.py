from bs4 import BeautifulSoup
import urllib.request
import re
import csv

def  not_relative_uri(href):
    return re.compile('^https://').search(href) is  not  None

url = 'https://vnexpress.net/'
category = [{'tag':'the-thao','id':0},{'tag':'phap-luat','id':1}]
for cate in category:
    page = urllib.request.urlopen(url+cate['tag'])
    soup = BeautifulSoup(page, 'html.parser')
    new_feeds = soup.findAll(class_='title_news')
    with open('data-'+cate['tag']+'.csv', 'w', encoding='utf8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Title', 'Content'])
        for nfeed in new_feeds:
            feed = nfeed.find("a")
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



# with open('data.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(['Title', 'Link'])
#     for feed in new_feeds:
#         title = feed.get('title')
#         link = feed.get('href')
#         writer.writerow([title, link])
#         print('Title: {} - Link: {}'.format(title, link))


# from bs4 import BeautifulSoup
# from sklearn.pipeline import Pipeline
# from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
# from sklearn.linear_model import LogisticRegression as LR
# import urllib.request
# import re
# url =  'https://vnexpress.net/'
# category = [{'tag':'the-thao','id':0},{'tag':'phap-luat','id':1}]
# train = {'text':[],'label':[]}
# test = {'text':[],'label':[]}
# word_dict = []
# for cate in category:
# 	page = urllib.request.urlopen(url+cate['tag'])
# 	soup = BeautifulSoup(page, 'html.parser')
# 	new_feeds = soup.findAll(class_='title_news')
# 	n = len(new_feeds)
# 	num_trend = int(3*n/4)
# 	num_test = n - num_trend
# 	print(num_test,num_trend)
# 	index = 0
# 	for nfeed in new_feeds:
# 		index = index + 1
# 		feed = nfeed.find("a")
# 		title = feed.get('title')
# 		link = feed.get('href')
# 		if title==None or title=="" or link==None:
# 			continue
# 		subpage = urllib.request.urlopen(link)
# 		subsoup = BeautifulSoup(subpage, 'html.parser')
# 		contents = subsoup.findAll(class_='Normal')
# 		train_contents = []
# 		test_contents = []
# 		for deail in contents:
# 			content = deail.getText().strip().lower()
# 			content = re.sub('[!@#$".,()]', '', content)
# 			content = content.split(' ')
# 			word_dict = set(word_dict).union(set(content))
# 			if index <= num_trend:
# 				train_contents = set(train_contents).union(set(content))
# 			else:
# 				test_contents = set(test_contents).union(set(content))
# 		train['text'].append(train_contents)
# 		train['label'].append(cate['id'])
# 		test['text'].append(test_contents)
# 		test['label'].append(cate['id'])
# 	break
# # print(word_dict)
# list=[]
# for sentence in train['text']:
# 	bags = dict.fromkeys(word_dict,0)
# 	for word in sentence:
# 		bags[word]+=1
# for senc in train['text']:
# 	bags = dict.fromkeys(word_dict,0)
# 	for word in sentence:
# 		bags[word]+=1
# 	list.append(bags)
# print(train['label'])
# X_train, y_train = train['text'], train['label']
# X_test, y_test = test['text'], test['label']
# lr_clf = Pipeline([('vect', CountVectorizer(stop_words='english')), ('tfidf', TfidfTransformer()), ('clf',LR())])
# lr_clf.fit_transform(X_train)
# lr_clf.fit(X=X_train, y=y_train)
# lr_acc, lr_predictions = imdb_acc(lr_clf)
# print(lr_acc)