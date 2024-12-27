# https://exercism.org/tracks/python/exercises/resistor-color-expert

BANDS = {
    "grey" : "0.05%",
    "violet" : "0.1%",
    "blue" : "0.25%",
    "green" : "0.5%",
    "brown" : "1%",
    "red" : "2%",
    "gold" : "5%",
    "silver" : "10%"
}

COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
]

MULTIPLIERS = ["", "kilo", "mega", "giga"]

def resistor_label(colors):
    
    tolerance=""
    zero_count=0
    digits = ""
    prefix_index= 0
    
    # check if colors are up to 4 or 5
    if len(colors) > 3:
        tolerance = BANDS[colors.pop()]
        zero_count = COLORS.index(colors.pop())


    for x in colors:
        digits += str(COLORS.index(x))

    
    for x in range(zero_count):
        digits += "0"
    
    while len(str(int(digits))) > 3: # use int here to ignore digits after the decimal point

        # use float instead of int to keep accurate decimal value
        digits  = float(digits) / 1000
        prefix_index += 1


    prefix = MULTIPLIERS[prefix_index]

    # append symbol to tolerance substring
    if tolerance:
        tolerance = " ±" + tolerance


    digits = float(digits)

    if digits.is_integer():
        digits = int(digits)

    digits = str(digits)

    return digits + " " + prefix + "ohms" + tolerance
