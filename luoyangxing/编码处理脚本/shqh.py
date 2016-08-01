#上海期货交易所编码代码
from xlrd import open_workbook
from xlutils.copy import copy
import os

def save(i,heyue,CODE):
    excel = r"D:\shqh.xls"
    rb = open_workbook(excel)
    wb = copy(rb)
    s = wb.get_sheet(0)
    s.write(i,0,"cc")
    s.write(i,1,heyue)
    s.write(i,2,CODE)
    s.write(i,3,"cc")
    os.remove(excel)
    wb.save(excel)


kindlist = ['cu','al','zn','pb','ni','sn','au','ag','rb','wr','hc','fu','bu','ru']
first32 = "404a2"

time = 1608
num = 1400
k = 1
for i in range(0,120):
    for j in range(0,len(kindlist)):
        if((time-13)%100==0):
            time = time - 13 + 101

        month = str(hex(num))[2:]
        if(len(month)) == 1:
            month = "00" + month
        if(len(month)) == 2:
            month = "0" + month
        kind = str(hex(j+1))[2:]

        print kindlist[j]+str(time)+" "+first32+month+"0000000"+kind
        heyue = kindlist[j]+str(time)
        CODE = first32+month+"0000000"+kind
        save(k,heyue,CODE)
        k = k + 1



    num = num + 1

    time = time + 1


