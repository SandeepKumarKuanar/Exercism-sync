def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    def factors(num: int) -> list[int]:
        list_of_factors = [divisor for divisor in range(1, num) if num % divisor == 0]
        return list_of_factors

    aliquot_sum = sum(factors(number))
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"
