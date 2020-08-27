import numpy as np

# a = np.array([[2, 3], [5, 2]])
# print(a)

d = np.array([[1, 2, 3, 4, 5], [2, 4, 5, 6, 7], [5, 7, 8, 9, 9]])
print(d)

print(d[1][2])
print(d[1, 2])
print(d[1:, 3:])

print(d.shape)
print(d.dtype)

# data = np.arange(1, 5)
# print(data)
# print(data.astype("float64"))
# print(data.astype("int32"))

print(np.zeros((2, 10)))
print(np.ones((2, 10)))
print(np.arange(2, 10))

a = np.ones((2, 3))
print(a)
b = np.transpose(a)
print(b)

arr1 = np.array([[2, 3, 4], [6, 7, 8]])
arr2 = np.array([[12, 23, 14], [36, 47, 58]])

print(arr1 + arr2)
print(arr1 * arr2)
print(arr1 / arr2)

arr3 = np.array([100, 200, 300])
print(arr1.shape)
print(arr3.shape)
print(arr1 + arr3)

arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr4.shape)
# print(arr1 + arr4)

arr5 = np.array([[9], [3]])
print(arr5.shape)
print(arr5 + arr1)