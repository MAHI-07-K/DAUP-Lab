import numpy as np
arr2 = np.array([1, 2, 3, 4, 5])
arr3 = np.array([0, 2, 4, 3, 5])

print("\nArray 1:", arr2)
print("Array 2:", arr3)

print("Greater:", np.greater(arr2, arr3))
print("Greater or Equal:", np.greater_equal(arr2, arr3))
print("Less:", np.less(arr2, arr3))
print("Less or Equal:", np.less_equal(arr2, arr3))
print("Equal:", np.equal(arr2, arr3))
print("Equal within tolerance:", np.allclose(arr2, arr3, atol=1))

# Additional demonstrations of other methods
print("\nZeros array:", np.zeros(5))
print("Ones array:", np.ones(5))
print("Linspace array:", np.linspace(0, 1, 5))

# Convert array to list
print("Array to list:", np.array([10, 20, 30]).tolist())
