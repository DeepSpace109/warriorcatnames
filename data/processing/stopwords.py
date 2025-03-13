from pathlib import Path
import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

path = Path(__file__).parent.parent / "cleaned/CatData.csv"
writePath = Path(__file__).parent.parent / "cleaned/tags.csv"
with path.open() as f:
    data = list(csv.reader(f))


stop_words = set(stopwords.words('english'))
stop_words.add('tom')
stop_words.add('she-cat')
stop_words.add(',')
for names in set([row[1] for row in data]):
    stop_words.add(names.lower())

for rows in data:
    rows[-1] = [w for w in word_tokenize(rows[-1]) if not w.lower() in stop_words]

print(rows)

with open(writePath,mode= "w") as f:
    for row in data:
        f.write(f"{row[0]}, {row[1]}, {row[2]}, {', '.join(row[3])} \n")
