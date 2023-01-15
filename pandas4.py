import numpy as np 
import pandas as pd 
from numpy.random import randn


outerındex=["Group1","Group1","Group1","Group2","Group2","Group2","Group3","Group3","Group3"]
innerındex = ["Index1","Index2'","Index3","Index1","Index2","Index3","Index1","Index2","Index3"]
a = list(zip(outerındex,innerındex)) #zip fonk. ile bu iki indexi birleştirdik
hierarchy = list(zip(outerındex,innerındex))
hierarchy = pd.MultiIndex.from_tuples(hierarchy)#pd içindeki multiındex ile çoklu indeks oluştururuz
print(hierarchy)
df = pd.DataFrame(randn(9,3),hierarchy,columns=["Column1","Column2","Column3"])
print(df)
print(df["Column1"])#column1 aldık
print(df.loc["Group1"])#loc sayesinde dataframe'i parçaladık ve group1'deki indexleri almış olduk
print(df.loc["Group1"].loc["Index1"])#group1 içindeki Index1'i çağırmış olduk
print("grup 3 içindeki index2'nin 3.sütundaki değeri: ",df.loc["Group3"].loc["Index2"]["Column3"])

df.index.names =["Groups","Indexes"]#dışardan içeriye doğru isim verdik
print(df)
print(df.xs("Group2"))#loc ile aynı işlemi görür
print(df.xs("Index1",level="Indexes"))#bu özellik sayesinde g1,g2 ve g3'lerin ındex1 lerini alıyoruz level'da nerden başlayacağını belirtiyoruz





