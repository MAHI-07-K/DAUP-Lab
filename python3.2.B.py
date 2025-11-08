# b. Find indices of max and min along a given axis
import numpy as np
arr = np.array([3, 7, 2, 9, 4, 7, 2, 9, 1])
matrix = np.array([[10, 20, 5],
                   [30, 15, 25]])

print("\nMatrix:\n", matrix)
print("Max value:", np.max(matrix))
print("Min value:", np.min(matrix))
print("Index of max (flattened):", np.argmax(matrix))
print("Index of min (flattened):", np.argmin(matrix))
print("Index of max along axis 0 (column-wise):", np.argmax(matrix, axis=0))
print("Index of min along axis 1 (row-wise):", np.argmin(matrix, axis=1))

# Using repr to get string representation
print("\nString representation of array:", repr(arr))

# Using bincount to count occurrences of non-negative integers
print("Bin count of array elements:", np.bincount(arr))

# Using unique to get unique elements and their counts
unique_elements, counts = np.unique(arr, return_counts=True)
print("Unique elements:", unique_elements)
print("Counts of each unique element:", counts)
