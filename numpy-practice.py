import numpy as np
from numpy.matlib import number

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print(arr.dtype)
sum = np.sum(arr)
print(sum)
mean = np.mean(arr)
print(mean)
print(np.std(arr))

matrix = np.array([[1, 2], [3, 4]])
print(matrix)
print(matrix.shape)
print(matrix.dtype)



matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7,8, 9]
])

index1 = matrix[1,2]

# select an index
print(index1) 
# select a row
print(matrix[1])
# select a column
# print(matrix[:, 1])numpy slicing
print('[0:2] --> ', matrix[0:2])
print(matrix[1:3, 1:3])

#  select row 0-1 and column 1-2
print('select row 0-1 and column 1-2 --> ', matrix[0:2,1:3])



numbers = np.array([1,2,3,4,5,6])

print("shape-> ",numbers.shape)
print("dtype-> ",numbers.dtype)

# print(numbers.reshape(2,3))
# print(numbers.reshape(3,3))

# auto calculate number of rows or columns
print(numbers.reshape(-1,3))
print(numbers.reshape(3,-1))
print(numbers.reshape(-1,2))
print(numbers.reshape(2,-1))