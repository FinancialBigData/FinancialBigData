#Imp_Apriori接口调用方式：

#获取频繁集L及其支持度SupportData

L,SupportData = Imp_Apriori.apriori(dataset,minSupport)

#minSupport为最小支持度
#dataset为输入的数据集，其形式为一个二维列表:[[],[],[],....,[]]；大列表中的小列表包含当天上涨了的股票代号

#获取强关联规则

rules = Imp_Apriori.generateRules(L,SupportData,minConf)

#rules为强关联规则，minConf为最小置信度