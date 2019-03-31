from bs4 import BeautifulSoup
import urllib.request
import re
from pyvi import ViTokenizer
from joblib import load

link = "https://www.24h.com.vn/bong-da/video-ket-qua-bong-da-suwon-incheon-utd-7-phut-2-ban-cong-phuong-thap-thom-c48a1039560.html"      
page = urllib.request.urlopen(link) 
bsPage = BeautifulSoup(page, 'html.parser')
bodyPage = bsPage.find('body')
contentInPTags = bodyPage.findAll('p')
result = ""
data = []
for pContent in contentInPTags:
        content = pContent.getText().strip().lower()
        content = re.sub('[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]', '', content)
        result = result + " " + content
result = ViTokenizer.tokenize(result)
data.append(result)
classifier = load("dump")
main = load("Main")
x_testcv = main.transform(data)
pred = classifier.predict(x_testcv[0])
print(pred[0].rstrip('.csv'))        