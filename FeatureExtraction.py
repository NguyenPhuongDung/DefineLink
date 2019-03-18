import pickle
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import TruncatedSVD

X_data = pickle.load(open('data/X_data.pkl', 'rb'))
y_data = pickle.load(open('data/y_data.pkl', 'rb'))

# X_test = pickle.load(open('data/X_test.pkl', 'rb'))
# y_test = pickle.load(open('data/y_test.pkl', 'rb'))
# create a count vectorizer object 
count_vect = CountVectorizer(analyzer='word', token_pattern=r'\w{1,}')
count_vect.fit(X_data)

# transform the training and validation data using count vectorizer object
X_data_count = count_vect.transform(X_data)
# X_test_count = count_vect.transform(X_test)
# word level - we choose max number of words equal to 30000 except all words (100k+ words)
tfidf_vect = TfidfVectorizer(analyzer='word', max_features=30000)
tfidf_vect.fit(X_data) # learn vocabulary and idf from training set
X_data_tfidf =  tfidf_vect.transform(X_data)
# assume that we don't have test set before
# X_test_tfidf =  tfidf_vect.transform(X_test)
svd = TruncatedSVD(n_components=300, random_state=42)
svd.fit(X_data_tfidf)


X_data_tfidf_svd = svd.transform(X_data_tfidf)
# X_test_tfidf_svd = svd.transform(X_test_tfidf)