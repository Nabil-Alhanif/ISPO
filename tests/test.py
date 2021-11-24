import json

f = open('tests/test.json')

data = json.load(f)

for i in data:
    print(i)
