import os
import glob

files = glob.glob(r'D:\Attachments\*')
for f in files:
    os.remove(f)


