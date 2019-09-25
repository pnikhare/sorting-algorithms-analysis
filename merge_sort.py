def split_list(some_list):
    mid = len(some_list)//2
    return some_list[:mid], some_list[mid:]


def merge_sorted_lists(left_list, right_list):
    if len(left_list) == 0:
        return right_list
    elif len(right_list) == 0:
        return left_list
    index_left = index_right = 0
    merged_list = []
    list_len_target = len(left_list) + len(right_list)
    while len(merged_list) < list_len_target:
        if left_list[index_left] <= right_list[index_right]:
            merged_list.append(left_list[index_left])
            index_left += 1
        else:
            merged_list.append(right_list[index_right])
            index_right += 1
        if index_right == len(right_list)
            merged_list += left_list[index_left:]
            break
        elif index_left == len(left_list):
            merged_list += right_list[index_right:]
            break
    return merged_list

def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        left, right = split(input_list)
        return merge_sorted_lists(merge_sort(left), merge_sort(right))

