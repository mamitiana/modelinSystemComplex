from pylab import *

#a = 2.1
#b = -7.5

x = 1

t = 0

xresult = [x , x]

timesteps = [t]


def update( x_p,  x_pp ):

    x_next = x_pp + x_p
    return  x_next, t + 0.1


for i in range(2,30):

    x ,  t = update(xresult[-1],xresult[-2] )
    xresult.append(x)
    timesteps.append(t)
print(xresult)
plot( xresult  )

show()
