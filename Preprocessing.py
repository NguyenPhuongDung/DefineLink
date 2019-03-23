from pyvi import ViTokenizer # thư viện NLP tiếng Việt
from sklearn.model_selection  import train_test_split
from tqdm import tqdm
import numpy as np
import gensim # thư viện NLP
import os 
import pickle
dir_path = os.path.dirname(os.path.realpath(os.getcwd()))
dir_path = os.path.join(dir_path, 'DefineLink')

def get_data(folder_path):
    X = []
    y = []
    dirs = os.listdir(folder_path)
    for file_path in tqdm(dirs):
        with open(os.path.join(folder_path, file_path), 'r', encoding="utf8") as f:
            lines = f.readlines()
            lines = ' '.join(lines)
            lines = gensim.utils.simple_preprocess(lines)
            lines = ' '.join(lines)
            lines = ViTokenizer.tokenize(lines)

            X.append(lines)
            y.append(file_path)
    return X, y

train_path = os.path.join(dir_path, 'Test')
X_data, y_data = get_data(train_path)
# X_train, X_test, y_train,  y_test = train_test_split(X_data, y_data , test_size=0.2) 
pickle.dump(X_data, open('test/X_test.pkl', 'wb'))
pickle.dump(y_data, open('test/y_test.pkl', 'wb'))
# pickle.dump(X_test, open('data/X_test.pkl', 'wb'))
# pickle.dump(y_test, open('data/y_test.pkl', 'wb'))