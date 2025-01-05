from pathlib import Path
import csv
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

path = Path(__file__).parent.parent / "cleaned/CatData.csv"

with path.open() as f:
    data = list(csv.reader(f))

stop_words = set(stopwords.words('english'))
stop_words.add('tom')
stop_words.add('she-cat')

testsen = data[-1][-1]
print([w for w in word_tokenize(testsen) if not w.lower() in stop_words])

