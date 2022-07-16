from re import A
import numpy as np
import matplotlib.pyplot as plt
t = range(30)
v = 5 * np.sin(t) + np.random.randn(30)

v_kalman = np.zeros(v.shape)
gain = np.zeros(v.shape)
x = 0  # state, x(k) = a * x(k-1) + b * u(k)
a = 1  # state transfer matrix
b = 0  # control matrix
h = 1  # observer matrix
p = 0  # estimate cov
q = 0.002  # process cov
r = 0.05  # observer cov
g = 0  #  kalman gain
print("size: ", v.size)
for i in range(len(v)):
    x = a * x 
    p = a * p * a + q

    g = p * h / (h * p * h + r)
    x = x + g * (v[i] - h * x)
    p = (1 - g * h) * p
    
    v_kalman[i] = x
    gain[i] = g
print(v_kalman)
plt.plot(v,"--")
plt.plot(v_kalman)
plt.show()

