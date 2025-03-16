from pathlib import Path
from wordsegment import load,segment
import csv

path = Path(__file__).parent.parent / "cleaned/CatData.csv"

with path.open() as f:
    data = list(csv.reader(f))

load()

segmented = []
for rows in data:
    seg = segment(str(rows[1]).lower())

    if len(seg) == 1:
        #segmentation failed and we will return later
        segmented.append(["fail",""])
    else:
        segmented.append(seg)

endings = set([x[1] for x in segmented])
endings.add("song")
for i in range(len(segmented)):
    if segmented[i][0] == "fail":
        for ends in list(endings):
            if str(data[i]).endswith(str(ends)):
                segmented[i] = [ str(data[i][1]).replace(ends, ""), str(ends)]
                break

print([x for x in segmented if x[1] == ""])


# fail = [x for x in segmented if len(x) == 1]
# segmented = [i for i in segmented if i not in fail]
# endings = set([x[1] for x in segmented])


# failsICanHandle = [x[0] for x in fail if any(elem in x[0] for elem in list(endings))]
# fail = [x for x in fail if x[0] not in failsICanHandle]

# test = []
# for names in failsICanHandle:
#     for ends in list(endings):
#         if str(names).endswith(ends):
#             test.append(str(names).replace(ends, ""))
#             break
            

# print(segmented)