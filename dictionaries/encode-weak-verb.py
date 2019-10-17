import sys
suffix = 'ian'
encoded_forms = []

with open(sys.argv[1], 'r') as to_read: #open filename
    #gihôrian, gi-hô-r-ian, as., sw. V. (1a): nhd. hören, gehorchen, gehören
    #adêlian%<v%>:adêl WK1   ;	!"zuerkennen"
    for line in to_read:
        i = 0
        while line[i:i+3] != 'ian':
            i = i + 1
        stem = line[0:i]
        for char in line:
            j = 0
            while line[j] != ':':
                j = j + 1
        gloss = line[j:]
        encoded_forms.append(stem+suffix+'%<v%>:'+stem+' WK1    ;	!' + gloss)

for form in encoded_forms:
    with open('to_import.lexc','a+') as to_write:
        to_write.write(form)
