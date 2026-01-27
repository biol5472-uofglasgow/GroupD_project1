import json

with open ("results.tsv", "r") as f:
    data = json.load(f)
print(data)
print(type(data))    

#can include tool version?