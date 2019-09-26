def insertion_sort(unsorted_list):
    # Traverse through 1 to len(arr)
    for i in range(1, len(unsorted_list)):
        j = i - 1
        temp = unsorted_list[i]
        while j >= 0 and temp < unsorted_list[j]:
            unsorted_list[j + 1] = unsorted_list[j]
            j -= 1
        unsorted_list[j + 1] = temp
    return unsorted_list
