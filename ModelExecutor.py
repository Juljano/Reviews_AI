import joblib

# load TF-IDF Vectorizer and Logistic Regression
vectorizer = joblib.load("Model/reviews_vectorizer.pkl")  # TF-IDF Vectorizer
clf = joblib.load("Model/reviews_tfidf_model.pkl")  # Logistic Regression

def starting_model(message_from_user):

    new_review = [message_from_user]
    #convert review into TF-IDF
    X_new = vectorizer.transform(new_review)

    # prediction
    prediction = clf.predict(X_new)

    print(F"Prediction: {prediction}")

    if prediction <= 2:
        print("Negative")
    elif prediction >= 4:
        print("Positive")
    else:
        print("Neutral")

