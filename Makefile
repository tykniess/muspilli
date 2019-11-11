all:
	cat os.lexc > os-copy.lexc
	cat os-copy.lexc | gsed s/'ī'/'î'/g |gsed s/'ē'/'ê'/g | gsed s/'ō'/'ô'/g | gsed s/'ā'/'â'/g > os.lexc
	hfst-lexc os.lexc -o os.lexc.hfst
	hfst-twolc  os.twol -o os.twol.hfst
	hfst-compose-intersect -1 os.lexc.hfst -2 os.twol.hfst -o os.gen.hfst
	hfst-invert os.gen.hfst -o os.mor.hfst	
	hfst-fst2strings os.mor.hfst | sort | gsed s/':'/'    \t'/g|gsed s/'<'/'   <'/g | gsed s/'>'/'>   '/g > forms.txt
	python3 coverage.py

