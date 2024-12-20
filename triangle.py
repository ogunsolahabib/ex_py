def equilateral(sides):
    if has_zeros(sides) or ineq_violation(sides):
        return False
    check= sides[0] == sides[1] == sides[2]
    return check


def isosceles(sides):
    sorted = sides.sort
    if has_zeros(sides) or ineq_violation(sides):
        return False
    dict = to_dict(sides)
    for key in dict:
        if dict[key] >= 2:
            return True
    return False
    


def scalene(sides):
    if has_zeros(sides) or ineq_violation(sides):
        return False
    dict= to_dict(sides)
    for key in dict:
        if dict[key] > 1:
            return False
    return True

def has_zeros(sides):
    for side in sides:
        if side==0:
            return True
    return False

def to_dict(sides):
    dict= {}
    for side in sides:
        if side in dict.keys():
            dict[side] = dict[side] + 1
        else:
            dict[side] = 1
    return dict

def ineq_violation(sides):
    sides.sort()
    if sides[0] + sides[1] < sides[2]:
        return True
    return False
