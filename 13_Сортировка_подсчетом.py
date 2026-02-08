
print()
'''
реализация для ЛЮБЫХ целых чисел
Время	O(n + k)
Память	O(k)
'''
arr3 = [-10,2,0,-5,-9,5,1,3,1,0,1]
arr2 = [1002,1001,100]

def counting_sort_3(input_array):
    if len(input_array) < 1:
        return []
    min_val, max_val = min(input_array), max(input_array)
    offset = - min_val
    counters = [0 for _ in range(max_val + offset + 1)]
    for i in range(len(input_array)):
        counters[input_array[i] + offset] += 1

    index = 0
    for i in range(len(counters)):
        for j in range(counters[i]):
            input_array[index] = i - offset
            index += 1

    return input_array


counting_sort_3(arr2)
print(arr2)

counting_sort_3(arr3)
print(arr3)





'''
ОЧень быстрая если массив состоит из цифр (не чисел)
ниже реализация для целых цифр от 0 до 9
'''

arr = [0, 2, 3, 2, 1, 5, 9, 1, 1]

def counting_sort(input_arr):
    counters = [0 for _ in range(10)]
    for i in range(len(input_arr)):
        counters[input_arr[i]] += 1
    index = 0
    # print(counters)
    for i in range(len(counters)):
        for j in range(counters[i]):
            input_arr[index] = i
            index += 1
    # print(input_arr)

#



'''
реализация для всех положительных целых чисел
'''


def counting_sort_2(input_array):
    if len(input_array) < 1:
        return []
    if min(input_array) < 0:
        raise ValueError("Только положительные числа")
    counters = [0 for _ in range(max(input_array) + 1)]
    print(max(input_array) + 1)
    for i in range(len(input_array)):
        counters[input_array[i]] += 1
    index = 0
    for i in range(len(counters)):
        for j in range(counters[i]):
            input_array[index] = i
            index += 1
    return input_array





