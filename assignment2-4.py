import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('./stock_data_2.csv', sep=',')
new_cols = ['day','month','year']
for col in new_cols:
    df.insert(0,col,0)
df[['month','day','year']] = df['Date'].str.split('/', 2, expand=True)
df = df.sort_values(['year','month','day'], ascending=[True,True,True])

def median(df):
    midPos = df['Close'].count() // 2
    if df['Close'].count() % 2 == 0:
        median = (df.iloc[midPos,6] + df.iloc[midPos-1,6])/2
    else:
        median = df.iloc[midPos,6]
    return median

mean = df[['Open', 'Close']].mean(axis=1)
median = df[['Close']].median(axis=1)
updown = [0]
change = [0]
for i in range(1, len(df.Close)):
    updown.append(df.iloc[i, 6] - df.iloc[i-1, 6])
    change.append((df.iloc[i, 6] - df.iloc[i-1, 6])/df.iloc[i-1, 6])
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(df.Date, mean, label = 'mean', linewidth=0.5)
ax1.plot(df.Date, median, label = 'median', linewidth=0.5)
ax2.plot(df.Date, updown, label = 'updown', linewidth=0.5)
ax2.plot(df.Date, change, label = '%change', linewidth=0.5)
ax1.legend()
ax2.legend()
fig.suptitle('Stock Data')
plt.xlabel('Date')
plt.ylabel('Values')
plt.show()