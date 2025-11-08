# a. Extract numbers less than and greater than a specified number
import numpy as np
arr = np.array([3, 7, 2, 9, 4, 7, 2, 9, 1])


specified_number = 5
less_than = arr[arr < specified_number]
greater_than = arr[arr > specified_number]

print("Original array:", arr)
print(f"Numbers less than {specified_number}:", less_than)
print(f"Numbers greater than {specified_number}:", greater_than)

