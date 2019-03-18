from pyvi import ViTokenizer, ViPosTagger # thư viện NLP tiếng Việt
from tqdm import tqdm
import numpy as np
import gensim # thư viện NLP
import os 
dir_path = os.path.dirname(os.path.realpath(os.getcwd()))
dir_path = os.path.join(dir_path, 'DefineLink')

def get_data(folder_path):
    X = []
    y = []
    dirs = os.listdir(folder_path)
    # for path in tqdm(dirs):
        # file_paths = os.listdir(os.path.join(folder_path, path))
    for file_path in tqdm(dirs):
        with open(os.path.join(folder_path, file_path), 'r', encoding="utf-16") as f:
            lines = f.readlines()
            lines = ' '.join(lines)
            lines = gensim.utils.simple_preprocess(lines)
            lines = ' '.join(lines)
            lines = ViTokenizer.tokenize(lines)

            X.append(lines)
            y.append(file_path)

    return X, y

train_path = os.path.join(dir_path, 'Data')
X_data, y_data = get_data(train_path)