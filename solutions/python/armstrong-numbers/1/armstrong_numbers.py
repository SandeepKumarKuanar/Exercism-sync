def is_armstrong_number(number):
    digits = list(str(number))
    raised = [int(i)**len(digits) for i in digits]

    return bool(sum(raised) == number)
