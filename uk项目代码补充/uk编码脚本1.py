#coding:utf-8
import csv
import sys
type = sys.getfilesystemencoding()
print type

# 用来计算期货的合约日期
def number_factory (number):
    temp = number % 100
    if temp == 12:
        number = number + 100
        number = number - 11
        return number
    else:
        return number + 1

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

# 创建目标文件
goalfile =  file('csvresult_4.csv','wb')
writer = csv.writer(goalfile)
writer.writerow(['期货名称','合约代码','uk']);
#下面的这几重循环是用来计算10年期货的uk代码
calendar = 1607
for month in range(1400,1520):
#计算期货的日期
    calendar = number_factory(calendar)
    calendar_str = str(calendar)
    print calendar_str
    csvfile = file('hk.csv','rb')
    reader = csv.reader(csvfile)
    month_code = function_uk(month)
    counter = 1
    for line in reader:
        future_code = '00000000'
        temp = function_uk(counter)

#这里用来计算期货的代码
        change_cp = 8 - len(temp)
        for h in range(0,len(temp)):
            l = list(future_code)
            l[change_cp] = temp[h]
            future_code  = ''.join(l)
            change_cp = change_cp + 1

        uk = '401a2'+month_code + future_code
        # print '4a0a1'+month_code + future_code
        linedate = line[1] + calendar_str
        print linedate
        counter = counter + 1
        temp_2 = [(line[0],linedate,uk)]
        writer.writerows(temp_2)
    #     print '#############################'
    # print '++++++++++++++++++++++++++++++'
goalfile.close()
csvfile.close()