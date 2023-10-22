from random import random
from time import time

import numpy as np


def timer(func: callable) -> callable:
    """
    Decorator function that measures the execution time of a given function.
    Parameters:
    - func (callable): The function to be timed.
    Returns:
    - callable: A wrapped function that measures the execution time of the original function and prints the result.
    """
    def wrapper(*args):
        start_time = time()
        result = func(*args)
        end_time = time()
        print(f"Function {func.__name__} took {end_time - start_time:.5f} sec.")
        return result

    return wrapper


def is_correct_list(the_list: list) -> bool:
    """
    Checks if given list is has the correct format and contents .
    Args:
        the_list (list): The list to be checked.
    Returns:
        bool: True if the list is a correct list, False otherwise.
    """
    if not all(isinstance(e, (int, float)) for e in the_list) or len(the_list) < 2:
        return False
    return True


@timer
def sort_descending_imperative(the_list: list) -> list:
    """
    Sorts given list in descending order using imperative approach.
    Args:
        the_list (list): List to be sorted.
    Returns:
        list: Sorted list in descending order.
    Raises:
        ValueError: If given list is not in correct format.
    """
    if not is_correct_list(the_list):
        raise ValueError("Unable to sort the list!")
    n = 0
    while n < len(the_list) - 1:
        if the_list[n] < the_list[n + 1]:
            the_list[n], the_list[n + 1] = the_list[n + 1], the_list[n]
            if n != 0:
                n -= 1
        else:
            n += 1
    return the_list


@timer
def sort_descending_declarative(the_list: list) -> list:
    """
    Sorts given list in descending order using declarative approach.
    Args:
        the_list (list): List to be sorted.
    Returns:
        list: Sorted list in descending order.
    Raises:
        ValueError: If given list is not in correct format.
    """
    if not is_correct_list(the_list):
        raise ValueError("Unable to sort the list!")
    np.repeat(np.arange(1 + max(the_list)), np.bincount(the_list))
    return the_list


# my_list = ['a', 5, 7, 9]  # try with non-numeric values
# my_list = []              # try with empty list
my_list = [random() for _ in range(10000)]

sort_descending_imperative(my_list)
print(f'Imperatively sorted list: {my_list}')

sort_descending_declarative(my_list)
print(f'Declaratively sorted list: {my_list}')
