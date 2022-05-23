#!/bin/python3

import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

output_0 = ""
for x in range(0, m):
    for y in range(0, n):
        output_0 += f"{matrix[y][x]}"
solution_0 = re.sub("(?<=\w)\W+(?=\w)", " ", output_0)
solution = re.sub("^ ", "", solution_0)
print(solution)