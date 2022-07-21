import pandas as pd
import datetime as dt
import numpy as np
# import matplotlib.pyplot as plt
df=pd.read_excel("../TimeCard_Data.xlsx",sheet_name="TimeCard")
df['Date']= pd.to_datetime(df['Date'])
date_df=df
date_df['Date']=date_df['Date'].dt.strftime('%b')
rpivot=date_df.groupby('Date')["Billable Hour","Non Billable Hour"].agg([np.sum])
new_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rpivot = rpivot.reindex(new_order, axis=0)
rpivot.reset_index(inplace=True)
rpivot.columns = ['Date','Billable','Non-Billable']
print(rpivot)

# x = np.arange(len(rpivot['Date']))  # the label locations
# width = 0.40  # the width of the bars
# fig, ax = plt.subplots()
# rects1 = ax.bar(x - width/2, rpivot["Billable"], width, label='Billable')
# rects2 = ax.bar(rpivot['Date'] , rpivot["Non-Billable"], width, label='Non-Billable')

# ax.set_ylabel('Hrs')
# ax.set_xlabel("Months")
# ax.legend()
# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, padding=3)

# plt.figure(figsize=(32, 62))
# plt.show()


