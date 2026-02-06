def steps(number):
    N = number
    step = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    while N != 1 and step < 1000:
        if N % 2 == 0:
            N /= 2
            step += 1
        else:
            N *= 3
            N += 1
            step += 1

    return step
    