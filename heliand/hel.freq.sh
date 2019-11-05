cat hel.txt | gsed ' s/[^a-zA-Zîêôâīēōāëđƀ]\+/ /g' | gsed 's/ /\n/g' | grep -v '^$' | sort -f | uniq -c | sort -gr > hel.freq.txt
