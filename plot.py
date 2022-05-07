import matplotlib.pyplot as plt
import numpy as np

x =  np.array(range(0,100))
y = 1/(1+x/100) * 100



plt.scatter(x[30],y[30])
plt.plot(x,y,color='b')
plt.show()