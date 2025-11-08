import pandas as pd
import numpy as np

# Sample data for the DataFrame problems (4.2)
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9.0, 16.5, np.nan, 9.0, 20.0, 14.5, np.nan, 8.0, 19.0],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)

df.loc['d', 'name'] = 'Suresh'

print("\nDataFrame after changing 'James' to 'Suresh':")
print(df)

# Output (check row 'd'):
#      name  score  attempts qualify
# a   Anastasia   12.5         1     yes
# b        Dima    9.0         3      no
# c   Katherine   16.5         2     yes
# d      Suresh    NaN         3      no  <-- Updated
# e       Emily    9.0         2      no
# ...