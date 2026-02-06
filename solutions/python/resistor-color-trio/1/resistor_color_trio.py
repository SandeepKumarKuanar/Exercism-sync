def label(colors):
    dict_colors = {
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
    to_be_multiplied = 10 * int(dict_colors[colors[0]]) + int(dict_colors[colors[1]])
    powers_of_ten = 10 ** int(dict_colors[colors[2]])
    net = to_be_multiplied * powers_of_ten
    if net >= 10**9:
        return f"{int(net / 10**9)} gigaohms"
    if net >= 10**6:
        return f"{int(net / 10**6)} megaohms"
    elif net >= 10**3:
        return f"{int(net / 10**3)} kiloohms"
    return f"{net} ohms"