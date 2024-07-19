from scripts.utilis import Draw_list
from scripts.Constants import *

def merge_sort(draw_info, ascending=True):
    lst = draw_info.lst
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left_half = merge_sort_inner(lst[:mid], ascending=ascending)
    right_half = merge_sort_inner(lst[mid:], ascending=ascending)
    
    left_index = 0
    right_index = 0
    sorted_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if (left_half[left_index] < right_half[right_index] and ascending) or (left_half[left_index] > right_half[right_index] and not ascending):
            lst[sorted_index] = left_half[left_index]
            left_index += 1
        else:
            lst[sorted_index] = right_half[right_index]
            right_index += 1
        sorted_index += 1
        Draw_list(draw_info, {left_index: COLOR["green"], right_index: COLOR["red"]}, True)
        yield True

    while (left_index < len(left_half)):
        lst[sorted_index] = left_half[left_index]
        left_index += 1
        sorted_index += 1
        Draw_list(draw_info, {left_index: COLOR["green"]}, True)
        yield True

    while (right_index < len(right_half)):
        lst[sorted_index] = right_half[right_index]
        right_index += 1
        sorted_index += 1
        Draw_list(draw_info, {right_index: COLOR["red"]}, True)
        yield True

    return lst

def merge_sort_inner(lst, ascending=True):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left_half = merge_sort_inner(lst[:mid], ascending=ascending)
    right_half = merge_sort_inner(lst[mid:], ascending=ascending)

    left_index = 0
    right_index = 0
    sorted_list = []

    while left_index < len(left_half) and right_index < len(right_half):
        if (left_half[left_index] < right_half[right_index] and ascending) or (left_half[left_index] > right_half[right_index] and not ascending):
            sorted_list.append(left_half[left_index])
            left_index += 1
        else:
            sorted_list.append(right_half[right_index])
            right_index += 1

    sorted_list.extend(left_half[left_index:])
    sorted_list.extend(right_half[right_index:])
    
    return sorted_list
