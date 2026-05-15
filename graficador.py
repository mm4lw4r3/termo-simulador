import numpy as np
import matplotlib.pyplot as plt
import os

x = np.linspace(0,10,100)
y = np.sin(x)

plt.plot(x,y)
plt.title("Funcion seno")
os.makedirs('graficas', exist_ok=True)
plt.savefig('graficas/grafica.png')