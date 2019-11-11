cat hel.txt | gsed s/'[^a-zA-ZâêîôûÎÊÂÔÛëđƀĐËīēōāĪĒŌĀŪ]'/'\n'/g | gsed -e 's/\(.*\)/\L\1/' | sort | uniq -c | sort -rn

