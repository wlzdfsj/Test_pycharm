import os
import numpy as np
from collections import Counter
import math
#语料库
strs=['我 喜欢 旅行 这 还 原来',
     '你 好 中国 我 爱 你 谢谢 你',
     '原来 你 还 在 这里 等 我 你 在',
     '中国 运动 健儿 胜利 在 望 胜利 这 个 中国',
     '春天 已经 来 了 ，万物 复苏 已经 定 还 在'
    ]
#####手动获取tf-idf

#1.词袋统计
words_list=[]
for item in strs:
    words_list.append(item.split())
print(words_list)
#2.统计词的数量
count_list=[]#count_list存放所有文章
for item in words_list:
    coun=Counter(item)  #自动统计列表中每个词出现次数  {'我': 1, '喜欢': 1, '旅行': 1}
    count_list.append(coun)
print(count_list)
#3.定义函数
def tf(word,count):
    return count[word]/sum(count.values())
def idf(word,count_list):  #count_list存放所有文章
    contain=0 #单词存在的文章数
    for text in count_list:  #遍历所有文章，计算每个单词出现的文章次数
        if word in text:
            contain+1
    return math.log(len(count_list)/(1+contain))
def tf_idf(word,count,count_list):
    return tf(word,count)*idf(word,count_list)
#4.输出结果
for index,text in enumerate(count_list): #enumerate（list）将列表转换成字典
    print("第{}个文档的TF-IDF信息为：".format(index+1))
    scores={}
    for word in text:
        tf_idfs=tf_idf(word,text,count_list) #计算每个单词的tf_idf值，存入字典
        scores[word]=tf_idfs
    for word,score in scores.items(): #遍历字典数据
        print("单词：{}，TF-IDF值为：{}".format(word,score))
print("---------------------------------------------------------")
#--------------------------------------------------------------------------
#通过sklearn获取tf-idf
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vec=TfidfVectorizer()
tfidf_matrix=tfidf_vec.fit_transform(strs) #将语料库文本数据转换成特征向量，矩阵
print(tfidf_vec.get_feature_names_out())#得到语料库所有不重复的词,直接将停用词去掉了
print(tfidf_vec.vocabulary_)#得到不重复的关键词对应id
print(tfidf_matrix.toarray()) #获取关键词的tf-idf值输出