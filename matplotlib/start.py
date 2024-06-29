import numpy as np
import matplotlib.pyplot as plt 

def f(x, a,b,c):
    return a * x**2 + b * x + c*x

x_data = np.linspace(-10,10, num=1000)
y_data = f(x_data, 3,2,4)

 
plt.show()