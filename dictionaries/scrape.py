import sys
##print ("This is the name of the script: ", sys.argv[0])
##print ("Number of arguments: ", len(sys.argv))
##print ("The arguments are: " , str(sys.argv))

lemmas = []
lemmas_cleaned = []
definitions = []
nums = ['1','2','3','4','5','6','7','8','9','0']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','k','l','m','n','o',
            'p','q','r','s','t','u','v','w','x','y','z', 'đ', 'ƀ',
            'ā','â','ā',
            'ê','ė', 'ē',
            'ô','ō',
            'ū','û',
            'ī','î']
neut_a_light = ['agu','alu','adu','oru','uru','atu','ibu','iƀu','etu','apu','epu','ipu','ilu']

POS_tags = ['as., st. V. (1)', 'as., st. V. (2)', 'as., st. V. (3a)', 'as., st. V. (3b)', 'as., st. V. (4)', 'as., st. V. (5)', 'as., st. V. (6)', 'as., st. V. (7)', \
'as., sw. V. (1a)', 'as., sw. V. (1b)', 'as., sw. V. (2)', \
'as., red. V.',\
            'as., st. M. (a)', 'as., st. N. (a)', 'as., st. M. (ja)', 'as., st. N. (ja)', 'as., st. M. (wa)', 'as., st. N. (wa)']

def dict_scrape(POS, dictionaryfile='as_kurzform.txt'):
    """Scrapes a dictionary for a given part of speech. POS tags in POS_tags.

    POS(str), dictionaryfile(str-of-filename) -> list-of-strings
    """
    if POS in POS_tags:
        with open(dictionaryfile, 'r') as to_scrape:
            for line in to_scrape:
                if POS in line:
                    lemmas.append(line)
    #cleaning
    for line in lemmas:
        i=0
        for char in line[:20]:
            if char == "*" or char == " ":
                break
            else:
                i=i+1
        lemmas_cleaned.append(line[:i].lower().strip().replace('*','').replace('?','')+'\n')
        #scrub line of the frequency data, begin with headword?
    return lemmas_cleaned

dict_scrape(sys.argv[1])

###encode masculine a-stem nouns for LEXICON:
##with open(POS[5:]+'_ready-for-import','w+') as to_write:
##    i=0
##    for line in lemmas_cleaned:
##        to_write.write(line[:-1]+"%<noun%>%<masc%>%<a-stem%>:"+line[:-1]+\
##                       " Masc-A-Stem ; ! \n")

###encode neuter a-stem nouns for LEXICON, accounting for syllable weight:
##with open('st. N. (a)_ready-for-import','w+') as to_write:
##    i=0
##    while i < len(lemmas):
##        to_write.write(lemmas_cleaned[i][:-1] + '%<noun%>%<neut%>%<a-stem%>:'+lemmas_cleaned[i][:-1]+' Neut-A-Stem ; ! ' + lemmas[i].replace('\n','') + '\n')    
##        i=i+1

#encode masc ja-stem nouns for LEXICON, accounting for syllable weight:
##with open('st. M. (ja)_ready-for-import','w+') as to_write:
##    i=0
##    while i < len(lemmas):
##        to_write.write(lemmas_cleaned[i][:-1] + '%<noun%>%<masc%>%<ja-stem%>:'+lemmas_cleaned[i][:-2]+' Masc-Ja-Stem \t\t; ! ' + lemmas[i].replace('\n','') + '\n')    #note the -2, this is to remove the i ending
##        i=i+1


#encode 'as., st. M. (ja)', account for syllable weight
##for lemma in lemmas_cleaned:
##    print (lemma[-2])
with open('st. N. (ja)_ready-for-import','w+') as to_write:
    i=0
    while i < len(lemmas):
        if lemmas_cleaned[i][-2] == 'i': #some (e.g. "net") end in something else, so check these first
            to_write.write(lemmas_cleaned[i][:-1] + '%<noun%>%<neut%>%<ja-stem%>:'+lemmas_cleaned[i][:-2]+' Neut-Ja-Stem \t\t; ! ' + lemmas[i].replace('\n','') + '\n')    #note the -2, this is to remove the i ending
        else:
            to_write.write(lemmas_cleaned[i][:-1] + '%<noun%>%<neut%>%<ja-stem%>:'+lemmas_cleaned[i][:-1]+' Neut-Ja-Stem \t\t; ! ' + lemmas[i].replace('\n','') + '\n')    #note the -1, this is to not remove the ending

        i=i+1


###encode 'as., st. M. (wa)'
##with open('st. M. (wa)_ready-for-import','w+') as to_write:
##    i=0
##    while i < len(lemmas):
##        to_write.write(lemmas_cleaned[i][:-1] + '%<noun%>%<masc%>%<wa-stem%>:'+lemmas_cleaned[i][:-2]+' Masc-Wa-Stem \t\t; ! ' + lemmas[i].replace('\n','') + '\n')    #note the -2, this is to remove the i ending
##        i=i+1

##with open('st. N. (wa)_ready-for-import','w+') as to_write:
##    i=0
##    while i < len(lemmas):
##        to_write.write(lemmas_cleaned[i][:-1] + '%<noun%>%<neut%>%<wa-stem%>:'+lemmas_cleaned[i][:-2]+' Neut-Wa-Stem \t\t; ! ' + lemmas[i].replace('\n','') + '\n')    #note the -2, this is to remove the i ending
##        i=i+1
