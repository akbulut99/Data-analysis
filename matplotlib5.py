import matplotlib.pyplot as plt 
import numpy as np 
x = np.arange(1,6) 
y = np.arange(2,11,2)
 
fig1 = plt.figure(figsize=(5,5))
axes1 = fig1.add_axes([0,0,1,1])
axes1.plot(x,x**0.5,color = "red",label = "x'in karekökü",   linewidth = 3)
axes1.plot(x,x**2,color = "green",label = "x kare",  linestyle=":",marker = "o" ,linewidth = 5  )
axes1.plot(x,x**3,color = "blue",label = "x küp", linestyle="--",marker = "o",markersize=10 ,markerfacecolor ="black",markeredgecolor="white",markeredgewidth=5 ,linewidth = 5)
axes1.legend()#labelların gözükmesi için 
plt.tight_layout()
plt.show()