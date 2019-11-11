cat hel.txt | gsed s/'[^a-zA-ZâêîôûÎÊÂÔÛ]'/'\n'/g | gsed -e 's/\(.*\)/\L\1/' | sed s/' '/''/g | sort | uniq | hfst-lookup ../os.mor.hfst
