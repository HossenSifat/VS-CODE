from socket import SIO_LOOPBACK_FAST_PATH
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

ser = pd.Series(np.random.rand(10))
print(ser)
print(type(ser))

newdf = pd.DataFrame(np.random.rand(334,5), index = np.arange(334))
print(newdf)
print(newdf.head())
print(type(newdf))
print(newdf.describe())
print(newdf.dtypes)

newdf[0][0]= 'Sifat'
print(newdf)

print(newdf.index)
print(newdf.columns)
print(newdf.to_numpy())
print(newdf)
newdf2 = newdf
newdf2[0][1] = 0.5
print(newdf2)
print(newdf)
newdf2 = newdf.copy()
newdf2[0][1] = 9154
print(newdf2)
print(newdf)


newdf.columns = list('ABCDE')
print(newdf)

newdf.loc[0,0 ]= 658
print(newdf)

newdf =newdf.drop(0, axis= 1)
print(newdf)
print(newdf.head())
print(newdf.loc[[1,2], :])
# print(newdf.loc[(newdf['A'] < 0.3)])
#in loc we need to call exist name in coloum and rows where iloc we call in serial number 
print(newdf.iloc[[0,2], [1,2]])
print(newdf.head(5))
newdf =newdf.drop([1,3], axis =0)
print(newdf)
newdf = newdf.reset_index(drop= True)
print(newdf)
