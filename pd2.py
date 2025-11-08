# Use the Series created in problem (i)
import pandas as pd
my_list = [10, 20, 30, 40, 50]
s = pd.Series(my_list)
python_list = s.tolist()

print("Converted Python List:")
print(python_list)
print("Type of the converted object:", type(python_list))

# Output:
# Converted Python List:
# [10, 20, 30, 40, 50]
# Type of the converted object: <class 'list'>