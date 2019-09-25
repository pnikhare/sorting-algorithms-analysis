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


def heap_insert(complete_heap, element):
    complete_heap.append(element)
    i = len(complete_heap)
    while i > 1 and complete_heap[i//2] > complete_heap[i - 1]:
        complete_heap[i -1], complete_heap[i//2] = complete_heap[i//2], complete_heap[i - 1]  # swap parent and child
    return complete_heap

def heap_remove_min(complete_heap):
    temp = complete_heap[1]
    length = len(complete_heap)
    complete_heap[1] = complete_heap[length - 1]
    length -= 1
    i = 1
    while i < length:
        if 2*i + 1 <= length:
            if complete_heap[i] <= complete_heap [2 * i] and complete_heap[i] <= complete_heap[2 * i + 1]:
                return temp
            else:
                j = 2*i if complete_heap[2*i] < complete_heap[2*i + 1] else (2 * i + 1)
                complete_heap[i],complete_heap[j] = complete_heap[j], complete_heap[i]
                i = j
        else:
            if 2 * i <= length:
                if complete_heap[i] > complete_heap[2 * i]:
                    complete_heap[i], complete_heap[2 * i] = complete_heap[2 * i], complete_heap[i]
                return temp
    return temp


def heap_sort(given_list):
    heap_list = [0]  # not gonna be using first element of heap
    sorted_list = []
    for element in given_list:
        heap_list = heap_insert(heap_list, element)
        sorted_list.append(heap_remove_min(heap_list))
    return sorted_list


a = [84,23,54,56,93]
b = heap_sort(a)
print(b)