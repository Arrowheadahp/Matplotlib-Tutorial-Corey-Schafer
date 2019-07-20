from matplotlib import pyplot as plt
from random import randint

plt.style.use('seaborn')

rn = range(20)

x= [randint(1,100) for i in rn]
y= [randint(1,100) for i in rn]


plt.scatter(x,y,
            s=40,       #size
            c='red',    #color
            #marker='x',
            edgecolor='black',
            alpha = 0.8,
            label = ''
            )

plt.scatter(y,x,
            s=40,       #size
            c='blue',    #color
            marker='x',
            edgecolor='black',
            alpha = 0.8,
            )


plt.savefig('graph7.png')
plt.show()
