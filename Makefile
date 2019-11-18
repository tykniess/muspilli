all:
	cat os.lexc > os-copy.lexc
	cat os-copy.lexc | gsed s/'ë'/'e'/g | gsed s/'ī'/'î'/g |gsed s/'ē'/'ê'/g | gsed s/'ō'/'ô'/g | gsed s/'ā'/'â'/g | gsed s/'ė'/'e'/g | gsed s/'ū'/'û'/g > os.lexc
	hfst-lexc -v os.lexc -o os.lexc.hfst
	hfst-twolc os.twol -o os.twol.hfst
	hfst-compose-intersect -v -o os.gen.hfst os.lexc.hfst os.twol.hfst
	hfst-invert -v os.gen.hfst -o os.mor.hfst	
	hfst-fst2strings os.mor.hfst --xfst obey-flags | sort | gsed s/':'/'\t\t'/g|gsed s/'<'/'   <'/g | gsed s/'>'/'>   '/g > forms.txt
	python3 gi-prefix.py
	cat forms-prefixed.txt>forms.txt
	python3 coverage.py
