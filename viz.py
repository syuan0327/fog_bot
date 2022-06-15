#機場能見度
import datetime
from bs4 import BeautifulSoup
import requests,time
import csv
today=datetime.date.today()
yesterday=today-datetime.timedelta(days=1)
two_day=yesterday-datetime.timedelta(days=1)
three_day=two_day-datetime.timedelta(days=1)
date=[]

date.append(str(three_day))
date.append(str(two_day))
date.append(str(yesterday))


alll=[]
for time in range(3):
    data=[]
    datas=[]
    for hour in range(23):
        url='https://watch.ncdr.nat.gov.tw/php/list_vis_obs_csv.php?d='+date[time]+'&t='+str(hour)+':00'
        news1=requests.get(url)
        soup1=BeautifulSoup(news1.text,'html.parser')
        a=soup1.prettify().split('\n')
        data.append(a)
    del_num=[]
    for i in range(len(data)-1):
        for j in data[i]:
            datas.append(j.split(','))
    for i in range(len(datas)-1):
        if datas[i]==['']:
            del_num.append(i)
    for i in range(len(del_num)-1,-1,-1):
        datas.pop(del_num[i])

    table=[]
    for i in range(len(datas)-1):
        if (datas[i][1]=='金門機場') :
            a=int(datas[i][3])/1000                                                          
            table.append((datas[i][4]+' '+str(a)).split(' '))

    for i in range(4):
        alll.append(table[0][2])
    for i in range(len(table)-1):

        alll.append(table[i][2])
    for i in range(4):
        alll.append(table[16][2])

viz=[]
for i in alll:
    viz.append([i,1])
label=['VIZ','Label']

with open('viz.csv','w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(label)
  # 寫入二維表格
    writer.writerows(viz)