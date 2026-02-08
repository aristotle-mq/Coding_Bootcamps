import random

print()
'''
O(n**2)
'''

def random_array(n):
    return [(random.randint(-99, 100)) for i in range(n)]

def sort_vibor(arr):
    for i in range(len(arr)):
        i_min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i_min]:
                i_min = j
        if arr[i] == arr[i_min]:
            continue
        arr[i], arr[i_min] = arr[i_min], arr[i]
    return arr

ls = random_array(20)
print(ls)
print(sort_vibor(ls))