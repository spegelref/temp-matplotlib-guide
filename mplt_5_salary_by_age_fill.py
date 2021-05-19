
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/developer_salaries.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444', linestyle='--',
         label='All devs')

plt.plot(ages, py_salaries, label='Python')

# overall_median = 57287

plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries > dev_salaries),
                 interpolate=True, alpha=0.25, label='Above avg.')

plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries <= dev_salaries),
                 interpolate=True, alpha=0.25, color='red',
                 label='Below avg.')


plt.legend()

plt.title('Median salary (USD) by Age')
plt.xlabel('Age')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()
plt.show()
