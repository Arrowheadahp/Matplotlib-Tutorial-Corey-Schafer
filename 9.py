from matplotlib import pyplot as plt
from random import choice
from matplotlib.animation import FuncAnimation
from itertools import count

plt.style.use('seaborn')

x = [0]
y = [0]

index = count(1)    #count is function that counts
                    #that is increases by 1 every time
                    #the function is encountered
                    #NO IDEA HOW THAT IS HELPFUL THOUGH

def animator(i):
    x.append(next(index))
    y.append(y[-1]+choice([-1, 0, 1]))

    if len(x)>100:
        x.pop(0)
        y.pop(0)

    plt.cla()       #cla is clear axis
    plt.plot(x, y)

anim = FuncAnimation(plt.gcf(), animator,
                     interval = 100)


plt.title('Realtime Plotting')
plt.xlabel('X Axis')
plt.ylabel('Values')

plt.savefig('graph9.png')
plt.show()
