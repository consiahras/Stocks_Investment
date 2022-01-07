import wget
import time
import os

dest_dir='/home/ksiachras/Daily_nasdaq_file'
timestr= time.strftime("%Y%m%d")
now = time.time()
ftp_url='ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt'
wget.download(ftp_url, out= dest_dir)

#Remove the older files that downloaded before that are before 5min timestamp
print("Removing Older Files except the last file we downloaded")
for file in os.listdir(dest_dir):
    pathfile=os.path.join(dest_dir, file)
    if pathfile.startswith("nasdaq"):
        if os.stat(pathfile).st_mtime < now - 300:
            os.remove(os.path.join(dest_dir, file))
