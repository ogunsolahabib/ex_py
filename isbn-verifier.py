# https://exercism.org/tracks/python/exercises/isbn-verifier

def is_valid(isbn):
    # remove hyphens
    digits= isbn.replace("-","")

    # invalidate if length != 10
    if len(digits) != 10:
        return False

    digits = list(digits)

    # invalidate if last character is non-numeric or not "X"
    if digits[-1].isnumeric() == False and digits[-1] != "X":
        return False

    # change last X to 10
    if digits[-1] == 'X':
        digits[-1] = "10"
        
    sum_of_prods= 0
    for i in range(10, 0, -1): # range 10,9,8,...,1
        if digits[10-i].isnumeric() == False:
            return False
        # digits[10-i] * i means digit[0]*9, digit[1]*8, .... 
        sum_of_prods += int(digits[10-i]) * i

    if sum_of_prods % 11 != 0:
        return False
    return True
        
