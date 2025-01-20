from nltk.corpus import brown

def splitname(inputname):
    name = list(inputname)
    words = [words for words in brown.words() if (len(words) < 8 and len(words) > 2)]
    buffer = name[0] + name[1] 
    for x in range(2,len(name)):
        buffer = buffer + name[x]
        if buffer in words:
            if ''.join(name[x+1:]) in words:
                return [buffer, ''.join(name[x+1:])]
            
print(splitname("tornear"))