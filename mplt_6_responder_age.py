
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data/ages.csv')
ids = data['Responder_id']
ages = data['Age']

median_age = 29
color = '#fc4f30'

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins=bins, edgecolor='black', log=True)
plt.axvline(median_age, color=color, label='Age median', linewidth=2)

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total respondents')

plt.tight_layout()

plt.show()
