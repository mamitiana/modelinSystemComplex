from pylab import *

a = 2.1
b = -7.5

x = 50
t = 0

result = [x]
timesteps = [t]


def update(a, x_p, b):
    print(x_p)
    return a * x_p + b, t + 0.1


for i in range(200):
    print(i)
    x , t = update(a, result[-1], b)
    result.append(x)
    timesteps.append(t)
print(result)

plot(timesteps, result)
show()
