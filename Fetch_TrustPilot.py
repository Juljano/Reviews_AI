import pandas as pd
import json




with open('reviews_ab_author.json', encoding='utf-8') as inputfile:
    json_value = json.load(inputfile)



df.to_csv('csvfile.csv', encoding='utf-8', index=False)



