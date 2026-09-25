import numpy as np

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
print(matrix[:, 1])


