import re

a = open('Output.txt','w')
chunk = ''
magicdict = {}

with open('MagicText.txt','r') as infile:
	for lines in infile:
		piece = re.sub(r'[^A-Za-z ]','', lines)
		chunk = piece.lower() + ' ' + chunk
		
list = chunk.split()
listnum = len(list)
p = 0
print(listnum)


a.write('Word\tCount\n')

for items in list:
	if items in magicdict:
		magicdict[items] += 1
	elif not items in magicdict:
		magicdict[items] = 1
		
for key, val in magicdict.items():
		a.write(key + '\t' + str(val) + '\n')