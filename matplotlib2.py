import matplotlib.pyplot as plt 
import numpy as np 
x = np.arange(1,6)
y = np.arange(2,11,2)
fig = plt.figure()#bir figür oluşturduk
axes = fig.add_axes([0.1,0.1,0.8,0.8])#figürümüze grafik ekliyoruz
#veridğimiz ilk değer x ekseninin sayfa düzleminde başlangıç noktasını belirler
#ikinci değer de y ekseninin uzaklığını belirler diğer değerler x ve y ekesninin kaçtan başlatmak istediğimizi belirtiyoruz
axes2 = fig.add_axes([0.2,0.5,0.2,0.3])
axes.plot(y,x)
axes.set_xlabel("outer x")
axes.set_ylabel("outer y")
axes.set_title("outer graph")

axes2.plot(x,y)
axes2.set_xlabel("ınner x")
axes2.set_ylabel("ınner y")
axes.set_title("ınner graph")
  
plt.show()