
import json
import operator

from flask import Flask
from flask import jsonify
from flask import request
from Text_Processor import Text_Processor
from create_index import read_formatted_input

app = Flask(__name__)

text_processor = Text_Processor()

def read_index_file(filename):
    global index
    with open(filename, 'r') as file:
        index = json.load(file)

def search(query):
    qterms=text_processor.preprocess_query(query)
    docs={}
    unit_score = 1/len(qterms)
    for qt in qterms:
        docindex=[v[0] for v in index[qt]]
        for doc in docindex:
            if doc not in docs:
                docs[doc] = unit_score
            else:
                docs[doc] = (float)(docs[doc]) + unit_score    
    sorted_docs = sorted(docs.items(), key=operator.itemgetter(1))
    sorted_docs = sorted_docs[::-1]
    sorted_docs = sorted_docs[0:20]
    return sorted_docs

@app.route('/')
def default_page():
    output_reviews=[]
    read_index_file('data/review_index.json')
    sorted_docs = search("cat-processed-bad-good")
    input_docs = read_formatted_input('data/formatted_sample_input.json') 
    for (index,score) in sorted_docs:
        output_reviews.append(input_docs[index])
    return jsonify(output_reviews)

@app.route('/<query>')
def search_query(query):
    output_reviews=[]
    read_index_file('data/review_index.json')
    sorted_docs = search(query)
    input_docs = read_formatted_input('data/formatted_sample_input.json') 
    for (index,score) in sorted_docs:
        output_reviews.append(input_docs[index])
    return jsonify(output_reviews)

if __name__ == '__main__':
    app.debug = True
    app.run()
    
