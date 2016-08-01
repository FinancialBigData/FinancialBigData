#大连商品交易所编码代码
from xlrd import open_workbook
from xlutils.copy import copy
import os

def save(i,heyue,CODE):
    excel = r"D:\dlsp.xls"
    rb = open_workbook(excel)
    wb = copy(rb)
    s = wb.get_sheet(0)
    s.write(i,0,"cc")
    s.write(i,1,heyue)
    s.write(i,2,CODE)
    s.write(i,3,"cc")
    os.remove(excel)
    wb.save(excel)


kindlist = ['C','CS','A','B','M','Y','P','JD','BB','FB','L','V','PP','J','JM','I']
first32 = "406a2"

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
        if(len(kind)==1):
            kind = "0000000" + kind
        else:
            if(len(kind)==2):
                kind = "000000" + kind
            else:
                if(len(kind == 3)):
                    kind = "00000" + kind



        heyue = kindlist[j]+str(time)
        CODE = first32+month+kind
        print heyue + " " + CODE
        save(k,heyue,CODE)
        k = k + 1



    num = num + 1

    time = time + 1


