import pandas as pd
import glob
import os

old_sent_files = glob.glob(r'C:\Users\Optimised\Data Analysis with  Python\Override\Report Result\*')
for f in old_sent_files:
	os.remove(f)

df=pd.concat([pd.read_csv(f) for f in glob.glob(r"C:\Users\Optimised\Data Analysis with  Python\Override\*.csv")], ignore_index = True)
df['Point Name'] = df['Point Name'].str.replace('Number','#Number')
dftest=df.pivot(index="Store Name", columns="Point Name", values="Value")
dftest.to_excel(r"C:\Users\Optimised\Data Analysis with  Python\Override\Report Result\report.xlsx")

#data = glob.glob(r'C:\Users\Optimised\Data Analysis with  Python\Override\*.csv')
#for f in data:
#    os.remove(f)
#print('''All done! bye bye now...''')
