import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([[4, 5, 6], [1, 2, 3]])
arrsq = np.sqrt(arr1)
exp = np.exp(arr1)
std = np.std(arr1)
stdx = np.std(arr2, axis=1)
print("Square root of a array: ", np.round(arrsq, decimals=2))
print("Exponential function: ", np.round(exp, decimals=2))
print("Sum of array: ", np.sum(arr1))
print("Mean of array: ", np.mean(arr1))
print("Max value: ", np.max(arr1))
print("Standard deviation: ", np.round(std, decimals=2))
print("Standard deviation along other axis: ", np.round(stdx, decimals=2))
