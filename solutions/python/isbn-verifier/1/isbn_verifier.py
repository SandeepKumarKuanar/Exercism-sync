def is_valid(isbn):
    cleaned_code = isbn.lower()
    net = []
    to_be_decided = 0
    testing = 10
    for number in cleaned_code:
        if number == 'x' and cleaned_code[-1] == 'x':
            net.append(10)
        elif number == '-':
            continue
        elif number.isnumeric():
            net.append(int(number))
        else:
            break

    for multiplier in range(len(net), 0, -1):
        to_be_decided += net[multiplier * -1] * testing
        testing -= 1

    if len(net) == 10:
        return to_be_decided % 11 == 0
    else:
        return False