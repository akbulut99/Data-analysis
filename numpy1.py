import numpy as np

data_list=[1,2,3,4]
arr = np.array(data_list) #tek boyutlu numpy array'i
data_list2 = [[10,20,30],[40,50,60],[70,80,90]]#3x3 lük bir matris oluşturuyoruz
arr2 = np.array(data_list2)
arr3 = np.array([1,2,3])
print(arr2[2,2])#arr2 listesindeki 2.elemanın 2.indexteki elamanını yazdırdım
arr4 = np.arange(0,100,3)#range yapısını numpy arraylerindeki kullanım şekli 
arr5=np.ones((3,3))#3x3 lük 1 matrisi
print(arr5)
np.linspace(0,100,5)#0 ile 100 arasındaki değerleri 5 parçaya bölerek saklar
np.linspace(0,1,5)
print(np.eye(3))#3x3 lük birim matris 
np.random.randint(0,10)#0 ile 10 arasında random değer verir
np.random.randint(15)
np.random.randint(0,30,3)#0 ile 30 arasında değer üretip 3 parça halinde saklar
np.random.rand(5)#0ile 5 arasındaki random değerleri 5 parça halinde depolar
gauss=np.random.randn(5)#gauss distribution yaparak negatif değerlerin de saklanmasını sağlar
print(gauss)
arr6 = np.arange(25)
print(arr6.reshape(5,5)) #arr6 listesinin 5x5lik  matrisler haline getirerek saklar
#oluşturmak istediğimiz matris boyutunun çarpımı saklanan elaman sayısına eşit olmalı 5x5=25 ama 2x5!=25 olduğu 2x5 lik matris şeklinde 25 tane değeri saklayamazsınız!!
newarray = np.random.randint(1,100,10)
newarray.max() #en büyük değeri verir
newarray.min() #en küçük değeri verir 
newarray.sum() #toplar
newarray.mean() #ortalamasını verir
newarray.argmax() # maximum değerin hangi indexte olduğunu öğrenebiliriz
#DETERMİNANT HESAPLAMA
#------------------------
detarray = np.random.randint(1,1283,64)
matris = detarray.reshape(8,8)
print(matris)
sonuc = np.linalg.det(matris)#linalg içindeki det fonksiyonu sayesinde determinant hesaplanabiir
print(sonuc)

detarray1 = np.array([[1,2],[3,4]])
sonuc1 = np.linalg.det(detarray1)
print(sonuc1)