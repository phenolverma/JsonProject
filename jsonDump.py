import json

infile = open(r'./file.json')

data = json.load(infile)

print(data)

outfile = open(r'simpleback.json', 'w')

json.dump(data, outfile, indent=0)
outfile.close()