import numpy as np
import pandas as pd 
from numpy.random import randn
df = pd.DataFrame(randn(4,3),["A","B","C","D"], ["Column1","Column2","Column3"])
print(df["Column1"] > 0)#numpylarda filtreleme işlemeni pandasda da yapabiliyoruz
df["Column4"] = pd.Series(randn(4),["A","B","C","D"]) #yeni bir sütun ekliyoruz
print(df)
df["Column5"] = randn(4) # başka bir sütun eklme yöntemi
print(df)
df["Column6"] = ["newValue1","newValue2","newValue3","newValue4"]
df.set_index("Column6") # column6 değerleri yeni satır başları olmuş oldu

df.set_index("Column6",inplace = True) #güncelleme yaptık
print(df) 