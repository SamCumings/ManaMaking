import time

a = open(time.strftime('%Y-%m-%d') + ' Creature_Data.arff','w')
cmclist = []
datalist = ['@DATA']

a.write('% Magic Creature Cards\n% UNH/UNG/pHHO Removed\n% Source: AllCards-x.json @ mtgjson.com\n% \n% Machine Learning Project - Sam Cumings / David Burks\n% Set Downloaded 15.10.25\n\n')

a.write('@RELATION CMC\n\n')
a.write('@ATTRIBUTE power NUMERIC\n')
a.write('@ATTRIBUTE toughness NUMERIC\n')

with open('Creature_Data.txt') as infile:
	next(infile)
	for line in infile:
		attributes = line.split('\t')
		cmc = ('CMC-' + str(attributes[3]))
		power = str(attributes[4])
		toughness = str(attributes[5])
		datalist.append(power + ',' + toughness + ',' + cmc)
		if cmc not in cmclist:
			cmclist.append(cmc)
			

			
a.write('@ATTRIBUTE class {' + ','.join(cmclist) + '}\n\n')

a.write('\n'.join(datalist))
#print(cmclist)
#print('\n'.join(datalist))
			
		

