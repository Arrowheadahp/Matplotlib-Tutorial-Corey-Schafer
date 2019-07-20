from matplotlib import pyplot as plt

plt.style.use('ggplot')

slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097,
          23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]

labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java',
          'Bash/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript',
          'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']

l=range(len(slices))
for i in l:
    labels[i]+=': '+str(
        round((slices[i]/sum(slices))*100,2))+'%'

labels.reverse()
slices.reverse()

plt.barh(labels,slices)

#plt.xticks(ticks=l, labels=labels)
plt.title('Programming Languages')

plt.savefig('graph2_2.png')
plt.show()

