from sqlalchemy import create_engine

import tushare as ts

file = open("D:\sh.txt")
engine = create_engine('mysql://root:123456@127.0.0.1/stock_linkage?charset=utf8')
while 1:
    line = file.readline()
    if not line:
        break
    line = line[:-1]
    df = ts.get_hist_data(line)
    print df
    try:
        df.to_sql(line,engine,if_exists='append')
    except Exception as e:
        try:
            df.to_sql(line,engine,if_exists='append')
        except AttributeError:
            print "error"
