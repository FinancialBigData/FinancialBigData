import time
import copy
import itertools

def loadDataSet():
    return [['A','B','C','D'],['B','D','E','F'],['B','C','D'],['A','B','C','D','E','F'],['A','C','F'],['B','C','F'],['A','C','D'],['A','B','C','D','G'],['A','B','D','G']]

def createC1(dataSet):
    C1 = []
    C = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])

    C1.sort()
    return map(frozenset,C1)


def scanD(D,Ck,minSupport):
    ssCnt = {}
    a = time.clock()
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if not ssCnt.has_key(can): ssCnt[can] = 1
                else: ssCnt[can] +=1

    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support

    return retList,supportData

def aprioriGen(Lk,k):
    retList = []
    L = []
    lenLk = len(Lk)

    for i in range(lenLk):
        a = list(Lk[i])
        L.append(a)


    for i in range(lenLk):
        for j in range(i+1,lenLk):
            L1 = (L[i])[:k-2]; L2 = (L[j])[:k-2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(frozenset(L[i]) | frozenset(L[j]))

    return retList

def con_of_Lk(Lk):
    a = set([])
    for i in range(0,len(Lk)):
            a = set(Lk[i]|a)

    return a

def cut_Lk(Lk,k):

    ssCnt = {}
    a = []
    b = []
    for i in range(0,len(Lk)):
        for j in Lk[i]:
            if frozenset([j]) not in a:

                a.append(frozenset([j]))

    for i in range(0,len(Lk)):
        for j in a:
            if j.issubset(Lk[i]):
                if not ssCnt.has_key(j):
                    ssCnt[j] = 1
                    b.append(j)
                else: ssCnt[j] +=1

    for i in b:
        if(ssCnt[i]<k-1):
            for j in Lk:
                if i.issubset(j):
                    Lk.remove(j)
    return Lk


def New_scanD(D,minSupport):
    ssCnt = {}
    for i in D:
        two_dimen = list(itertools.combinations(list(i),2))
        for j in two_dimen:
            if not ssCnt.has_key(frozenset(j)):
                ssCnt[frozenset(j)] = 1
            else:
                ssCnt[frozenset(j)] += 1

    print "the length of C2" + str(len(ssCnt))

    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support
    print "len of retList" + str(len(retList))
    return retList,supportData

def apriori(dataSet,minSupport):
    C1 = createC1(dataSet)
    D = map(set,dataSet)
    L1,supportData = scanD(D,C1,minSupport)
    a = con_of_Lk(L1)

    for i in range(0,len(D)):
         D[i] = D[i] & a

    L = [L1]
    k = 2
    while (len(L[k-2])>0):
        start = time.clock()

        # LL = copy.deepcopy(L[k-2])
        # LL = cut_Lk(LL,k-1)
        #
        # Ck = aprioriGen(LL,k)
        if k == 2:
            start = time.clock()
            Lk,supK = New_scanD(D,minSupport)
            end = time.clock()
            print "time of New_scanD" + str(end-start)
        else:
            Ck = aprioriGen(L[k-2],k)
            print "the lengt of Ck" + str(len(Ck))
            middle = time.clock()
            print "time of aprioriGen:"+str(k) +":"+ str(middle-start)
            Lk, supK = scanD(D,Ck,minSupport)
            time1= time.clock()
            print "time of sacnD" + str(k) +":" + str(time1-middle)
        print "the length of Lk" + str(len(Lk))
        a = con_of_Lk(Lk)
        DD = copy.deepcopy(D)
        for i in range(0,len(D)):
                TS = copy.deepcopy(D[i])
                D[i] = D[i] & a
                if(len(D[i])<k+1):
                    DD.remove(TS)
                else:
                    DD.remove(TS)
                    DD.append(D[i])
        D = DD
        supportData.update(supK)
        L.append(Lk)
        k +=1

    return  L,supportData

def generateRules(L,supportData,minConf):
    bigRuleList = []
    for i in range(1,len(L)):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if (i>1):
                rulesFromConseq(freqSet,H1,supportData,bigRuleList,minConf)
            else:
                calcConf(freqSet,H1,supportData,bigRuleList,minConf)
    return bigRuleList

def calcConf(freqSet, H, supportData, br1, minConf):
    prunedH = []
    for conseq in H:
        conf = float(supportData[freqSet]) / float(supportData[freqSet-conseq])
        if (conf >= minConf):
            print freqSet-conseq,'-->',conseq,'conf:',conf
            br1.append((freqSet-conseq,conseq,conf))
            prunedH.append(conseq)
    return prunedH

def rulesFromConseq(freqSet, H, supportData, br1, minConf):
    m = len(H[0])
    if (len(freqSet) > (m+1)):
        if (m==1):
            Hmp1 = calcConf(freqSet, H, supportData,br1, minConf)

        Hmp1 = aprioriGen(H,m+1)
        Hmp1 = calcConf(freqSet, Hmp1, supportData,br1, minConf)
        if (len(Hmp1) > 1):
            rulesFromConseq(freqSet, Hmp1, supportData, br1, minConf)