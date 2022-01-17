import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

cwd = os.getcwd()
_DATA_PATH = os.path.join(cwd, 'data')

df = pd.read_csv(os.path.join(_DATA_PATH, 'prices_summary-market1.csv'))

ax = plt.gca()
plt.ylabel('Price')
line1 = df.plot.line(x='period', y='price', ax=ax, marker='o')
line2 = df.plot.line(x='period', y='expected', ax=ax, style=':', color='darkgrey')

plt.xticks(np.arange(0, df['period'].max()+1, 1.0))
plt.xlim((.5,df['period'].max()+.5))


plt.xlabel('Trading Period')

### Add a table with additional market information to the plot
#Include a table that contains dividend, number of contracts and number of participants for each trading period.

rows = ['dividend', 'contracts', 'began_round']
cell_text = []
cell_text.append(['%d' % (df['dividend'][x]) for x in range(df.shape[0])])
cell_text.append(['%d' % (df['contracts'][x]) for x in range(df.shape[0])])
cell_text.append(['%d' % (df['participants'][x]) for x in range(df.shape[0])])

print(cell_text)

### Position table

#The table will appear at the top the of the plot.

the_table = plt.table(cellText = cell_text,
    rowLabels = rows,
    loc='top',
)

### Prices in each period
plt.subplots_adjust(left=0.2, bottom=0.2)
plt.show()
