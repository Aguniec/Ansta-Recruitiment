import numpy as np
from decimal import Decimal


def postal_codes_generator(first_code, last_code):
    """ Generate a list of postal codes between two given codes """
    first_number = string_format(first_code)
    last_number = string_format(last_code)
    list_of_postal_codes = []
    for number in range(first_number, last_number):
        postal_code = str(number)
        list_of_postal_codes.append((postal_code[0:2] + "-" + postal_code[2:]))
    return list_of_postal_codes


def string_format(code):
    """ Format postal code to number """
    postal_code_list = code.split("-")
    postal_number = int("".join(postal_code_list))
    return postal_number


def numbers_not_in_array(arr, number):
    """ Returns a list of numbers that are not in an array with the length of the given number"""
    all_numbers = set(([i for i in range(1, number + 1)]))
    given_numbers = set(arr)
    return list((all_numbers | given_numbers) - (all_numbers & given_numbers))


def decimal_list(first_number, last_number):
    """ Returns a list of decimal numbers with stride of 0.5"""
    return np.arange(Decimal(first_number), Decimal(last_number+0.5), Decimal(0.5))


print(postal_codes_generator("79-900", "80-155"))
print(numbers_not_in_array([2, 3, 7, 4, 9], 10))
print(decimal_list(2.0, 5.5))
