import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import operator
import re

df = pd.read_csv('whatsapp-group-data.csv', index_col=0)

words_dict = {}
ignore_words = ['', 'the', 'you', 'too', 'i', 'is', 'and', 'it', 'a', 'this', 'in', \
                    'of', 'for', 'that', 'are', 'not', 'your', 'they', 'have', 'im', \
                    'be', 'me', 'on', 'to', 'its', 'how', 'just', 'we', 'but', \
                    'my', 'so', 'oh', 'o', 'now', 'u', 'at', 'there', 'youre', 'do', \
                    'or', 'then', 'go', 'am', 'oo', 'can', 'which', 'will', 'as', 'was', \
                    'from', 'those']

for index, row in df.iterrows():
    words = row['text'].split(' ')
    for word in words:
        word = word.lower()
        word = re.sub('[^a-z]+', '', word) # allow only letters

        if word in ignore_words:
            break

        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

words = sorted(words_dict.items(), key=operator.itemgetter(1), reverse=True)

print(words[:100])