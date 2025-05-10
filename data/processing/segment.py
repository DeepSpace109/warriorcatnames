from pathlib import Path
from wordsegment import load,segment
import csv

path = Path(__file__).parent.parent / "cleaned/CatData.csv"

with path.open() as f:
    data = list(csv.reader(f))


load() #loads segmentation

segmented = []
for rows in data:
    seg = segment(str(rows[1]).lower()) #segments everything in lower-case

    if len(seg) == 1:
        #segmentation failed and we will return later
        segmented.append(["fail",""])
    else:
        segmented.append(seg)

endings = set([x[1] for x in segmented])
endings.add("song")
endings.add("star")
endings.add("throat")
endings.add("watcher")
endings.add("beam")
endings.add("briar")
endings.add("fish")

for i in range(len(segmented)):
    if segmented[i][0] == "fail":
        for ends in list(endings)[1:]:
            if str(data[i][1]).endswith(str(ends)):
                segmented[i][0] = str(data[i][1]).lower()[:-len(ends)]
                segmented[i][1] = str(ends)
                break

for x in range(len(segmented)):
    if segmented[x][0] == "fail":
        print(data[x])


writePath = Path(__file__).parent.parent / "cleaned/names.csv"

with open(writePath,mode= "w") as f:
    for row in segmented: 
        if row[0] == "fail" or row[0] == "r" or row[0] == "t": # remove known errors
            f.write(f"\n")
            continue
        f.write(f"{row[0]}, {row[1]}\n")
        #TODO replace "-" with " " to get rid of those stupid "black-and-white" descriptors