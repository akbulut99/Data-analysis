import numpy as np
import pandas as pd 
label_list=["mustafa","kemal","murat","kadir","zeynep"]
data_list =[10,20,30,40,50]
a = pd.Series(data= data_list,index= label_list) #pandas serimizi oluşturduk
b = pd.Series(data_list) #herhangi bir index vermezsek kendisi otomatik atar
nparray = np.array([10,20,30,40,50])
print(pd.Series(nparray,label_list))#np listesi de verebiliriz
print(pd.Series(data= nparray,index=["a","b","c","d","e "]))
datadic ={"kadir":30,"murat":58,"cenk":60} #verilerimizi sözlük formatında oluşturduk
print(pd.Series(datadic)) 