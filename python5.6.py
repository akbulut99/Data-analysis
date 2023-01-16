import numpy as np
import pandas as pd 

dataset = {"Departman":["Bilişim","İnsan Kaynakları","Üretim","Üretim","Bilişim","İnsan Kaynakları"],
"Çalışan":["Mustafa","Jale","Kadir","Zeynep","Murat","Ahmet"],
"Maaş":[3000,3500,3000,4500,2000,4000] }  #datasetimiz oluşturduk
df = pd.DataFrame(dataset) #datasetimizden dataframe'mizi oluşturduk
DepGroup = df.groupby("Departman")#departmana göre gorupby işlemlerimizi yapar
DepGroup.sum()#her bir departmanda çalışan insanların toplam maaşlarını bize verir
df.groupby("Departman").sum()#ekstra değişken tanımlamadan işlemimizi daha kısa yapmış oluruz
int(df.groupby("Departman").sum().loc["Bilişim"])#sadece bilişim departmanının maaşını buluruz
print(df.groupby("Departman").count())#her bir departmanda çalışan insan sayısını bulmuş oluryz
print(df.groupby("Departman").max())#departmanlar kendi içinde gruplanarak her bir departmanın en yüksek maaştan en düşüğe doğru sıralanır
df.groupby("Departman").min()
df.groupby("Departman").min()["Maaş"] #maaş sütünuna göre en düşük maaşları getirir ve kendi içinde yeni bir seri oluşturur.
a = df.groupby("Departman").max()["Maaş"]["Bilişim"]
print("bilişim departmanın en yüksek maaşı: ",a)

