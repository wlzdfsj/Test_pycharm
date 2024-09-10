import numpy as np
#re库用于字符串的模式匹配
import re
import random
#读取文章，提取所有的单词，返回列表
def textParse(doc):
    list_of_tokens=re.split(' ',doc)
    return list_of_tokens

#将总单词列表转换成语料库
def createvocablist(doclist):
    vocabset=set([])  #采用集合，去掉重复词
    #doc代表每篇文章单词列表
    for doc in doclist:
      vocabset=vocabset|set(doc)   #取不重复的所有单词
    return list(vocabset)

#将文章转换成特征向量
def setofword2vec(doc,vocablist):
    vec=[0]*len(vocablist)
    for i in doc:
        #如果文章中的某个词在语料库中存在，则置为1
        if i in vocablist:
            vec[vocablist.index(i)]=1
    return vec

#朴素贝叶斯模型  || 训练模型需要执行的步骤，关键得出每个单词在垃圾文件、正常文件出现的概率 ||
def trainNB(trainmat,train_label):
    #文章总数
    numdocs=len(train_label)
    #每篇文章对应的特征向量的总长度=语料库中单词的总长度
    numwords=len(trainmat[0])
    #垃圾邮件出现的概率
    p1=sum(train_label)/float(numdocs)
    #统计语料库中所有单词在垃圾文件、正常文件中出现的次数
    p0num=np.ones((numwords)) #语料库中单词在正常文件中出现次数，用数组表示
    p1num=np.ones((numwords)) #语料库中单词在垃圾文件中出现次数，用数组表示
    p0down=2 #分母 设置成类别个数
    p1down=2
    #遍历所有文件，统计单词在垃圾文件、正常文件出现的文件总和
    for i in range(numdocs):
        if train_label[i]==1:  #垃圾文件
            p1num+=trainmat[i] #遍历所有垃圾文件，统计语料库中每个单词在垃圾文件出现的文件总和【0,8,11,8,2,0,13.。。。】
            p1down+=sum(trainmat[i]) #遍历所有垃圾文件，所有词出现的次数总和
        else:  #正常文件
            p0num += trainmat[i]  # 统计每个单词在正常文件中出现次数
            p0down += sum(trainmat[i])

    #统计概率
    p1vec=np.log(p1num/p1down) #语料库中每个单词在垃圾文件中出现概率 P(d1,d2,d3,d4....|垃圾文件)
    p0vec = np.log(p0num / p0down)
    return p0vec,p1vec,p1


#P(垃圾|邮件)=P(垃圾)*P(邮件|垃圾)/P(邮件)   P(邮件)=P(d1,d2,d3,d4,....)
#P(正常|邮件)=P(正常)*P(邮件|正常)/P(邮件)

#化简：不用考虑分母
#log[P(垃圾|邮件)]=log[P(垃圾)]+log[P(邮件|垃圾)]=log[P(垃圾)]+log[P(d1,d2,d3,d4,d5,...|垃圾)]=log[P(垃圾)]+log[P(d1|垃圾)]+log[P(d2|垃圾)]+...

#测试数据集需要执行的步骤，关键利用朴素贝叶斯公式，及训练模型时得出的概率，得出每篇文章所属的类别
def classifyNB(testmat,p0vec,p1vec,p):   #p0vec:统计所有正常邮件中，所有单词的概率  p:垃圾邮件概率
    p1=np.log(p)+sum(testmat*p1vec)  #testmat测试文本特征向量  将该篇文章当中出现的单词*它在垃圾邮件中出现的概率 求和
    p0 = np.log(1-p) + sum(testmat * p0vec)
    if p0>p1:
        return 0
    else:
        return 1

def spam():
    doclist=[]  #存放所有文章
    classlist=[] #存放文章对应标签
    for i in range(1,11):
        #1.读取文件,得到单词列表
        wordlist=textParse(open('email/spam/%d.txt'%i,'r').read())
        #2.将单词列表存放到总列表库中
        doclist.append(wordlist)
        classlist.append(1) #1代表垃圾文件

        # 1.读取文件,得到单词列表
        wordlist = textParse(open('email/ham/%d.txt' % i, 'r').read())
        # 2.将单词列表存放到总列表库中
        doclist.append(wordlist)
        classlist.append(0)  # 0代表正常文件
    #获取语料库
    vocablist=createvocablist(doclist)
    #切分训练数据集和测试数据集
    #print(doclist)
    train_data=[]
    train_label=[]
    test_data=[]
    test_label=[]
    index =random.sample(range(0,20),12)#取12个样本为数据集
    for i in range(20):
        if i in index:
            train_data.append(doclist[i])
            train_label.append(classlist[i])
        else:
            test_data.append(doclist[i])
            test_label.append(classlist[i])
    print(train_label)
    print(test_label)

    #训练数据集
    trainmat=[]  #存放所有文章的特征向量
    #构建特征向量
    for doc in train_data:
        vec=setofword2vec(doc,vocablist) #将文章转换成特征向量
        trainmat.append(vec)
    #训练模型   p0vec:单词在正常邮件中出现概率， p1vec：单词在垃圾邮件中出现概率，p1：垃圾邮件出现概率
    p0vec,p1vec,p1=trainNB(np.array(trainmat),np.array(train_label))
    #预测数据集
    result_label=[]
    for doc in test_data:
        vec=setofword2vec(doc,vocablist) #测试集的特征向量
        result=classifyNB(np.array(vec),p0vec,p1vec,p1)
        result_label.append(result)
    print(result_label)
    sam=0
    #计算准确率
    for i in range(len(result_label)):
        if result_label[i]==test_label[i]:
            sam+=1
    print(sam)
    print(f"原始:{test_label}\n预测:{result_label}\n准确率:{sam / len(test_label)}")


spam()


#步骤：1.读取所有文章，把这些文章放入一个列表中
#2.根据总的文章列表，获取语料库（去掉重复词）
#3.划分训练集和测试集
#4.训练模型，把所有的文章转换成特征向量
#5.采用朴素贝叶斯算法，计算垃圾邮件出现的概率p1、所有语料库中单词出现在垃圾文件概率p1vec、正常文件概率p0vec
#6.预测数据集，将每篇文章转换成特征向量，利用训练过程中得出的概率,预测其所属的类别
#7.将测试集中所有文章预测的类别与原来的类别做对比，查看其准确率