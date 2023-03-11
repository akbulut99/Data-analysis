#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


# In[3]:


veri = pd.read_csv("olimpiyatlar_temizlenmiş.csv")


# In[26]:


#histogram grafiği çizdireceğiz dağılımları daha iyi görmek için
def plothistogram(degisken):
    """
    girdi: Değişken/sütun adı
    çıktı: ilgili değişkenin histogramı
    """
    plt.figure()
    plt.hist(veri[degisken],bins=100,color="orange") #bins kaç parçaya böleceğini yazarız
    plt.xlabel(degisken)
    plt.ylabel("Frekans")
    plt.title("Veri Sıklığı.{}".format(degisken))
    plt.show()


# In[27]:


#tüm histogramları çizdirelim
sayısal_degisken=["Age","boy","kilo","yıl"]
for i in sayısal_degisken:
    plothistogram(i)


# In[29]:


veri.describe()#veriyi bize özetleyen bir fonksiyondur


# In[ ]:




