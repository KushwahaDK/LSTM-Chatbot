# Building a deep NLP chatbot using seq2seq models

# importing the required libraries
import os
import re
import time

import numpy as np
import tensorflow as tf

DATASET_PATH = 'dataset/cornell movie-dialogs corpus/'

def read_dataset():
    lines_buff = open(os.path.join(DATASET_PATH,'movie_lines.txt'), mode='r', encoding='latin-1')
    lines = lines_buff.read().split('\n')
    lines_buff.close()

    converasations_buff = open(os.path.join(DATASET_PATH,'movie_conversations.txt'), mode='r', encoding='latin-1')
    converasations = converasations_buff.read().split('\n')
    converasations_buff.close()

    return lines, converasations

def data_preprocessing(lines, converasations):

    # Mapping each dialogie with the corresponding dialogie code in a dictionary for accessing easily    
    
    lines = [line for line.split('+++$+++') in lines]
    dict_mapping = dict((i, c) for i, c in enumerate(lines))

def model_building():
    pass

def model_training():
    pass

def model_testing():
    pass

read_dataset()