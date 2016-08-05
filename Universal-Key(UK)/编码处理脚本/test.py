import tushare as ts
from sqlalchemy import create_engine
engine = create_engine('mysql://root:123456@127.0.0.1/stock_linkage?charset=utf8')
df = ts.get_hist_data("000001")
print df
df.to_sql("000001",engine,if_exists='append')