#coding:utf-8
import csv

def function_uk(code):
    result = ''
    warehouse = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'];
#无限循环使用了连续取余的方法得到16进制的每一位数字
    while 1:
        temp = divmod(code,16);
        code = temp[0]
        result = result + warehouse[temp[1]]
        if code == 0:
            break;
        else:
            continue;
    order = []
#这个循环用来逆序输出我们拼接的余数的字符串
    for i in result:
        order.append(i)
    order.reverse()
    return ''.join(order)

def date_code(year,month):
    result = 1
    result = function_uk((year - 1900)*12 + month)
    return  result

goalfile = file('SZAZR.csv','wb')
writer = csv.writer(goalfile)
csvfile = file('SZAZ.csv','rb')
reader = csv.reader(csvfile)

counter = 1
begin = '40123'
for line in reader:
    year = int(line[2].split('/')[0])
    month = int(line[2].split('/')[1])
    date = date_code(year,month)
    future_code = '00000000'
    temp = function_uk(counter)
    change_cp = 8 - len(temp)
    for h in range(0,len(temp)):
        l = list(future_code)
        l[change_cp] = temp[h]
        future_code = ''.join(l)
        change_cp = change_cp + 1
    counter = counter + 1
    uk = begin + date + future_code
    temp_1 = [(line[0],line[2],uk)]
    writer.writerows(temp_1)
goalfile.close()
csvfile.close()