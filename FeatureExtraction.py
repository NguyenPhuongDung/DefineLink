import pickle
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn import preprocessing 
from sklearn.model_selection  import train_test_split
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from gensim.models import KeyedVectors 
import os 
from joblib import dump

dir_path = os.path.dirname(os.path.realpath(os.getcwd()))
word2vec_model_path = os.path.join(dir_path, 'DefineLink')

X_data = pickle.load(open('data/X_train.pkl', 'rb'))
y_data = pickle.load(open('data/y_train.pkl', 'rb'))

X_test = pickle.load(open('test/X_test.pkl', 'rb'))
y_test = pickle.load(open('test/y_test.pkl', 'rb'))
# create a count vectorizer object 
count_vect = CountVectorizer(analyzer='word', token_pattern=r'\w{1,}')
count_vect.fit(X_data)

# transform the training and validation data using count vectorizer object
X_data_count = count_vect.transform(X_data)
X_test_count = count_vect.transform(X_test)
# word level - we choose max number of words equal to 30000 except all words (100k+ words)
tfidf_vect = TfidfVectorizer(analyzer='word', max_features=3000)
tfidf_vect.fit(X_data) # learn vocabulary and idf from training set
X_data_tfidf =  tfidf_vect.transform(X_data)
# assume that we don't have test set before
X_test_tfidf =  tfidf_vect.transform(X_test)

svd = TruncatedSVD(n_components=300, random_state=42)
svd.fit(X_data_tfidf)


X_data_tfidf_svd = svd.transform(X_data_tfidf)
X_test_tfidf_svd = svd.transform(X_test_tfidf)



encoder = preprocessing.LabelEncoder()
y_data_n = encoder.fit_transform(y_data)
y_test_n = encoder.fit_transform(y_test)

encoder.classes_ # kết quả: array(['Chinh tri Xa hoi', 'Doi song', 'Khoa hoc', 'Kinh doanh',
                 #                 'Phap luat', 'Suc khoe', 'The gioi', 'The thao', 'Van hoa',
    
# def train_model(classifier, X_data, y_data, X_test, y_test,is_neuralnet=False, n_epochs=3):       
#     X_train, X_val, y_train, y_val = train_test_split(X_data, y_data, test_size=0.1, random_state=42)
    
#     if is_neuralnet:
#         classifier.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=n_epochs, batch_size=512)
        
#         val_predictions = classifier.predict(X_val)
#         test_predictions = classifier.predict(X_test)
#         val_predictions = val_predictions.argmax(axis=-1)
#         test_predictions = test_predictions.argmax(axis=-1)
#     else:
#         classifier.fit(X_train, y_train)
    
#         train_predictions = classifier.predict(X_train)
#         val_predictions = classifier.predict(X_val)
#         test_predictions = classifier.predict(X_test)
#     # print("train_predictions accuracy: ", metrics.accuracy_score(train_predictions, y_val))    
#     print("Validation accuracy: ", metrics.accuracy_score(val_predictions, y_val))
#     print("Test accuracy: ", metrics.accuracy_score(test_predictions, y_test))
# train_model(MultinomialNB(), X_data_tfidf, y_data,X_test_tfidf, y_data, is_neuralnet=False)
# train_model(MultinomialNB(), X_data_tfidf_svd, y_data, is_neuralnet=False)
# train_model(MultinomialNB(), X_data_tfidf_svd, y_data, is_neuralnet=False)

mnb = MultinomialNB()
mnb = mnb.fit(X_data_tfidf, y_data)
dump(mnb,"dump")
