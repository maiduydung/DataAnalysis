from matplotlib import pyplot as plt



slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]

colors = ['']

plt.pie(slices, wedgeprops={'edgecolor':'black'},labels = labels,
        explode= explode, autopct='%1.1f%%')

plt.title("Most used languages")
plt.tight_layout()
plt.show()