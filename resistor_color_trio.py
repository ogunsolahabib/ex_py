# https://exercism.org/tracks/python/exercises/resistor-color-trio

PREFIXES = ["", "kilo", "mega", "giga"]
COLOR_LIST = [
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
def label(colors):
    
    digits = str(COLOR_LIST.index(colors[0])) + str(COLOR_LIST.index(colors[1]))
    zero_count= COLOR_LIST.index(colors[2])
    print(int(digits), zero_count)
    # move any additional zeros from digits to zero_count
    while len(digits) and digits[-1] == "0":
        digits = digits[:-1]
        zero_count += 1
    prefix = PREFIXES[zero_count // 3]
    for x in range(zero_count % 3):
        digits+= "0"
    return str(int(digits)) + " " + prefix + "ohms"
