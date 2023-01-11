import numpy as np
arr1 = np.ones(5) # 5 tane birden oluşan 1x1 lik matris
print(arr1)
arr2 = np.zeros(5) #5 tane sıfırdan oluşan 1x1 lik matris
print(arr2)
arr3 =np.arange(1,100)
boolenarray = arr3 % 2 == 0
print(arr3[boolenarray].reshape(7,7))#1 ile 100 arasında ikiye tam bölünebilen sayıların 7x7 lik matrisi
print(arr1*10) # 5 tane 10 bulunduran 1x1 lik matris
arr4 = np.arange(1,17)
print(arr4.reshape(4,4))# 1'den 16'ya kadar sayıların barındıran 4x4'lük matris
I = np.eye(4) #4x4'lük birim matris
print(I)
arr5 = np.random.randint(0,5)#0 ile 5 arasında rastgele değer üretir
print(arr5)
gauss = np.random.randn(5,5) #5x5'lik gauss distribution matrisi
print(gauss)
arr6= np.linspace(1,5,20)#1 ile 5 arasındaki mesafeyi 20 eşit parçaya bölerek bir array oluşturduk 
print(arr6)
arr = np.arange(1,101).reshape(10,10)
print(arr)
print(arr[4:]) #5satırdan başlar
print(arr[6:,4:])#7.satırdan başlar sonraki satırda 4 fazlasıyla devam eder
print(arr[:3,2:4]) # ilk 3 satırın 3.ve 4.sütunlarındaki gösterir 
array1=np.array([2,12,22])
print(arr[:3,1:2])#array1'i 3x1 lik matris haline getirir
arr11 = ((np.random.rand(9) * 5).astype(int)).reshape(3,3)
arr22 = ((np.random.rand(9) * 5).astype(int)).reshape(3,3)
print(arr11 * arr22) # iki matrisi çarpar
print(arr11 + arr22) # iki matrisi toplar
print(arr11.mean()) # arr11 matrisinin tüm elamanlarının ortlamasını veriri
