import random
import time

print()
'''
O(n**2) 
'''
def check_array(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def random_array(n):
    return [(random.randint(-99, 100)) for i in range(n)]

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



ls = random_array(25000)
ls2 = ls.copy()


start = time.time()
bubble_sort(ls)
finish = time.time()
print(f'{check_array(ls)}___[{finish - start}]')
