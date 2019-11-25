import sys
from bs4 import BeautifulSoup
import re


soup = BeautifulSoup(open(sys.argv[1]), 'html.parser')

#doc=soup.find('div', {'class':'contentus'})

#text=doc.get_text()

text=soup.get_text()

text = re.sub('[0-9]+', '\1 ',text)

for c in '[|]':
	text=text.replace(c,'')

text=text.replace('{b}','ƀ').replace('{d}','đ').replace('. . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . ','').replace('Heliand','').replace('Fitte','').replace('______________________________________________________________________________','').replace('Die Evangelisten (Book of Kells, um  )','').replace('______________________________________________________________________________','').replace('<<< Übersicht  <<< vorige Seite','').replace('BIBLIOTHECA AUGUSTANA','').replace('nächste Seite >>>','').replace('bibliotheca Augustana','').replace('\num\n','').strip()
#text=" ".join(text.split())     #this optional step removes a lot of whitespace
print(text)



#call this on hel.txt

#####


#extra_symbols = ['(',')','[',']','{','}','{','}','1','2','3','4','5','6','7','8','9','10']

#text.replace().replace(.replace(.replace(.replace(.replace(.replace(

#print(text)
