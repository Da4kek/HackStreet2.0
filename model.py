import pandas as pd 
from Utils import preprocess
from sklearn.model_selection import train_test_split
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
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
        param_grid = [{'vect__ngram_range':[(1,1)],
                    'vect__stop_words':[None,stop],
                    'vect__tokenizer':[tokenizer,tokenizer_port],
                    'svm__C':[1.0,2.0,3.0,4.0,5.0],
                    'svm__kernel':['linear','rbf'],
                    'svm__gamma':['auto','scale'],
                    },
                    {'vect__ngram_range':[(1,1)],
                    'vect__stop_words':[None,stop],
                    'vect__tokenizer':[tokenizer,tokenizer_port],
                    'vect__norm':[None],
                    'vect__use_idf':[False],
                    'svm__C':[1.0,2.0,3.0,4.0,5.0,6.0],
                    'svm__kernel':['linear','rbf'],
                    'svm__gamma':['auto','scale']}]

        ps_svm_tf = Pipeline([("vect",tfidf),
                            ("svm",SVC(random_state=1))])

        grid_svm_tf = GridSearchCV(ps_svm_tf,param_grid,
                                cv=5,
                                verbose=1,
                                n_jobs=-1,
                                scoring='accuracy')
        grid_svm_tf.fit(X_train, y_train)
        self.model = grid_svm_tf.best_estimator_
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
