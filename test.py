import date
import viz
import pandas 
import csv
def datee():
    date
    viz
    df1 = pandas.read_csv('all.csv').replace("V","30")
    df2 = pandas.read_csv('viz.csv')


    res = pandas.concat([df1, df2],axis=1)

    res.to_csv('testdata.csv',index = False)

