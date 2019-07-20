from matplotlib import pyplot as plt
import numpy as np

X=range(11)
ax=np.arange(11)
print (ax+0.5)
width=0.26

plt.style.use('ggplot')

plt.bar(ax-width,[i for i in range(11)], width=width, label='1')
plt.bar(ax,[i*1.5 for i in range(11)], width=width, label='1.5')
plt.bar(ax+width,[i*2 for i in range(11)], width=width, label='2')

plt.xticks(ticks=ax, labels=X)

plt.title('Hello Graphs')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

plt.tight_layout()

plt.savefig('graph2.png')
plt.show()
