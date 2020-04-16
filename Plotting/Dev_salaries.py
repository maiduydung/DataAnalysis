from matplotlib import pyplot as plt
import numpy as np



# Median Developer Salaries by Age
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

x_indexes = np.arange(len(ages_x))
print(x_indexes)
width = 0.25

#black line
plt.bar(x_indexes - width, dev_y, width = width, color="#444444", linestyle ='--', label = "All devs")

#blue line
plt.bar(x_indexes, py_dev_y, width = width, color="#008fd5" ,label = 'Python devs')

#red line
plt.bar(x_indexes + width, js_dev_y, width = width, color="#e5ae38", label='JS devs')


plt.xlabel('Age')
plt.ylabel('Salary (USD) ')
plt.title('Median salary by Age')
plt.legend()
plt.tight_layout()
plt.show()