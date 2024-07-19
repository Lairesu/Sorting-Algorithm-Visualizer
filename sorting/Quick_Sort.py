def quick_sort(draw_info, ascending=True):
    lst = draw_info.lst
    
    def _quick_sort(lst, ascending):
        if len(lst) <= 1:
            return lst
        
        pivot = lst[0]
        left_partition = []
        right_partition = []

        for value in lst[1:]:
            if (ascending and value < pivot) or (not ascending and value > pivot):
                left_partition.append(value)
            else:
                right_partition.append(value)

        left_partition = _quick_sort(left_partition, ascending)
        right_partition = _quick_sort(right_partition, ascending)

        return left_partition + [pivot] + right_partition

    sorted_lst = _quick_sort(lst, ascending)
    for i in range(len(lst)):
        draw_info.lst = sorted_lst[:i+1] + lst[i+1:]
        yield
