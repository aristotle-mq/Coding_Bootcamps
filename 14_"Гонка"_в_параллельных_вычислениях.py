import numpy as np


N = 100000 # размер массива



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


