from matplotlib import pyplot as plt
from random import randint
from matplotlib.animation import FuncAnimation
from itertools import count

plt.style.use('seaborn')

x = list(range(20))
y = [randint(0,9) for i in x]

index = count(20)     #count is function that counts
                    #that is increases by 1 every time
                    #the function is encountered
                    #NO IDEA HOW THAT IS HELPFUL THOUGH

def animator(i):
    global x,y
    x.append(next(index))
    y.append(randint(0, 9))
    x.pop(0)
    y.pop(0)

    plt.cla()       #cla is clear axis
    plt.plot(x, y)

anim = FuncAnimation(plt.gcf(), animator,
                     interval = 1000)


plt.title('Realtime Plotting')
plt.xlabel('X Axis')
plt.ylabel('Values')

plt.savefig('graph9_2.png')
plt.show()
