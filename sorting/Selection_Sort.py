from scripts.utilis import Draw_list
from scripts.Constants import *


def selection_sort(draw_info, ascending= True):
    lst =  draw_info.lst

    for i in range(len(lst)-1):
        min_index = i
        for j in range(i+1, len(lst)):
            if (lst[min_index] > lst[j] and ascending) or (lst[min_index] < lst[j] and  not ascending):
                min_index = j
                
        lst[i], lst[min_index] = lst[min_index], lst[i]
        Draw_list(draw_info, {i: COLOR["green"], min_index: COLOR["red"]}, True)
        yield True

    return lst