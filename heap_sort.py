def swap(i, j):                    
    unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i] 


def heapify(end, i):
    # assuming array starts at 1
    left_child_index = 2 * i
    right_child_index = 2 * i + 1
    max = i
    if left_child_index < end and unsorted_list[i] < unsorted_list[left_child_index]:   
        max = left_child_index   
    if right_child_index < end and unsorted_list[max] < unsorted_list[right_child_index]:   
        max = right_child_index   
    if max != i:   
        swap(i, max)   
        heapify(end, max)   


def heap_sort():     
    end = len(unsorted_list)   
    start = end // 2 - 1
    for i in range(start, -1, -1):
        heapify(end, i)   
    for i in range(end-1, 0, -1):   
        swap(i, 0)   
        heapify(i, 0)   

