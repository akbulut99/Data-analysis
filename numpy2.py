import numpy as np 
arr = np.arange(1,10)
print(arr[0:4])#0 dan 4.indexe kadar parçladık
print(arr[::2])#2şer 2şer parçaladık
print(arr.reshape(3,3))
arr[:3] = 25 #ilk 3 index değerini 25 olarak değiştirdi
print(arr)
arr = np.arange(1,10)
arr2=arr.copy() #arr'yi kopyaladık
arr2[:3] = 1283
print(arr2)
