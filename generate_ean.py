from random import randrange


def generate_12_random_numbers():
    numbers = []
    for x in range(12):
        numbers.append(randrange(10))
    return numbers


def calculate_checksum(ean):
    """
    Calculates the checksum for an EAN13
    @param list ean: List of 12 numbers for first part of EAN13
    :returns: The checksum for `ean`.
    :rtype: Integer
    """
    assert len(ean) == 12, "EAN must be a list of 12 numbers"
    sum_ = lambda x, y: int(x) + int(y)
    evensum = reduce(sum_, ean[::2])
    oddsum = reduce(sum_, ean[1::2])
    return (10 - ((evensum + oddsum * 3) % 10)) % 10


def getnumber():
    numbers = generate_12_random_numbers()
    numbers.append(calculate_checksum(numbers))
    bar = ''.join(map(str, numbers))
    return bar
