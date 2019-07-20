from matplotlib import pyplot as plt
from random import randint

plt.style.use('fivethirtyeight')

ages=[randint(20,60) for i in range(1000)]
        #random ages

bins = range(18,65,1)
#print (sorted(ages))

plt.hist(ages,
         bins = bins,
         edgecolor = 'black',
         alpha = 0.4,
         log=True
         )

plt.axvline(40)

plt.title('HISTOGRAM')
plt.xlabel('Ages')
plt.ylabel('Frequency')

plt.savefig('graph6.png')
plt.show()

