import csv
import sys
import random

heliand_words  = []
muspilli_words = []
covered_words  = []

heliand = 'heliand/hel-tokens.txt'
muspilli= 'forms.txt'

with open(muspilli, 'r', newline='\n') as mfile:
    reader=csv.reader(mfile, delimiter='\t')
    for row in reader:
        muspilli_words.append(row[0].strip())

with open(heliand, 'r', newline='\n') as hfile:
    for row in hfile:
        heliand_words.append(row.strip())

for token in heliand_words:
    if token.lower() in muspilli_words:
        covered_words.append(token)

coverage = str(round((len(covered_words)/len(heliand_words)*100),3))

print("\nThere are "+str(len(heliand_words))+" unique tokens in the Hêliand.")
print("Project Muspilli currently contains "+str(len(muspilli_words))+" synthetically-generated forms.")
print("Of the "+str(len(heliand_words))+" unique tokens in the Hêliand, Project Muspilli contains " +\
      str(len(covered_words)) + " forms, or "+str(coverage)+"%. Wow!\n") 

with open('README.md', 'w') as README:
	README.write("")

with open('README.md', 'a') as README:
        README.write("""Introducing Muspilli, a Finite-State Transducer for the Old Saxon language.\nBuilt on the framework of Helsinki Finite-State Technologies (HFST) using Köbler's Old Saxon Dictionary.\nCurrent output forms are in forms.txt\n\n
""")

with open('README.md', 'a') as README:
    README.write("There are "+str(len(heliand_words))+" unique tokens in the Hêliand.\nProject Muspilli currently contains "+str(len(muspilli_words))+" synthetically-generated forms.\n'")
    README.write("Of the "+str(len(heliand_words))+" unique tokens in the Hêliand, Project Muspilli contains " + str(len(covered_words)) + " forms, or ")
    README.write(str(coverage)+"%. Wow!\n")
