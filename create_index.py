import json

from Indexer import Indexer
from Text_Processor import Text_Processor

indexer = Indexer()
text_processor = Text_Processor()

def read_formatted_input(filename):
    with open(filename) as json_data:
        full_reviews = json.load(json_data)
    return full_reviews

def get_review_text(full_reviews):
    review_text = []
    for review in full_reviews:
        review_text.append(review['review/text'])
    return review_text

def print_index_to_file():
    full_reviews = read_formatted_input('data/formatted_sample_input.json')
    review_text = get_review_text(full_reviews)
    indexer.process_review_text(review_text,text_processor.preprocess_text)
    with open('data/review_index.json', 'w') as file:
     file.write(json.dumps(indexer.terms))
    
if __name__ == "__main__" :
    print_index_to_file()