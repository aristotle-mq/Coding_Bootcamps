import numpy as np

N = 1000 # Размер матрицы

first_matrix = np.random.randint(-100, 100, (N, N))
second_matrix = np.random.randint(-100, 100, (N, N))
serial_mul_res = first_matrix @ second_matrix

print(serial_mul_res)
