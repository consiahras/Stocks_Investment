import wget
import time

timestr= time.strftime("%Y%m%d")
ftp_url='ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt'
wget.download(ftp_url, out=("nasdaqlisted" + timestr))
