from matplotlib import pyplot as plt

plt.style.use('ggplot')

'''slices = [60,40,30,20]
labels = ['Sixty', 'Forty', 'Thirty', 'Twenty']
colors = ['yellow', 'blue', 'green', 'red']'''

slices = [59219, 55466, 47544, 36443, 35917, 31991]

labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python',
          'Java', 'Bash/PowerShell']


explode = [0, 0, 0.1, 0, 0, 0]



for i in range(len(labels)):
    labels[i]+=':'+str(
        round((slices[i]/402056)*100,2))+'%'

slices.reverse()    #   this is to
labels.reverse()    #   look good


plt.pie(slices,
        labels = labels,
        wedgeprops = {'edgecolor':'black'},
        #colors = colors,
        explode = explode,
        shadow=True,
        startangle=90,
        autopct = '%1.2f%%'
        )

plt.title('Programming Languages')

plt.savefig('graph3.png')
plt.show()

