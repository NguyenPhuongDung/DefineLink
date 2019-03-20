from sklearn import preprocessing 
from sklearn.model_selection  import train_test_split
from sklearn import metrics
import pickle

X_data = pickle.load(open('data/X_data.pkl', 'rb'))
y_data = pickle.load(open('data/y_data.pkl', 'rb'))
encoder = preprocessing.LabelEncoder()
y_data_n = encoder.fit_transform(y_data)
# y_test_n = encoder.fit_transform(y_test)

encoder.classes_ # kết quả: array(['Chinh tri Xa hoi', 'Doi song', 'Khoa hoc', 'Kinh doanh',
                 #                 'Phap luat', 'Suc khoe', 'The gioi', 'The thao', 'Van hoa',
print(encoder.classes_)     
def train_model(classifier, X_data, y_data,is_neuralnet=False, n_epochs=3):       
    X_train, X_val, y_train, y_val = train_test_split(X_data, y_data, test_size=0.1, random_state=42)
    
    if is_neuralnet:
        classifier.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=n_epochs, batch_size=512)
        
        val_predictions = classifier.predict(X_val)
        # test_predictions = classifier.predict(X_test)
        val_predictions = val_predictions.argmax(axis=-1)
        # test_predictions = test_predictions.argmax(axis=-1)
    else:
        classifier.fit(X_train, y_train)
    
        train_predictions = classifier.predict(X_train)
        val_predictions = classifier.predict(X_val)
        # test_predictions = classifier.predict(X_test)
        
    print("Validation accuracy: ", metrics.accuracy_score(val_predictions, y_val))
    # print("Test accuracy: ", metrics.accuracy_score(test_predictions, y_test))
    train_model(naive_bayes.MultinomialNB(), X_data_tfidf, y_data, is_neuralnet=False)
