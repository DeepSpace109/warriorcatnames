from pathlib import Path
import csv
import json

path = Path(__file__).parent.parent / "cleaned/CatData.csv"
tagspath = Path(__file__).parent.parent / "cleaned/tags.csv"
writepath = Path(__file__).parent.parent / "trainingdata/sample.jsonl"

with path.open() as f:
    names = list(csv.reader(f))[1:] #remove header

with tagspath.open() as f:
    tags = list(csv.reader(f))[1:] #remove header

print(tags)
data = []


a1 = {"role": "system", "content": "You will genrate a WarriorCats name based on the traits given. No other text should be present and names should be separated by a space" }
for i in range(len(names)):
    temp = {} # initialize temp dict
    a2 = { "role": "user", "content": str.join(" ", tags[i])} #what the user will give to you
    a3 = { "role": "assistant", "content": names[i][1]} #what it returns
    print(a1)
    print(a2)
    print(a3)
    data.append({"messages": [a1,a2,a3]})

print(len(data))

with open(writepath, 'w') as file:
    for entry in data:
        json_string = json.dumps(entry)
        file.write(json_string + '\n')