from pylab import *

#a = 2.1
#b = -7.5

x = 1
y = 1

t = 0

xresult = [x]
yresult = [y]
timesteps = [t]


def update( x_p,  y_p ):

    x_next = 0.56* x_p + y_p
    y_next = -0.5*x_p + 0.5*y_p
    return  x_next, y_next ,t + 0.1


for i in range(300):
    print(i)
    x , y , t = update(xresult[-1], yresult[-1] )
    xresult.append(x)
    yresult.append(y)
    timesteps.append(t)

plot( xresult ,yresult, )

show()
