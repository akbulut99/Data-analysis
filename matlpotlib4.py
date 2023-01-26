import matplotlib.pyplot as plt 
import numpy as np 
x = np.arange(1,6) 
y = np.arange(2,11,2)
fig,axes = plt.subplots(nrows=2,ncols=1,)
axes[0].plot(x,y,color="red")
axes[0].set_title("First Axes")
axes[1].plot(x,x**0.5,color="purple")
axes[1].set_title("Second Axes")
plt.tight_layout()
plt.show()
fig.savefig("fig1.png")