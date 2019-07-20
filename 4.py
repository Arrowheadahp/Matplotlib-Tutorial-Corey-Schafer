from matplotlib import pyplot as plt

plt.style.use('ggplot')

stack=[1,2,3]

p1=[1,1,2]
p2=[2,2,3]
p3=[1,2,3]
labels=['p1', 'p2', 'p3']

plt.stackplot(stack, p1, p2, p3,
              labels = labels)

plt.title('Stackplot Title')
plt.savefig('graph4.png')
plt.legend(loc = 'upper left')
plt.show()
    
