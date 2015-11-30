import json
import time
import re

a = open('Creature_Data2.txt','w')
b = open('Not Included.txt','w')
c = open('Creature_Cata_Arff_New.arff','w')

with open('AllCards-x.json', encoding='utf-8') as infile:
    magicdb = json.load(infile)


a.write('Name' + '\t' + 'Type' + '\t' + 'Subtype' + '\t' + 'CMC' + '\t' + 'Colors' + '\t'+ 'Power' + '\t' + 'Toughness' + '\t' + 'Text' + '\t' + 'Sets' + '\n')
id=0
datalist = []
for cards in magicdb:
    try:
        if ('Creature' in magicdb[cards]['type']) and (('UNG' not in magicdb[cards]['printings']) or ('UNH' not in magicdb[cards]['printings']) or ('pHHO' not in magicdb[cards]['printings'])):
            m = magicdb[cards]
            card=''
            arff_line=''
            id+=1
            arff_line+=str(id)+','
            
            card=m.get('name','No-name') + '\t'
            card+=str(m.get('types','No-Type')) + '\t'
            card+=str(m.get('subtypes','No-sub-type')) + '\t'
            try:
                card+=str(m['cmc']) + '\t'
                arff_line+=str(m['cmc'])+','
            except:
                b.write(m['name'] + 'No CMC- not included...' + '\n')
                continue
            card+=str(m.get('colors','colorless')) + '\t'
            if 'Red' in m.get('colors','colorless'):
                isRed=1
            else:
                isRed=0
            if 'Blue' in m.get('colors','colorless'):
                isBlue=1
            else:
                isBlue=0
            if 'Green' in m.get('colors','colorless'):
                isGreen=1
            else:
                isGreen=0
            if 'Black' in m.get('colors','colorless'):
                isBlack=1
            else:
                isBlack=0
            if 'White' in m.get('colors','colorless'):
                isWhite=1
            else:
                isWhite=0
            if m.get('colors','colorless') == 'colorless':
                isColorless=1
            else:
                isColorless=0
            try:
                if '*' in m['power']:
                    card+='0\t'
                    power=0
                else:
                    card+=str(m['power']) + '\t'
                    power = m['power']
            except KeyError:
                b.write(m['name'] + 'No Power- not included...' + '\n')
                continue
            try:
                if '*' in m['toughness']:
                    card+='0\t'
                    toughness=0
                else:
                    card+=str(m['toughness']) + '\t'
                    toughness=m['toughness']
            except KeyError:
                b.write(m['name'] + 'No Toughness- not included...' + '\n')
                continue
            card+=m.get('text','NA').replace('\n',' ') + '\t'
            reg_flying=re.compile("Flying")
            if reg_flying.search(m.get('text','NA')):
                isFlying=1
            else:
                isFlying=0

            reg_vannila=re.compile("NA")
            if reg_vannila.search(m.get('text','NA')):
                isVanilla=1
            else:
                isVanilla=0

            reg_trample=re.compile("Trample")
            if reg_trample.search(m.get('text','NA')):
                isTrample=1
            else:
                isTrample=0

            reg_morph=re.compile("Morph")
            if reg_morph.search(m.get('text','NA')):
                isMorph=1
            else:
                isMorph=0

            reg_haste=re.compile("Haste")
            if reg_haste.search(m.get('text','NA')):
                isHaste=1
            else:
                isHaste=0

            reg_Strike=re.compile("strike")
            if reg_Strike.search(m.get('text','NA')):
                isStrike=1
            else:
                isStrike=0

            card+=str(m['printings']) + '\n'
            a.write(card)
            arff_line+=str(power)+','+str(toughness)+','+str(isRed)+','+str(isBlue)+','+str(isGreen)+','+str(isBlack)+','+str(isWhite)+','+str(isColorless)+','+str(isVanilla)+','+str(isFlying)+','+str(isTrample)+','+str(isMorph)+','+str(isHaste)+','+str(isStrike)
            datalist.append(arff_line)
    except:
        print(magicdb[cards]['name'] + ' failed')



c.write('% Magic Creature Cards\n% UNH/UNG/pHHO Removed\n% Source: AllCards-x.json @ mtgjson.com\n% \n% Machine Learning Project - Sam Cumings / David Burks\n% Set Downloaded 15.10.25\n\n')

c.write('@RELATION CMC\n\n')
c.write('@ATTRIBUTE Id NUMERIC\n')
c.write('@ATTRIBUTE cmc NUMERIC\n')
c.write('@ATTRIBUTE power NUMERIC\n')
c.write('@ATTRIBUTE toughness NUMERIC\n')
c.write('@ATTRIBUTE isRed NUMERIC\n')
c.write('@ATTRIBUTE isBlue NUMERIC\n')
c.write('@ATTRIBUTE isGreen NUMERIC\n')
c.write('@ATTRIBUTE isBlack NUMERIC\n')
c.write('@ATTRIBUTE isWhite NUMERIC\n')
c.write('@ATTRIBUTE isColorless NUMERIC\n')
c.write('@ATTRIBUTE isVanilla NUMERIC\n')
c.write('@ATTRIBUTE isFlying NUMERIC\n')
c.write('@ATTRIBUTE isTrample NUMERIC\n')
c.write('@ATTRIBUTE isMorph NUMERIC\n')
c.write('@ATTRIBUTE isHaste NUMERIC\n')
c.write('@ATTRIBUTE isStrike NUMERIC\n')


c.write('@DATA\n')

for line in datalist:
    c.write(line+'\n');

a.close()
b.close()
c.close()

