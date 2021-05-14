
import numpy as np
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

ages_x = [ 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35 ]

x_indices = np.arange(len(ages_x))
width = 0.25

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998,
            70003, 70000, 71496, 75370, 83640 ]

js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373,
            62375, 66674, 68745, 68746, 74583 ]

dev_y = [38496, 42000, 46752, 49320, 53200, 56000,
         62316, 64928, 67317, 68748, 73752 ]

plt.bar(x_indices - width, dev_y, width=width, color='#444444', label='All devs')
plt.bar(x_indices, py_dev_y, width=width, linewidth=3, label='Python')
plt.bar(x_indices + width, js_dev_y, width=width, linewidth=3, label='Javascript')

plt.xticks(ticks=x_indices, labels=ages_x)
plt.title('Median salary (USD) by Age')
plt.xlabel('Age')
plt.ylabel('Median salary (USD)')

plt.legend()

plt.tight_layout()

plt.show()
