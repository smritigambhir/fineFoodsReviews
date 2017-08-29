# -*- coding: utf-8 -*-
"""
Created on Sat Aug 05 13:59:39 2017

@author: smgambhi
"""

import random
import os
import json
import sys  

sys.setdefaultencoding('latin-1')

def read_file(fname):
    fp = open(fname)
    sample_numbers = random.sample(range(1,500000),100000)
    line_numbers = [1+(x-1)*9 for x in sample_numbers]
    sample_input=[]
    i=1
    while True:
        temp = fp.readline()
        if temp == '' or i>5116093:
            break
        if i in line_numbers:
            for k in range(1,8):
                temp = temp+fp.readline()
                i = i+1
            temp=temp.decode('utf-8','ignore').encode("utf-8")
            sample_input.append(temp)
        i = i+1
    fp.close()
    return sample_input
    
def write_sample_input_to_file(fname,documents):
    fp = open(fname,'w')
    fp.writelines(documents)
    fp.close()

def format_sampled_input(documents):
    formatted_reviews=[]
    for document in documents:
        key_value_pairs = document.split('\n')
        key_value_pairs.remove('')
        review = dict()
        for pair in key_value_pairs:
            key_value = pair.split(':')
            value = ''
            for i in range(1,len(key_value)):
                value = value + (key_value[i])
            review[key_value[0]] = value
            #print review
        formatted_reviews.append(review)
    return formatted_reviews
    
def write_json_to_file(filename,json_array):
    with open(filename, 'w') as outfile:
        json.dump(json_array, outfile)
        
    
documents=read_file('data/foods.txt')
write_sample_input_to_file('data/sampled_input.txt',documents)
formatted_reviews = format_sampled_input(documents)
write_json_to_file('data/formatted_sample_input.json',formatted_reviews)