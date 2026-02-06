def equilateral(sides):
    ## they are giving us a list of sides
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if sum(sides) == 0:
        return False
    elif a == b and b == a and a == c:
        if a + b >= c and a + c >= b and c + b >= a:
            return True
        else:
            return False
    else:
        return False


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if sum(sides) == 0:
        return False
    elif a == b or b == c or c == a:
        if a + b >= c and a + c >= b and c + b >= a:
            return True
        else:
            return False 
    else:
        return False


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if sum(sides) == 0:
        return False
    elif a != b and b != c and c != a:
        if a + b >= c and a + c >= b and c + b >= a:
            return True
        else:
            return False
    else:
        return False
