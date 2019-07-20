from matplotlib import pyplot as plt

plt.style.use('ggplot')

xaxis = list([0.1*i for i in range(21)])
sqplot = list([i*i for i in xaxis])
sqrplot = list([i**0.5 for i in xaxis])
bs=1

plt.plot(xaxis,
         sqrplot,
         label='sqroot')
                                #THE WHERE ARGUMENT IS NOT WORKING IN THE FILL_BETWEEN FUNCTION
plt.plot(xaxis,
         xaxis,
         label='linear',
         linestyle='--')

plt.plot(xaxis,
         sqplot,
         label='square')


plt.fill_between(xaxis,     #x axis here
                 sqplot,    #line plot for filling
                 color = 'green',
                 alpha = 0.35,  #opacity determination
                 label = 'sqroot integ')

plt.fill_between(xaxis,
                 [i**0.5 for i in xaxis],#for bound
                 xaxis,          #for another bound
                 color = 'red',
                 alpha = 0.25,
                 label = 'btn sq and lin')

plt.fill_between(xaxis,
                 xaxis,
                 sqplot,
                 where = (xaxis > sqplot),
                 color = 'brown',
                 alpha = 0.25,
                 label = 'x>x**0.5')

plt.fill_between(xaxis,
                 sqrplot,
                 sqplot,
                 where=(sqrplot < sqplot),
                 color = 'yellow',
                 alpha = 0.25,
                 label = 'x*x < x**0.5')
                 

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

plt.savefig('graph5.png')
plt.show()
