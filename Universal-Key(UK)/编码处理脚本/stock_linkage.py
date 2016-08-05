#coding:utf-8
import  MySQLdb
import Apriori_support

def get_dataset(StartTime,EndTime,stock):

    time_length = []#用于存储每只股票存在数据的时间窗口长度
    dataset = []#用来存储每天上涨的股票
    data = {}#用来存储每支股票每天上涨情况

    try:
        conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',port=3306,db='stock_linkage')
        cursor = conn.cursor()

        for j in range(0,len(stock)):
            sql = "select price_change from" + "`" + stock[j] + "`" + "where date <= str_to_date('" + EndTime +"','%Y-%m-%d')"+ " and " + "date >= str_to_date('" + StartTime +"','%Y-%m-%d');"
            rs = cursor.execute(sql)#rs为该支股票存在数据的时间窗口长度
            print rs
            for i in range(0,rs):
                data[i] = 'kong'#初始化股票每天上涨情况,'kong'代表未上涨
                if(j == 0):
                    dataset.append([]) #初始化数据集，均为一个空列表

            time_length.append(rs)#存储查询结果窗口长度
            info = cursor.fetchmany(rs)#得到查询结果集

            i = 0
            for (updown,) in info:#遍历查询结果集，如果当天不是下降，就加入字典data[i] = stock[j]
                if(updown > 0):
                    data[i] = stock[j]
                i = i+1

            for i in data:
                if(data[i] != 'kong'):#将上涨股票代码加入数据集
                    try:
                        dataset[i].append(data[i])
                    except IndexError as e:
                       print "该时间窗口内股票数据不完全，请调整时间时间窗口后重新请求"
                       exit()

        for i in range(0,len(time_length)):#检查所有股票存在数据的时间长度是否相等，如果不等则不能得到结果数据集，退出程序
            if(time_length[0] != time_length[i]):
                print "该时间窗口内股票数据不完全，请调整时间时间窗口后重新请求"
                exit()

        cursor.close()
        conn.close()

    except MySQLdb.Error,e:
      print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    return dataset
def plate_linkage(stock,Startdate,EndDate,minSupport,minConf):

    dataset = []
    dataset_temp = get_dataset(Startdate,EndDate,stock)
    for i in dataset_temp:
        if (i != []):
             dataset.append(i)
    print len(dataset)

    L,SupportData = Apriori_support.apriori(dataset,minSupport)
    rules = Apriori_support.generateRules(L,SupportData,minConf)
    print rules

if __name__ == "__main__":
    stock = ['000006','000009','000010']
    plate_linkage(stock,'2016-01-04','2016-04-19',10,0.4)


