import datetime
import requests
import csv,time
from bs4 import BeautifulSoup

label=['time','temp','dpTemp','RH','WDIR']
with open('all.csv','w',newline='')as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(label)


today=datetime.date.today()
yesterday=today-datetime.timedelta(days=1)
two_day=yesterday-datetime.timedelta(days=1)
three_day=two_day-datetime.timedelta(days=1)
date=[]

date.append(str(three_day))
date.append(str(two_day))
date.append(str(yesterday))

datelist=[]
datelist.append(three_day.strftime('%Y/%m/%d'))
datelist.append(two_day.strftime('%Y/%m/%d'))
datelist.append(yesterday.strftime('%Y/%m/%d'))

for i in range(len(date)):
    url='https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467110&stname=%25E9%2587%2591%25E9%2596%2580&datepicker='+date[i]+'&altitude=47.9m'
    print(url)
    htmlFile=requests.get(url)
        
    objSoup=BeautifulSoup(htmlFile.text,'html.parser') #解析網站
    txt=objSoup.text.split() #以split分隔讀取到的網頁內容並存成list  
    start=60
    m=0
    table=[]
    while m < 24:
        a=[]
        for j in range(start,start+8): #j為讀取標題，時間、溫度等24筆
            a.append(txt[j])  
        table.append([datelist[i]+'-'+a[0],a[3],a[4],a[5],a[7]])
        start+=17
        m+=1
    with open('all.csv','a',newline='')as csvfile:
        writer = csv.writer(csvfile)

        # 寫入二維表格
        writer.writerows(table)
    



