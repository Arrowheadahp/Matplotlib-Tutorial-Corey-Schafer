from matplotlib import pyplot as plt

plt.style.use('ggplot')

plt.plot([0.1*i for i in range(11)],[(0.1*i)**0.5 for i in range(11)],label='sqroot')

plt.plot([0.1*i for i in range(11)],[0.1*i for i in range(11)],label='linear')

plt.plot([0.1*i for i in range(11)],[0.01*i*i for i in range(11)],label='square')

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

plt.savefig('graph1.png')
plt.show()
