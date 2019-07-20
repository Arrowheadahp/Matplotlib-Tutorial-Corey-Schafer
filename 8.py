from matplotlib import pyplot as plt
from datetime import datetime
from random import randint

plt.style.use('seaborn')

dates = [datetime(2019, 5, i) for i in range(24,31)]

y=[randint(0,9) for i in range(7)]

plt.plot_date(dates, y,
              linestyle = '-',
              )

plt.gcf().autofmt_xdate()   #gcf == get current figure

plt.title('Datetime Plots')
plt.xlabel('Dates')
plt.ylabel('Values')

plt.savefig('graph8.png')
plt.show()

