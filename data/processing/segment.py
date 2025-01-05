from pathlib import Path
from wordsegment import load,segment
import csv

path = Path(__file__).parent.parent / "cleaned/CatData.csv"

with path.open() as f:
    data = list(csv.reader(f))

load()
print(segment(data[-1][1]))
print(data[-1])