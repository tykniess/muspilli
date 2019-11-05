import sys
from bs4 import BeautifulSoup
import re


soup = BeautifulSoup(open(sys.argv[1]), 'html.parser')

doc=soup.find('div', {'class':'contentus'})

text=doc.get_text()

text = re.sub('[0-9]+', '\1 ',text)

for c in '{[|]}':
	text=text.replace(c,'')

print(text)

#extra_symbols = ['(',')','[',']','{','}','{','}','1','2','3','4','5','6','7','8','9','10']

#text.replace().replace(.replace(.replace(.replace(.replace(.replace(

#print(text)
