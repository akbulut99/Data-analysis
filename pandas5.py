import numpy as np
import pandas as pd 
from numpy.random import rand

arr = np.array([[10,20,np.nan],[5,np.nan,np.nan],[21,np.nan,10]]) # 3x3 lük bir matrsi oluşturduk
df = pd.DataFrame(arr,index=["Index1","Index2","Index3"],columns=["Column1","Column2","Column3"])
print(df)
df.dropna()#kayıp ya da bozuk verileri dataframe'den siler axis=1 dersek 1.sütuna göre siler
print(df.dropna(thresh=2)) #bir indexte minumum 2 tane notAnumber olmayan veri olmalı yoksa silmez
print(df.fillna(value=3))#notanumber olan veriler yerine değer atamak için kullanılır
print(df.sum())#her bir column değerini kendi içinde toplar
print(df.sum().sum())#tüm index değerlerini toplar
print(df.isnull().sum())#isnull komutu bir sütunda kaç tane notanumber olduğunu öğrenmemizi sağlar

