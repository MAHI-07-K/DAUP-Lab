# Create a Pandas Series from a Python list
import numpy as np
import pandas as pd
my_list = [10, 20, 30, 40, 50]
s = pd.Series(my_list)

print("Pandas Series:")
print(s)

# Output:
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64