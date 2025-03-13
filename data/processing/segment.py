from pathlib import Path
from wordsegment import load,segment
import csv

path = Path(__file__).parent.parent / "cleaned/CatData.csv"

with path.open() as f:
    data = list(csv.reader(f))

load()

segmented = []
for rows in data:
    segmented.append(segment(rows[1]))

fail = [x for x in segmented if len(x) == 1]
segmented = [i for i in segmented if i not in fail]
endings = set([x[1] for x in segmented])


failsICanHandle = [x[0] for x in fail if any(elem in x[0] for elem in list(endings))]
fail = [x for x in fail if x[0] not in failsICanHandle]

test = []
for names in failsICanHandle:
    for ends in list(endings):
        temp = names.split(ends)
        if len(temp) == 2:
            test.append(temp)
            break

print(list(endings))
print(test)