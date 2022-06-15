import csv

def nn():
    data=[]
    with open('ans.csv', newline='',encoding='utf-8') as csvfile:

     # 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)
        for row in rows:
      
            data.append(row[0])

    ans=data[1]
    return ans


