from gensim.models import KeyedVectors 
import os 

dir_path = os.path.dirname(os.path.realpath(os.getcwd()))
word2vec_model_path = os.path.join(dir_path, "DefineLink")

w2v = KeyedVectors.load_word2vec_format(word2vec_model_path)
vocab = w2v.wv.vocab
wv = w2v.wv

def get_word2vec_data(X):
    word2vec_data = []
    for x in X:
        sentence = []
        for word in x.split(" "):
            if word in vocab:
                sentence.append(wv[word])

        word2vec_data.append(sentence)

    return word2vec_data

X_data_w2v = get_word2vec_data(X_data)
X_test_w2v = get_word2vec_data(X_test)