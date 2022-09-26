import numpy as np
import pandas as pd
dict1 = {
    'name': ['sifat', 'shuvo', 'rohan', 'imran'],
    'marks': [92, 94, 86 ,70],
    'city': ['Ctg', 'Ukia', 'Khulna', 'Dhaka']
}

df = pd.DataFrame(data =dict1)
print(df)
df.to_csv('Friend_marks')
