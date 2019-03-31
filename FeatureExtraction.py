import pickle
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from joblib import dump

X_data = pickle.load(open('data/X_train.pkl', 'rb'))
y_data = pickle.load(open('data/y_train.pkl', 'rb'))

X_test = pickle.load(open('test/X_test.pkl', 'rb'))
y_test = pickle.load(open('test/y_test.pkl', 'rb'))
count_vect = CountVectorizer(analyzer='word', token_pattern=r'\w{1,}')
count_vect.fit(X_data)

# transform the training and validation data using count vectorizer object
X_data_count = count_vect.transform(X_data)
X_test_count = count_vect.transform(X_test)
# word level - we choose max number of words equal to 30000 except all words (100k+ words)
tfidf_vect = TfidfVectorizer(analyzer='word', max_features=3000)
tfidf_vect.fit(X_data) # learn vocabulary and idf from training set
dump(tfidf_vect,"Main")
X_data_tfidf =  tfidf_vect.transform(X_data)
# assume that we don't have test set before
X_test_tfidf =  tfidf_vect.transform(X_test)
  
def train_model(classifier, X_data, y_data, X_test, y_test,n_epochs=3):       
    classifier.fit(X_data, y_data)
    dump(classifier,"dump")
    test_predictions = classifier.predict(X_test)  
    print("Test accuracy: ", metrics.accuracy_score(test_predictions, y_test))
train_model(MultinomialNB(), X_data_tfidf, y_data,X_test_tfidf, y_data)

