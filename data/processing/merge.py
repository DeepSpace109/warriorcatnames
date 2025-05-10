from pathlib import Path
import csv
import json

pathname = Path(__file__).parent.parent / "cleaned/names.csv"
pathtag = Path(__file__).parent.parent / "cleaned/tags.csv"
writepath = Path(__file__).parent.parent / "trainingdata/sample.json"

with pathname.open() as f:
    names = list(csv.reader(f))[1:] #remove header

with pathtag.open() as f:
    tag = list(csv.reader(f))[1:]  #remove header   

data = []

assert (len(tag) == len(names)) , "Data Processing has resulted in a misalignment"

for i in range(len(names)):
    temp = {} # initialize temp dict
    if names[i] == []:
        continue
    if tag[i] == [] or tag[i] == "":
        temp = {"root": names[i][0],"suffix": names[i][1], "Tags": ""}
    else:
        temp = {"root": names[i][0],"suffix": names[i][1], "Tags": tag[i]}

    data.append(temp)

print(len(data))

with open(writepath, 'w') as file:
    for entry in data:
        json_string = json.dumps(entry)
        file.write(json_string + '\n')