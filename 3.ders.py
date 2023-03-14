#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

# In[3]:


veri = pd.read_csv("olimpiyatlar_temizlenmiş.csv")


# In[5]:


#kutu grafileri çizelim
plt.boxplot(veri.Age)
plt.title("Yaş değişkeni için kutu grafiği")
plt.xlabel("yaş")
plt.ylabel("Değer")
plt.show()


# In[20]:


def plotbar(degisken,n=5):
    veri1 = veri[degisken]
    veri_sayma = veri1.value_counts()
    veri_sayma = veri_sayma[:n]
    plt.figure()
    plt.bar(veri_sayma.index,veri_sayma,color="orange")
    plt.xticks(veri_sayma.index,veri_sayma.index.values)
    plt.xticks(rotation=45)
    plt.ylabel("Frekans")
    plt.title("Veri sıklığı.{}".format(degisken))
    plt.show()
    print("{}, {}".format(degisken,veri_sayma))


# In[ ]:





# In[21]:


kategorik_degisken=["isim","cinsiyet","takım","ülke kodu","Sezon","şehir","spor","etkinlik","Medal"]
for i in kategorik_degisken:
    plotbar(i)


# In[38]:


#cinsiyete göre boy ve ağırlık karşılaştırması saçılım grafiği olarak
erkek=veri[veri.cinsiyet=="M"]
kadın=veri[veri.cinsiyet=="F"]
plt.figure()
plt.scatter(kadın.boy,kadın.kilo,alpha=0.8,label="kadın",color="orange")#alpha opaklığı ayarlar
plt.scatter(erkek.boy,erkek.kilo,alpha=0.4,label="erkek",color="navy")
plt.xlabel("boy")
plt.ylabel("kilo")
plt.title("boy/kilo arasındaki ilişki")
plt.legend()
plt.show()


# In[41]:


veri.loc[:,["Age","boy","kilo"]].corr()#korelasyon çıkartacak


# In[48]:


#madalya ve yaş arasındaki ilişki
#önce sporcuları madalya türlerine göre ayıralım
veri_gecici =veri.copy()
veri_gecici=pd.get_dummies(veri_gecici,columns=["Medal"])#get_dummies komutu madalya sütununu kendi içinde parçladı
veri_gecici.head(2)


# In[57]:


veri_gecici[["Age","Medal_Bronze","Medal_Gold","Medal_Silver"]].groupby(["takım"],as_index=False).sum().sort_values(by="Medal_Gold",ascending=False)


# In[52]:


veri.columns


# In[ ]:




