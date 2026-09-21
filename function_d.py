def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    current_max = numbers[0]
    for number in numbers:
        if number > current_max:
            current_max = number

    return current_max


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
