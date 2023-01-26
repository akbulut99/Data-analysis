import matplotlib.pyplot as plt 
import numpy as np 
x = np.arange(1,6) 
y = np.arange(2,11,2)

fig,axes = plt.subplots(nrows=2,ncols=1)  #2 satırı ve 2 sütunu olan bir tuple gibi yapı oluşturduk


fig = plt.figure(figsize=(4,4))
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y,color = "yellow")

plt.tight_layout() #grafiklerin daha güzel durmasını sağlar :)

plt.show()