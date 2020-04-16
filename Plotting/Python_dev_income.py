from matplotlib import pyplot as plt

# Median Python Developer Salaries by Age
py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(py_dev_x, py_dev_y)
plt.xlabel('Age')
plt.ylabel('Salary (USD) ')
plt.title('Python Developer Salaries by Age')
plt.show()