#Imp_Apriori�ӿڵ��÷�ʽ��

#��ȡƵ����L����֧�ֶ�SupportData

L,SupportData = Imp_Apriori.apriori(dataset,minSupport)

#minSupportΪ��С֧�ֶ�
#datasetΪ��������ݼ�������ʽΪһ����ά�б�:[[],[],[],....,[]]�����б��е�С�б�������������˵Ĺ�Ʊ����

#��ȡǿ��������

rules = Imp_Apriori.generateRules(L,SupportData,minConf)

#rulesΪǿ��������minConfΪ��С���Ŷ�