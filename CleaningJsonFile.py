import pandas as pd
import json


def read_json_file(json_file):
    all_reviews = []
    with open(json_file, encoding='utf-8') as jsonfile:
        json_content = json.load(jsonfile)
        if json_content:
            for block in json_content: # Hier werden alle Elemente von '@graph' ausgegeben
                graph_data = block.get('@graph', [])
                for item in graph_data:
                    if item.get('@type') == 'Review':
                        review_body = item.get('reviewBody', '')
                        headline = item.get('headline', '')
                        rating_value = item.get('reviewRating', {}).get('ratingValue', '')
                        print(F"Review Body : {review_body} & Headline : {headline} & Rating Value : {rating_value}")

                        json_data ={
                            "review_body": review_body,
                            "headline": headline,
                            "rating_value": rating_value
                        }
                        all_reviews.append(json_data)


        return  all_reviews

def write_reviews_into_csv(all_reviews):
    df = pd.DataFrame(all_reviews, columns=['review_body', 'headline', 'rating_value'])
    df = pd.DataFrame(all_reviews)
    df.to_csv("cleaned_data/trainings_data_reviews.csv", index=True)


write_reviews_into_csv(read_json_file("Raw_Data/reviews_ab_author.json"))
