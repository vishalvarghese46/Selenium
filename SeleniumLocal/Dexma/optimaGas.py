import pandas as pd
from ftplib import FTP
import glob, os, sys, shutil
import time

#clear everthing in the SendMe folder

old_sent_files = glob.glob(r'C:\Users\optimisedbuildings\Documents\Optima\SendMe\*')
for f in old_sent_files:
    os.remove(f)

#Parsing all the csv's

df = pd.concat([pd.read_csv(f) for f in glob.glob(r'C:\Users\optimisedbuildings\Documents\Optima\*.csv')], ignore_index = True)
df.drop(["Daily Total", "Max Reading","Min Reading","Data Source","Status","Unnamed: 59"], axis=1,inplace=True)
df['UNITS'] = df['UNITS'].map({'kWh':420})
df.drop_duplicates(keep='last', inplace=True)
df.sort_values(['OPTIMA Half Hourly DATA', 'READING DATE'], ascending='True', inplace = True)
df.to_csv(r"C:\Users\optimisedbuildings\Documents\Optima\SendMe.csv", index = False)

#FTP the SendMe.csv from the SendMe folder

print('''......
.... FTP'ing the csv now!!
......''')

time.sleep(5)

ftp = FTP('ftp.dexcell.com')
ftp.login(user='127005', passwd = '141559')#username & password
#ftp.cwd('Destination directory')


send_file = glob.glob(r'C:\Users\optimisedbuildings\Documents\Optima\SendMe\*.csv')
ftp.storlines("STOR " + os.path.basename(send_file), open(send_file,"rb"))
ftp.quit()
