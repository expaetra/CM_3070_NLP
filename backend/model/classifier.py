#Simple machine learning classifier that predicts computer science discipline of a research paper

#Imports
from sklearn.feature_extraction.text import TfidfVectorizer #Convert text to numerical vectors
from sklearn.linear_model import LogisticRegression #Classificaiton mode
from .data import TRAINING_DATA #Labeled examples used for training


class CSDisciplineClassifier: 
    def __init__(self):
        texts, labels = zip(*TRAINING_DATA) #Separate training data into paper descriptions and CompSci disciplines

        #Set up model, remove stopwords, avoid overfitting
        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=3000,
        )

        X =self.vectorizer.fit_transform(texts) #Convert the training text into TF-IDF vectors

        #Initialize classifier, train it on the vectorized data
        self.model = LogisticRegression(max_iter=1000)
        self.model.fit(X, labels) 

    #Prediction function - inference on unseen text
    def predict(self, text: str) -> dict:
        X = self.vectorizer.transform([text]) 
        probs = self.model.predict_proba(X)[0] #Get probabilities
        classes = self.model.classes_ #Retrieve labels 

        #Return the most likely CompSci disciplines and probability distribution
        return {
            "prediction": self.model.predict(X)[0],
            "probabilities": {
                cls: float(prob)
                for cls, prob in zip(classes,probs)
            },
        }
