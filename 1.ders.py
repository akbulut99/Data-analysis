#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


# In[46]:


df =pd.read_csv("olimpiyatlar.csv") #veri setimizi dahil ettik


# In[9]:


df.info()#veri hakkında bilgilere bakabliriz


# In[47]:


#sütun isimlerini yeniden adlandıralım.(rowlar içinde indexten yapabilirsim)
df.rename(columns={
            'Name':'isim',
            'Gender':'cinsiyet',
            'age':'yas',
            'Height':'boy',
            'Weight':'kilo',
             'Team':'takım',
            'NOC':'ülke kodu',
             'Games':'oyunlar',
              'Year':'yıl',
             'Season':'Sezon',
            'City':'şehir','Sport':'spor',
            'Event':'etkinlik','Meda':'madalya'
},inplace=True)


# In[48]:


#drop fonksiyonu ile bazı sütunları çıkartalım
df=df.drop(["ID","oyunlar"],axis=1)


# In[36]:


#her bir etkinlik özelinde boy ve kilo ortalamalarını bul
#her bir etkinlik özelinde kayıp boy ve kilo değerlerini ortalamaya eşitle
veri_copy =df.copy()#verimiz bozulmasın diye kopyaladık
essiz_etkinlik =pd.unique(df.etkinlik)#etkinlikleri tekrar etmeyecek şekilde(unique) bir değişkene atıyoruz
print("Etkinlik sayısı:{}".format(len(essiz_etkinlik)))
etkinlik[:10]#ilk 10tanesine bakalım


# In[30]:


boy_kilo=["boy","kilo"]
for i in essiz_etkinlik:
    #etkinlik filtresi oluşturalım
    filtre = veri_copy.etkinlik == i
    #etkinliğe göre filtreleyim
    veri_filtre=veri_copy[filtre]
    #boy ve kilo ortalamaları hesaplayalım
    for s in boy_kilo:
        ortalama=np.round(np.mean(veri_filtre[s]),2)
        if~np.isnan(ortalama):#etkinlik özelinde ortalama varsa
            veri_filtre[s]=veri_filtre[s].fillna(ortalama)
        else:#eğer etkinlik özelinde ortalama varsa ortalamayı hesapla
            tüm_veri_ortalaması=np.round(np.mean(df[s]),2)
            veri_filtre[s]=veri_filtre[s].fillna(tüm_veri_ortalaması)
    #etkinlik özelinde kayıp değerleri doldurulmuş olan veriyi,veri_geciciye eşitle
    veri_copy[filtre]=veri_filtre
    #kayıp değerleri giderilmiş olan geçici veriyi gerçek veriye eşitleyelim
    df = veri_copy.copy()
    df.info()#boy ve kilo sütunlarında kayıp değer sayısına bakalım


# In[54]:


#yaş değişkeninde tanımlı olmayan değerleri bulalım.
yas_ortalaması = np.round(np.mean(df.Age),2)
df["Age"]=df["Age"].fillna(yas_ortalaması)


# In[63]:


#madalya alamanyaları veri setimizden çıkartalım
madalya =df["Medal"]
pd.isnull(madalya).sum()#madalya kazanamayan sporcu sayısı
madalya_filtresi=~pd.isnull(madalya)#madalya alanları ayırdık
df=df[madalya_filtresi]#bu komutla da madalyası olmayanlar veri setimizden düştü
df.head(5)


# In[64]:


#sonradan kullanmak için kaydedelim
df.to_csv("olimpiyatlar_temizlenmiş.csv")


# In[ ]:




