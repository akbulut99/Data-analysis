import matplotlib.pyplot as plt 
import numpy as np 
x = np.arange(1,6) 
y = np.arange(2,11,2)
fig,axes = plt.subplots(nrows=2,ncols=1,)
axes[0].plot(x,y,color="red")
axes[0].set_title("First Axes")
axes[1].plot(x,x**0.5,color="purple")
axes[1].set_title("Second Axes")

fig1 = plt.figure(figsize=(6,4))
axes1 = fig1.add_axes([0,0,1,1])
axes1.plot(x,x**0.5,color = "red",label = "x'in karekökü")
axes1.plot(x,x**2,color = "green",label = "x kare")

axes1.plot(x,x**3,color = "blue",label = "x küp")
axes1.legend()#labelların gözükmesi için 
plt.tight_layout()
plt.show()
fig.savefig("fig1.png")
fig1.savefig("fig2.png")
