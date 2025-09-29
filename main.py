import os

import Preprocessing
from ModelExecutor import starting_model


if __name__ == '__main__':

    if not os.path.exists("Model/reviews_tfidf_model.pkl"):
        preprocessor = Preprocessing.Preprocessing()
    else:
        print("Model existiert schon")

    try:
        while True:
            start = starting_model(input("Bitte gebe eine Bewertung ab: "))
    except KeyboardInterrupt:
        print("Programm abgebrochen")

