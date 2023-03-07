import functools

def multiply_even_numbers(nums):
    """Multiply the even numbers.

        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48

        >>> multiply_even_numbers([3, 4, 5])
        4

    If there are no even numbers, return 1.

        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    # num for num in nums if num is even, add to that thing
    # reduce, sum in python
    even_nums = [num for num in nums if num % 2 == 0]

    if len(even_nums) == 0:
        return 1

    return functools.reduce(product, even_nums)


def product(x, y):
    return x * y