import os
import Preprocessing
from ModelExecutor import starting_model

if __name__ == '__main__':
    file_path = "Model/reviews_tfidf_model.pkl"
    file_exists = os.path.isfile(file_path)
    if not file_exists:
        print("Model wird trainiert... Bitte warten")
        preprocessor = Preprocessing.Preprocessing()
        print("Model ist fertig")
    else:
        print("Model existiert schon - Model wird ausgeführt!")
    try:
        while True:
            start = starting_model(input("Bitte gebe eine Bewertung ab: "))
    except KeyboardInterrupt:
        print("Programm abgebrochen")
