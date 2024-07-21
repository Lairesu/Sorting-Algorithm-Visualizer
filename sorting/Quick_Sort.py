from scripts.utilis import Draw_list
from scripts.Constants import *

def quick_sort(draw_info, ascending=True):
    lst = draw_info.lst
    yield from quick_sort_recursion(draw_info, lst, 0, len(lst) - 1, ascending)

def quick_sort_recursion(draw_info, lst, low, high, ascending):
    if low < high:
        pivot_index = yield from partition(draw_info, lst, low, high, ascending)

        # Recursively sort elements before and after the pivot
        yield from quick_sort_recursion(draw_info, lst, low, pivot_index - 1, ascending)
        yield from quick_sort_recursion(draw_info, lst, pivot_index + 1, high, ascending)

def partition(draw_info, lst, low, high, ascending):
    """
    We set a variable i to be one less than the starting index low.
    This helps us keep track of where to put the numbers smaller than the pivot.
    """

    pivot = lst[high]
    i = low - 1

    Draw_list(draw_info, {high: COLOR["blue"]}, True)  # Highlight pivot
    yield True

    for j in range(low, high):
        """
        If the number is smaller than the pivot (or larger if sorting in descending order),
        we move it to the left side.
        We do this by swapping it with the element at i+1.
        We highlight the numbers being swapped in green and red.
        """
        if (lst[j] < pivot and ascending) or (lst[j] > pivot and not ascending):
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
            Draw_list(draw_info, {i: COLOR["green"], j: COLOR["red"]}, True)  # Highlight swapping elements
            yield True

    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    Draw_list(draw_info, {i + 1: COLOR["green"], high: COLOR["blue"]}, True)  # Final swap with pivot
    yield True

    return i + 1

