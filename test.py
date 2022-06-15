import date
import viz
import pandas 
import csv
import model

date
viz
df1 = pandas.read_csv('all.csv').replace("V","30")
df2 = pandas.read_csv('viz.csv')
res = pandas.concat([df1, df2],axis=1)
res.to_csv('testdata.csv',index = False)

model

data=[]
with open('ans.csv', newline='',encoding='utf-8') as csvfile:

     # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    for row in rows:
      
        data.append(row[0])

ans=data[1]
print(ans)







