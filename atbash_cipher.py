# https://exercism.org/tracks/python/exercises/atbash-cipher

ALPHABET = [chr(one) for one in range(97,123)]

def encode(word):
    word= word.lower()
    res = ""
    for x in word:
        entry = ""
        if x.isalnum():

            if x in ALPHABET:
                entry = ALPHABET[len(ALPHABET) - 1 - ALPHABET.index(x)]
           
            elif x.isnumeric():
                entry = x
    
            size = len("".join(res.split(" ")))
                
            if size >= 5 and size % 5 == 0:
                entry = " " + entry
           
        res += entry
       
    return res

def decode(word):
    res = ""
    for x in word:
        entry = ""
        if x.isalnum():
            if x in ALPHABET:
                entry= ALPHABET[len(ALPHABET) - ALPHABET.index(x) - 1]
            if x.isnumeric():
                entry= x
        res +=entry
        
    return res
    
