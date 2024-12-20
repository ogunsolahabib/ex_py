# vowels = ['a', 'e', 'i', 'o', 'u']

# def get_letters_before_first_vowel(text):
#     first_vowel=0

#     letters_before_first_vowel=""
    
#     for x in text:
#         if x in vowels:
#             first_vowel= text.index(x)
#             break
#     if first_vowel > 0:
#         letters_before_first_vowel = text[0:first_vowel]
#     return letters_before_first_vowel
        
    


# def is_rule1(text):
#     return text[0] in vowels
# def is_rule2(text):
#     letters_before_first_vowel= get_letters_before_first_vowel(text)
#     return letters_before_first_vowel != text and len(letters_before_first_vowel) != 0


# def is_rule3(text):
#     has_qu = "qu" in text
#     # letters_before_qu = list(text.split("qu")[0])
#     # vowels_before_qu= list(filter(lambda x: x in vowels, letters_before_qu))
#     # has_no_consonants_before_qu = len(vowels_before_qu) != 0
#     return has_qu

# def is_rule4(text):
#     has_y = "y" in text
    
#     cons_before_y = get_cons_before_y(text)

#     return has_y and len(cons_before_y) > 0

        
# def get_cons_before_y(text):
#     cons_before_y=""
#     letters_before_y= text.split("y")[0]
#     vowels_before_y = list(filter(lambda x: x in vowels, letters_before_y))
#     has_cons_before_y = len(vowels_before_y) == 0
#     if has_cons_before_y:
#         cons_before_y= letters_before_y
#     cons_before_y = "".join(cons_before_y)
#     return cons_before_y


# def translate(text):
#     words= text.split()
#     words = map(translate_word, words)
#     return " ".join(words)
    

# def translate_word(text):
#     first_letter = text[0]
  
#     if text.startswith("xr") or text.startswith("yt") or first_letter in vowels:
#         return text + "ay"
        
#     if is_rule3(text):
#         return text[text.index("qu")+2:]+ text.split("qu")[0] + "quay"
    
#     if is_rule2(text):
#         letters_before_first_vowel= get_letters_before_first_vowel(text)
#         return text[text.index(letters_before_first_vowel)+ len(letters_before_first_vowel):] + letters_before_first_vowel + "ay"
        
  
#     if is_rule4(text):
#         cons_before_y = get_cons_before_y(text)
#         return text[text.index("y"):] + cons_before_y + "ay"
    
        
           
#     return text








VOWELS= ["a", "e", "i", "o", "u"]

def is_rule1(text):
    return text[0] in VOWELS or text.startswith("xr") or text.startswith("yt")

def is_rule2(text):
    return text[0] not in VOWELS

def is_rule3(text):
    return "qu" in text and is_all_cons(letters_before_target(text, "qu"))

def is_rule4(text):
    before_target=letters_before_target(text, "y")
    return "y" in text and is_all_cons(before_target) and len(before_target) > 0
    
    
    

def translate(text):
    words = list(map(translate_word, text.split(" ")))
    return " ".join(words)
    
def translate_word(text):
    if is_rule1(text):
        return text + "ay"
    if is_rule4(text):
        return text[text.index("y"):]+letters_before_target(text, "y")+"ay"
    if is_rule3(text):
        # letters after qu + letters before qu + quay
        return text[text.index("qu")+2:] + letters_before_target(text, "qu") +"quay"
    if is_rule2(text):
        cons_before_first_vowel= get_cons_before_first_vowel(text)
        return text[len(cons_before_first_vowel):] + cons_before_first_vowel + "ay"


        

    
        
        
    
        



def get_cons_before_first_vowel(text):
     # find first vowel
    first_vowel = 0
    for x in text:
        if x not in VOWELS:
            first_vowel += 1
        else:
            break

    return text[0:first_vowel]

def is_all_cons(text):
    count=0
    for x in text:
        if x in VOWELS:
            return False
        else:
            count+=1
    return len(text) == count
    
def letters_before_target(text, target):
    return text.split(target)[0]
    




























    
    
