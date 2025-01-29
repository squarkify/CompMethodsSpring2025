"""This program will do calculate 
Emily Maher January 25, 2024"""

import numpy as np


#calcaulting average velocties
x = np.array([2.0, 2.2, 0.0, -1.5, -2.8])
t = np.array([0.0,1.0, 2.0, 3.0, 4.0])

v1 = (x[1] - x[0])/(t[1]-t[0])
print("v1 = {:.2f}".format(v1))
v2 = (x[2] - x[1])/(t[2]-t[1])
print("v2 = {:.2f}".format(v2))
v3 = (x[3] - x[2])/(t[3]-t[2])
print("v3 = {:.2f}".format(v3))
v4 = (x[4] - x[3])/(t[4]-t[3])
print("v4 = {:.2f}".format(v4))



#introducing loops
r = [1,3,5]
for n in r:
    print(n)
    print(2*n)
print("Finished")

#Using a loop to calcaulte average velocity
Vavg = np.empty(4)
for n in range(4):
    Vavg[n] = (x[n+1]-x[n])/(t[n+1]-t[n])
    print("v_", n, "= {:.2f}".format(Vavg[n]), sep="")
