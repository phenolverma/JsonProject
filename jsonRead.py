import json

infile = open(r'./file.json')

data = json.load(infile)

print(data)
print(data['101']['Salary'])

