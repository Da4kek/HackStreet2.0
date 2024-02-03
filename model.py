import pandas as pd 
from Utils import preprocess
from sklearn.model_selection import train_test_split
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords
from sklearn.model_selection import GridSearchCV



class TextClassifier:
    def __init__(self, train_file, test_file, model_file):
        self.train_file = train_file
        self.test_file = test_file
        self.model_file = model_file
        self.load_data()
        self.train_model()
        

    def load_data(self):
        self.train_data = pd.read_csv(self.train_file)
        self.test_data = pd.read_csv(self.test_file)

    def train_model(self):
        stop = stopwords.words("english")
        tokenizer = preprocess.tokenizer
        tokenizer_port = preprocess.tokenizer_port
        X_train = self.train_data['Subtitle']
        y_train = self.train_data['New_Emotion']
        X_test = self.test_data['Subtitle']
        y_test = self.test_data['New_Emotion']

        tfidf = TfidfVectorizer(strip_accents=None,
                                lowercase=False,
                                preprocessor=None)
        param_grid = [{"vect__ngram_range": [(1, 1)],
                       "vect__stop_words": [stop, None],
                       "clf__penalty": ['l1', 'l2'],
                       "clf__C": [1.0, 10.0, 100.0],
                       "vect__tokenizer": [tokenizer, tokenizer_port]},
                      {"vect__ngram_range": [(1, 1)],
                       "vect__stop_words": [stop, None],
                       "vect__tokenizer": [tokenizer, tokenizer_port],
                       "vect__norm": [None],
                       "vect__use_idf": [False],
                       "clf__penalty": ['l1', 'l2'],
                       "clf__C": [1.0, 10.0, 100.0]}]
        lr_tfidf = Pipeline([("vect", tfidf),
                             ("clf", LogisticRegression(random_state=0, solver='liblinear'))])


        gs_lr_tfidf = GridSearchCV(lr_tfidf, param_grid, scoring='accuracy',
                           cv=5,
                           verbose=1,
                           n_jobs=-1)
        gs_lr_tfidf.fit(X_train, y_train)
        self.model = gs_lr_tfidf.best_estimator_
        print("Train accuracy: ", self.model.score(X_train, y_train))
        print("Test accuracy: ", self.model.score(X_test, y_test))

    def save_model(self):
        joblib.dump(self.model, self.model_file)

if __name__ == "__main__":
    train_file = "Data/Train_Data_updated.csv"
    test_file = "Data/Test_Data_updated.csv"
    model_file = "Data/model.pkl"
    text_classifier = TextClassifier(train_file, test_file, model_file)
    text_classifier.save_model()
