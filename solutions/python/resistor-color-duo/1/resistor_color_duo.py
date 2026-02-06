def value(colors):
    codes = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }
    #list_codes = colors.split("-")
    value_of_resistance = ''
    for color in colors:
        if colors.index(color) == 2:
            continue
        value_of_resistance += str(codes[color])

    return int(value_of_resistance)