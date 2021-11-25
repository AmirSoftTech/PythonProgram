'''
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    for col in row:
        print(col)
'''

import numpy as matrix
mat = matrix.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]

    ]
)
print(mat)
print("----------------------------------------")
arr1 = matrix.array([1, 2, 3])

arr2 = matrix.array([4, 5, 6])

arr3 = matrix.array([7, 8, 9])

arr = matrix.vstack((arr1, arr2, arr3))

print(arr)
