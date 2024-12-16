import pandas as pd
import numpy as np
import scipy.stats as stats


df = pd.read_csv('Seatdata.csv')
df = df.dropna()
 
def iz(col):
   # IQR Test
   print('Calculating Percentiles')
   print(f'{col:}\n')
   q1 = np.percentile(df[col], 25)
   q3 = np.percentile(df[col], 75)

   iqr = q3 - q1
   ub = q3 + 1.5 * iqr
   lb = q1 - 1.5 * iqr

   outliers = df[(df[col] > ub) | (df[col] < lb)].index
   
   print('IQR test finished successfully')

   #Z-score

   print('Calculating Z-score')
   idx = []
   zscore = stats.zscore(df[col])
   c = -1
   ocouter = 0 
   for i in zscore:
      c += 1
      if (i >= 3) or (i <= -3):
         idx.append(c)
         ocouter += 1

   print('dropping outliers')
   lst = []
   for i in outliers:
      lst.append(i)

   print(f'In {col}. deletion in progress... ')
   dele = []
   for i in lst:
      for j in idx:
         if i == j:
            dele.append(i)
   print(f'indexs similar in column "{col}". {dele}')

   df.drop(dele, axis = 0, inplace=True)

   print('Operation successfully completed with exit code 0')

for i in df.columns:
   iz(i)
   print('\n')