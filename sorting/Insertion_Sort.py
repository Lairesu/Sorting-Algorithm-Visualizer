from scripts.utilis import Draw_list
from scripts.Constants import *

def insertion_sort(draw_info, ascending = True):
    lst = draw_info.lst
    for i in range(1, len(lst)):
        current = lst[i]
        j = i
        while True:
            ascending_sort = j > 0 and lst[j-1] > current and ascending
            descending_sort = j > 0 and lst[j-1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[j] = lst[j-1]
            j =  j - 1
            lst[j] = current
            Draw_list(draw_info,{i: COLOR["green"], i-1: COLOR["red"]}, True)
            yield True

    return lst
    

