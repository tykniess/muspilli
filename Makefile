all:
	cat os.lexc > os-copy.lexc
	cat os-copy.lexc | sed s/'ë'/'e'/g | sed s/'ī'/'î'/g |sed s/'ē'/'ê'/g | sed s/'ō'/'ô'/g | sed s/'ā'/'â'/g | sed s/'ė'/'e'/g | sed s/'ū'/'û'/g > os.lexc
	hfst-lexc -v os.lexc -o os.lexc.hfst
	hfst-twolc os.twol -o os.twol.hfst
	hfst-compose-intersect -v -o os.gen.hfst os.lexc.hfst os.twol.hfst
	hfst-invert -v os.gen.hfst -o os.mor.hfst	
	hfst-fst2strings os.mor.hfst --xfst obey-flags | sort | sed 's/:/ /g'|sed 's/</ </'g | sed 's/>/> /g' > forms.txt
	python3 coverage.py	
