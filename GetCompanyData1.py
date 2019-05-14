# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 08:27:14 2015

Gets company financial data from the Economic Times Website
for a range of companies whose URLs have been extracted by GetURLLinks program
and stored in a text file.

Writes the data into a another textfile

@author: hduser
"""

import urllib3
from bs4 import BeautifulSoup

f = open('GetCompanyDataOutput.csv','w')
f.write("Comp,Sales,OthOpInc,OpProfit,EBITDA,Interest,Dep,Tax,NetP,EPS"+"\n")

urlfile = open('GetURLLinksOutput-extract.txt', 'r')
url_list = list(urlfile)
#print ('url_list is {} '.format(urlfile))
for url in url_list:
    url = url.rstrip('\n')
    #print ('The URL is {} '.format(url))
    http = urllib3.PoolManager()
    page = http.request('GET',url)
    soup = BeautifulSoup(page.data)
    #http = urllib3.PoolManager()
    #page = http.request('GET',URL)
    #soup = BeautifulSoup(page.data,"lxml")
    #print (soup)
    spoon1 = soup.find_all(attrs={"class":"flt quartYear bold w132"})
    #print ('spoon1 is {} '.format(spoon1))
    Sales = spoon1[0].span.string.replace(",","")
    OthOpInc = spoon1[1].span.string.replace(",","")
    OpProfit = spoon1[2].span.string.replace(",","")
    OpInc = spoon1[3].span.string.replace(",","")
    EBITDA = spoon1[4].span.string.replace(",","")
    Interest = spoon1[5].span.string.replace(",","")
    Dep = spoon1[6].span.string.replace(",","")
    Tax = spoon1[7].span.string.replace(",","")
    NetP = spoon1[8].span.string.replace(",","")
    EPS = spoon1[9].span.string.replace(",","")
    
    #Comp = spoon2[0].span.string
    #print(Sales,OthOpInc,OpProfit, OpInc,EBITDA,Interest,Dep,Tax,NetP,EPS)
    
    title1 = soup.title.string
    print ('title is {} '.format(title1))
    #Com = title1.strip('Share')
    #Com = Com.strip('share')
    Share = title1.find("Share")
    share = title1.find("share")
    print ('Share {} '.format(Share))
    print ('share {} '.format(share))
    if (share == -1):
        Com = title1[:(title1.find("Share")-1)]
        Com = Com.rstrip()
        print ('Com1 is {} '.format(Com))
    elif (Share == -1):
        Com = title1[:(title1.find("share")-1)]
        Com = Com.rstrip()
        print ('Com1 is {} '.format(Com))

    #Com = Com[:(Com.find("share")-1)]
    #Com = Com.rstrip()
    #print ('Com2 is {} '.format(Com))
    f.write(Com+","+Sales+","+OthOpInc+","+OpProfit+","+EBITDA+","+Interest+","+Dep+","+Tax+","+NetP+","+EPS+"\n")
    
    
f.close()
urlfile.close()
