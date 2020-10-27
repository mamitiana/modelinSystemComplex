a = 1.1
x =1
result = [x]
from pylab import *

def update(a, x):
    return  a*x

for i in range(30):
    x = update(a, x)
    result.append(x)
print(result)

plot(result)
show()