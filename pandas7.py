import numpy as np 
import pandas as pd 
dataset1 = {
    "A": ["A1","A2","A3","A4"],
    "B":["B1","B2","B3","B4"],
    "C":["C1","C2","C3","C4"],
}

dataset2 = {
    "A": ["A5","A6","A7","A8"],
    "B":["B5","B6","B7","B8"],
    "C":["C5","C6","C7","C8"],
}
df1 = pd.DataFrame(dataset1,index=[1,2,3,4])
df2 = pd.DataFrame(dataset2,index=[5,6,7,8])
print(df1)
print("-------------------------")
print(df2)

a = pd.concat([df1,df2])#iki dataframe'i indexlerine göre toplar
b = pd.concat([df1,df2],axis=1)# iki dataframe'i columnlara göre yanyana toplar
 #----join----- sql'deki mantık ile çalışır column olarak dataframe'leri birleştirmemizi sağlar
dataset3 = {
    "A" : ["A1","A2","A3","A4"],
    "B" : ["B1","B2","B3","A4"],
}
dataset4 = {
    "X" : ["X1","X2","X3"],
    "Y" : ["Y1","Y2","Y3"],
    
}
df3 = pd.DataFrame(dataset3,index=[1,2,3,4])
df4 = pd.DataFrame(dataset4,index=[1,2,3])
print(df4.join(df3))
#----Merge---- sadece ortak olan değerlerle bir dataframe elde edilir
dataset5 = {
    "A" : ["A1","A2","A3"],
    "B" : ["B1","B2","B3"],
    "anahtar" : ["K1","K2","K3"]
}
dataset6 = {
    "X" : ["X1","X2","X3","X4"],
    "Y" : ["Y1","Y2","Y3","Y4"],
    "anahtar" : ["K1","K2","K5","K4"]
}
df5 = pd.DataFrame(dataset5, index=[1,2,3])
df6= pd.DataFrame(dataset6,index=[1,2,3,4])

d = pd.merge(df5,df6, on="anahtar") #anahtar değerlerinden ortak olanlara göre bir inner join işlemi gerçekleştirir
print(d)




#join ve merge farkı; join indexler üzerinden ilerlerken merge column'lar üzerinden ilerler