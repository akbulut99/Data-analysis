import numpy as np

newarray = np.arange(1,21)
newarray=newarray.reshape(5,4)#5x4 lük matris yaptık
print(newarray)
print(newarray[:,:2])#sütunların sadece ilk 2 değerini aldık
print(newarray[:3,:3])#ilk 3'ü alır satır ve sütunu alır
print(newarray[:2,:])#ilk iki satırı aldık
print(newarray[:2])
arr = np.arange(1,11)
print(arr > 3) # arr içindeki 3 den büyük değerelere true, 3 den küçüklere false değeri koyar.
boolenarray = arr > 3 #bu işlemde mantıksal ifademizi bir değişkene atadaık
print(arr[boolenarray])#false olanları listeden atıp sadece true olanları gösterir
print(arr[arr > 5]) # aynı mantıkla çalışır