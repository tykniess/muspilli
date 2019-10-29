import sys
#suffix = 'ian'     #used for 1st class weak verbs
#suffix = 'an'   #2nd class weak verbs
suffix = 'an' #strong verbs
verb_class = '1'
delineating_characters = [',','*']
encoded_forms = []

with open(sys.argv[1], 'r') as to_read: #open filename
#gihôrian, gi-hô-r-ian, as., sw. V. (1a): nhd. hören, gehorchen, gehören
#mîthan%<v%>%<str%>%<class1%>:mî STR1-TH-STEM   ;        !"avoid"
    for line in to_read:
        i = 0
        while line[i] not in delineating_characters:
            i = i + 1
        stem = line[0:i-len(suffix)]
        for char in line:
            j = 0
            while line[j] != ':':
                j = j + 1
        gloss = line[j+1:]
#        encoded_forms.append(stem+suffix+'%<v%>:'+stem+' WK1    ;	!' + gloss)
#        encoded_forms.append(stem+suffix+'%<v%>:'+stem+' WK2    ;	!' + gloss)
        if stem[-2:] == 'th':
            encoded_forms.append(stem+suffix+'%<v%>%<str%>%<class' +\
                             str(verb_class) + '%>:'+stem[:-2]+\
                             ' STR1-TH-STEM    ;	!' + gloss)
        else:
            encoded_forms.append(stem+suffix+'%<v%>%<str%>%<class' +\
                             str(verb_class) + '%>:'+stem+\
                             ' STR1    ;	!' + gloss)


for form in encoded_forms:
    with open('to_import.txt','a+') as to_write:
        to_write.write(form)



#this failed to accurately parse holon
