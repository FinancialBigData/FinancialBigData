import re
import os
from xlrd import open_workbook
from xlwt import easyxf
from xlutils.copy import copy

def save(i,a):
   excel = r"D:\shdfz.xls"
   rb = open_workbook(excel)
   wb = copy(rb)
   s = wb.get_sheet(0)
   s.write(i,21,a)
   os.remove(excel)
   wb.save(excel)


i = 1
for line in open(r"D:\shdfz.txt"):
    if line:
        try:
            date = re.search("\d\d\d\d-\d\d-\d\d\|\d\d\d\d\-\d\d-\d\d",line)
            date = date.group()
            date = date.split("|")[1]
            year = date[0:4]
            month = date[5:7]
            print year
            print month
            year = int(year)
            month = int(month)
            deadline = (year - 1900) * 12 + month
            print deadline
            deadline = hex(deadline)
            deadline = str(deadline)[2:]

            sequence = hex(i)
            sequence = str(sequence)[2:]
            if(len(sequence) == 1):
                sequence = "000" + sequence
            else:
                if(len(sequence)==2):
                    sequence = "00" + sequence
                else:
                    if(len(sequence)==3):
                        sequence = "0" + sequence

            UK = "40225" + deadline + "0000" + sequence
            print UK
            save(i,UK)
            i = i + 1
        except Exception as e:
            print e.message
