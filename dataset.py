import subprocess, os
from pathlib import Path
import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordsegment import load,segment
from pprint import pprint
from splitname import splitname


def dataset():
    path = Path(__file__).parent / "data/cleaned/CatData.csv"
  
    with path.open() as f:
        data = list(csv.reader(f))

    #extend stopwords
    stop_words = stopwords.words('english')
    new_stops = [i[1].lower() for i in data] + [
        "tom",
        "she-cat",
        ","
    ]
    stop_words.extend(new_stops)
    load()
    
    ##Data Preperation
    
    for rows in data[1:]:
        #segment
        rows[-1] = [w for w in word_tokenize(rows[-1]) if not w.lower() in stop_words]
        
        #split names
        try:
            prefix,suffix = segment(rows[1].lower())
            rows[1]=prefix
            rows.insert(2,suffix)
        except Exception as e:
            prefix,suffix = splitname(rows[1].lower())
            rows[1]=prefix
            rows.insert(2,suffix)

    pprint([rows for rows in data if rows[2] == "ERROR"])
    #split names
    






dataset()

