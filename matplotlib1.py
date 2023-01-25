import matplotlib.pyplot as plt 
import numpy as np
x = np.arange(1,6)
y = np.arange(2,11,2)
plt.plot(x,y,"red")#x ve y grafiği

plt.subplot(2,2,1)
plt.plot(x,y,"blue")

plt.subplot(2,2,2)
plt.plot(x,y,"green")

plt.subplot(2,2,3)
plt.plot(x,y,"yellow")

plt.subplot(2,2,4)
plt.plot(x,y,"black")
plt.show() 