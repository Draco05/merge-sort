import random


# Implementation of merge sort in Python 3.10
# This logic may work in most of the programming languages

#  Merge sort using recursion!
def merge_sort(start, end):
    if len(lst[start:end]) == 1:
        return lst[start:end]
    size = end - start
    return merge(merge_sort(start, start + (size // 2)), merge_sort(start + (size // 2), end))


# Merge two sorted lists
def merge(lst1, lst2):
    i = 0
    j = 0
    merged_lst = []

    # Appending to merged_lst the smallest numbers in each list
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_lst.append(lst1[i])
            i += 1
        elif lst1[i] > lst2[j]:
            merged_lst.append(lst2[j])
            j += 1
        else:
            merged_lst.append(lst1[i])
            merged_lst.append(lst2[j])
            i += 1
            j += 1

    # Concatenate the remaining list
    if i == len(lst1):
        merged_lst = merged_lst + lst2[j:]
    elif j == len(lst2):
        merged_lst = merged_lst + lst1[i:]
    return merged_lst


lst = [random.randint(0, 100) for _ in range(10)]
print(lst)
print(merge_sort(0, len(lst)))

