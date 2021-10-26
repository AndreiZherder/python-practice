import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)
y = np.sin(x)
plt.figure()
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = sin(x)')
plt.show()

