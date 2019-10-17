all:
	hfst-lexc os.lexc -o os.lexc.hfst
	hfst-twolc os.twol -o os.twol.hfst
	hfst-compose-intersect -1 os.lexc.hfst -2 os.twol.hfst -o os.gen.hfst



