import numpy as np
arr = np.array([3, 2, 1, 2])
print("Original array: ", arr)
print("Append (6,7,8): ",np.append(arr, [6, 7, 8]))
print("Insert Specific (10,11) at third second position: ", np.insert(arr, 2, [10, 11]))
print("Delete values (1,3): ", np.delete(arr, [0, 2]))
print("Unique element: ", np.unique(arr))
print("Sorted array: ", np.sort(arr))
np.savetxt('arr.txt', arr)
ld = np.loadtxt('arr.txt')
print("Loaded from arr.txt: ", ld)

