from matplotlib import pyplot as plt
from random import randint

plt.style.use('ggplot')

rn = range(20)

x= [randint(1,100) for i in rn]
y= [randint(1,100) for i in rn]

colors = [randint(1,9) for i in rn]


plt.scatter(y,x,
            s=40,           #size
            c=colors,       #color
            cmap = 'Reds',  #colormap without which grey
            #marker='x',
            edgecolor='black',
            alpha = 0.8,
            )

colbar = plt.colorbar()
colbar.set_label('Intensity')

#plt.legend()

plt.savefig('graph7.png')
plt.show()
