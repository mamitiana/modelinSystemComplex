a = 1.1
x =1
t = 0

result = [x]
timesteps = [t]
from pylab import *

def update(a, x):
    return  a*x , t+0.1

for i in range(30):
    x , t= update(a, x)
    result.append(x)
    timesteps.append(t)
print(result)

plot(timesteps,result)
show()