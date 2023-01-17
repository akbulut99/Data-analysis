import numpy as np 
import pandas as pd 
df = pd.DataFrame({
    "Column1":[1,2,3,4,5,6],
    "Column2":[100,100,200,300,300,100],
    "Column3":["Mustafa","Kamil","Emre","Ayşe","Murat","Zeynep"]
})

a = df.head(n=3) #ilk 'n' rowu bize geri döner
#df.unique()#eşsiz değerleri bulmamızı sağlar
df["Column2"].nunique()#column2'de kaç tane eşşiz değerin olduğunu bize geri döner
df["Column2"].value_counts() #column2'de bir değerin kaç döndüğünü gösterir
b=df[(df["Column1"]>=4) & (df["Column2"]==300)]#column1'in 4 ten büyük ve column2'in 300'e eşit olan değerlerini getirir
print(b)
def times3(x):
    return x * 3

df["Column2"] = df["Column2"].apply(times3) #column2'deki değerleri times3 fonksiyonuyla 3 le çarpıp yeniden güncelledik
df["Column2"] = df["Column2"].apply(lambda x : x * 2)#fonksiyonu istersek lambda ile de tanımlayabiliriz
 
df.drop("Column3",axis=1) #column3'ü siler.
df.columns #columnları görmemizi sağlar
df.index #indexleri görmemizi sağlar
df1 = pd.DataFrame({
    "Ay" : ["Mart","Nisan","Mayıs","Mart","Nisan","Mayıs","Mart","Nisan","Mayıs"],
    "Şehir":["Ankara","Ankara","Ankara","İstanbul","İstanbul","İstanbul","İzmir","İzmir","İzmir"],
    "Nem":[10,25,50,21,67,80,30,70,75]
})

d=df1.pivot_table(values="Nem",index="Ay",columns="Şehir")
print(d)

