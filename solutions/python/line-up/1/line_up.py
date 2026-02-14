def line_up(name, number):
    ordinal = ""
    ordinal += str(number)
    if number % 20 == 1 and number != 11:
        ordinal += "st"
    elif number % 20 == 2 and number != 12:
        ordinal += "nd"
    elif number % 20 == 3 and number != 13:
        ordinal += "rd"
    else:
        ordinal += "th"
    return f"{name}, you are the {ordinal} customer we serve today. Thank you!"
