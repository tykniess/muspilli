cat hel.txt | gsed ' s/[^a-zA-Zîêôâīēōāëđƀ]\+/ /g' | gsed 's/ /\n/g'
