# b. Test whether none of the elements of a given array is zero
import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
print("\nArray:", arr1)
print("None of the elements is zero:", np.all(arr1))