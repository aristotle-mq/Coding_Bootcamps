print()
'''
O(n * log n)
'''


def quick_sort(arr):
    if len(arr) < 2: return arr
    else:
        pivot = arr[0]
        left = [i for i in arr[1:] if i <= pivot]
        right = [i for i in arr[1:] if i > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

mas = [95,-43,0,53,2,-8,-3,-29,6,86,34,1]
print(quick_sort(mas))