def square_of_sum(number):
    net = 0
    for num in range(1, number + 1):
        net += num
    return net**2


def sum_of_squares(number):
    net = 0
    for num in range(1, number + 1):
        net += num**2
    return net


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
