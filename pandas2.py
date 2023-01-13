
import numpy as np 
import pandas as pd 
from numpy.random import randn,rand

df = pd.DataFrame(data= randn(3,3), index = ["A","B","C"], columns = ["sütun1","sütun2","sütun3"])
#dataframeler serilerin birleşmiş halidir
print(df["sütun1"])
df["sütun4"] = pd.Series(randn(3),["A","B","C"])#frame'mize yeni bir sütun ekledik
print(df)
df.drop("sütun4",axis=1,inplace=True)#"1.satıra göre sütun 4'ü siler"
#dataframe'i güncellemek için inplace=True olarak değeri vermeliyiz..a
print(df)
print(df.loc["A"])