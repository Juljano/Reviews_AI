import os
import joblib
import spacy
import pandas
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

csv_path = "cleaned_data/trustpilot_reviews_with_ratings.csv"

def read_csv_file(filename):
    with open(filename, "r", encoding='utf-8') as csv_file:
        df = pandas.read_csv(csv_file)
        review_body = df["review_body"].values
        review_rating = df["review_rating"].values

    return review_body, review_rating


class Preprocessing:
    def __init__(self):
        self.nlp = spacy.load('de_core_news_sm')
        reviews_bodies, rating_values = read_csv_file(csv_path)
        clean_tokens = self.tokenize(reviews_bodies)
        self.tfidf_transform(clean_tokens, rating_values)

    def tokenize(self, review_body):
        clean_tokens = []
        for review in review_body:
            doc = self.nlp(review)
            tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct and token.is_alpha] # Info: token.is_alpha = No Numbers and Emojis
            clean_tokens.append(tokens)

        return clean_tokens

    def tfidf_transform(self, reviews_bodies, rating_values):

        if len(reviews_bodies) and len(rating_values):
            print("The number of review bodies and rating values is equal")

        y = rating_values # rating values (1 - 5 Stars)
        tfidf_vectorizer = TfidfVectorizer()
        x_tfidf = tfidf_vectorizer.fit_transform([' '.join(review) for review in reviews_bodies]) # read reviews from the list

        x_train, x_test, y_train, y_test = train_test_split(x_tfidf, y, test_size=0.2, random_state=42, stratify=y)

        logistic_model = LogisticRegression(max_iter=10000)
        logistic_model.fit(x_train, y_train)


        accurcy = metrics.accuracy_score(y_test, logistic_model.predict(x_test))
        print(f"Genauigkeit: {accurcy:2f}")
        print(classification_report(y_test, logistic_model.predict(x_test)))

        #save model in the 'Model'-Folder
        if not os.path.exists("Model"):
            os.mkdir("Model")

        joblib.dump(logistic_model, "Model/reviews_tfidf_model.pkl")
        joblib.dump(tfidf_vectorizer, "Model/reviews_vectorizer.pkl")
        print("Model gespeichert")
