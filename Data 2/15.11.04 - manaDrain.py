import json

a = open('Creature_Data.txt','w')
b = open('Not Included.txt','w')

with open('AllCards-x.json', encoding='utf-8') as infile:
	magicdb = json.load(infile)
	
	
a.write('Name' + '\t' + 'Type' + '\t' + 'Subtype' + '\t' + 'CMC' + '\t' + 'Power' + '\t' + 'Toughness' + '\t' + 'Text' + '\t' + 'Sets' + '\n')
	
for cards in magicdb:
	try:
		if (('Creature' in magicdb[cards]['type']) and (('UNG' and 'UNH' and 'pHHO') not in magicdb[cards]['printings'])):
			try:
				m = magicdb[cards]
				a.write(m['name'] + '\t' + ' '.join(m['types']) + '\t' + ' '.join(m['subtypes']) + '\t' + str(m['cmc']) + '\t' + str(m['power']) + '\t' + str(m['toughness']) + '\t' + m['text'].replace('\n',' ') + '\t' + ' '.join(m['printings']) + '\n')
			except KeyError:
				a.write(m['name'] + '\t' + ' '.join(m['types']) + '\t' + ' '.join(m['subtypes']) + '\t' + str(m['cmc']) + '\t' + str(m['power']) + '\t' + str(m['toughness']) + '\t\t' + ' '.join(m['printings']) + '\n')
			except:
				b.write(m['name'] + ' not included...' + '\n')
	except:
		print(magicdb[cards]['name'] + ' failed')
		
a.close()
b.close()