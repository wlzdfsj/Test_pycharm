from pprint import pprint
import numpy as np
dataset = np.array([
    # 色泽,根蒂,敲击,纹理,脐部,触感, 好坏
    ['青绿', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', '好瓜'],
    ['乌黑', '蜷缩', '沉闷', '清晰', '凹陷', '硬滑', '好瓜'],
    ['乌黑', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', '好瓜'],
    ['青绿', '蜷缩', '沉闷', '清晰', '凹陷', '硬滑', '好瓜'],
    ['浅白', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', '好瓜'],
    ['青绿', '稍蜷', '浊响', '清晰', '稍凹', '软粘', '好瓜'],
    ['乌黑', '稍蜷', '浊响', '稍糊', '稍凹', '软粘', '好瓜'],
    ['乌黑', '稍蜷', '浊响', '清晰', '稍凹', '硬滑', '好瓜'],
    ['乌黑', '稍蜷', '沉闷', '稍糊', '稍凹', '硬滑', '坏瓜'],
    ['青绿', '硬挺', '清脆', '清晰', '平坦', '软粘', '坏瓜'],
    ['浅白', '硬挺', '清脆', '模糊', '平坦', '硬滑', '坏瓜'],
    ['浅白', '蜷缩', '浊响', '模糊', '平坦', '软粘', '坏瓜'],
    ['青绿', '稍蜷', '浊响', '稍糊', '凹陷', '硬滑', '坏瓜'],
    ['浅白', '稍蜷', '沉闷', '稍糊', '凹陷', '硬滑', '坏瓜'],
    ['乌黑', '稍蜷', '浊响', '清晰', '稍凹', '软粘', '坏瓜'],
    ['浅白', '蜷缩', '浊响', '模糊', '平坦', '硬滑', '坏瓜'],
    ['青绿', '蜷缩', '沉闷', '稍糊', '稍凹', '硬滑', '坏瓜']
])

features = {
    '色泽': ['青绿', '乌黑', '浅白'],
    '根蒂': ['蜷缩', '稍蜷', '硬挺'],
    '敲击': ['浊响', '沉闷', '清脆'],
    '纹理': ['清晰', '稍糊', '模糊'],
    '脐部': ['凹陷', '稍凹', '平坦'],
    '触感': ['硬滑', '软粘']
}

labels = ["好瓜", "坏瓜"]
#p(好瓜|青绿,蜷缩,浊响,清晰,凹陷,硬滑)=p(好瓜)*p(青绿,蜷缩,浊响,清晰,凹陷,硬滑|好瓜)/p(青绿,蜷缩,浊响,清晰,凹陷,硬滑)
                        #       =p(好瓜)*p(青绿,蜷缩,浊响,清晰,凹陷,硬滑|好瓜)/p(好瓜)*p(青绿,蜷缩,浊响,清晰,凹陷,硬滑|好瓜)+p(坏瓜)*p(青绿,蜷缩,浊响,清晰,凹陷,硬滑|坏瓜)
#p(青绿,蜷缩,浊响,清晰,凹陷,硬滑|好瓜)=p(青绿|好瓜)*p(蜷缩|好瓜)*p(浊响|好瓜)*p(清晰|好瓜)*p(凹陷|好瓜)*p(硬滑|好瓜)

#实例代表朴素贝叶斯分类器
class Bayes:
    def __init__(self, features: dict, labels: list) -> None:  #初始化模型
        self.features = features #每个特征类别（如色泽、根蒂...）取值范围
        self.labels = labels  #好瓜、坏瓜
        self.feature_classes = list(self.features.keys()) #特征类别   # 色泽,根蒂,敲击,纹理,脐部,触感, 好坏
        self.condi_prob = {} #保存条件概率的字典  存放每种瓜对应所有可能的特征概率
        self.prior_prob = {} #保存先验概率的字典  存放好瓜和坏瓜的概率
        self._statistic = {}  #_statistic:统计所有可能瓜的数量{'好瓜':10,'好瓜.色泽.青绿':3,'好瓜.色泽.乌黑':1,....‘坏瓜’:5,'坏瓜.色泽.青绿':1....}
        self._samples = 0#样本个数
        for i in self.labels: #好瓜、坏瓜
            self.prior_prob[i] = 1 / len(self.labels) #各标签初试概率相等0.5 {'坏瓜': 0.5, '好瓜': 0.5}
            self.condi_prob[i] = {} #每个标签初始化一个空的字典存储条件概率#condi_prob{}: {'好瓜':{'色泽':{'青绿':0.2,'乌黑':0.13,'浅白':0.23},'根蒂':{...}...},'坏瓜':{'色泽':{}}}
            self._statistic[i] = 0 #每个标签的样本数清零
            for j in self.feature_classes:  # 色泽,根蒂,敲击,纹理,脐部,触感, 好坏
                self.condi_prob[i][j] = {} #{'好瓜':{'色泽':{}},'坏瓜':{'色泽':{}}}
                for k in self.features[j]:#遍历['青绿', '乌黑', '浅白']
                    self.condi_prob[i][j][k] = 1 / len(self.features[j])#好瓜、色泽、青绿的初试概率1/3  #{'好瓜':{'色泽':{'青绿':0.3,'乌黑':0.3,'浅白':0.3},'根蒂':{...}...},'坏瓜':{'色泽':{}}}
                    self._statistic['.'.join([i, j, k])] = 0 # {'好瓜':0,'好瓜.色泽.青绿':0,'好瓜.色泽.乌黑':0,....‘坏瓜’:0,'坏瓜.色泽.青绿':0....}

    # p(好瓜|青绿,蜷缩,浊响,清晰,凹陷,硬滑)=p(好瓜)*p(青绿,蜷缩,浊响,清晰,凹陷,硬滑|好瓜)/p(青绿,蜷缩,浊响,清晰,凹陷,硬滑)
    # =p(好瓜)*p(青绿,蜷缩,浊响,清晰,凹陷,硬滑|好瓜)/p(好瓜)*p(青绿,蜷缩,浊响,清晰,凹陷,硬滑|好瓜)+p(坏瓜)*p(青绿,蜷缩,浊响,清晰,凹陷,硬滑|坏瓜)

    #p(坏瓜|青绿,蜷缩,浊响,清晰,凹陷,硬滑)
    #=p(坏瓜)*p(青绿,蜷缩,浊响,清晰,凹陷,硬滑|坏瓜)/p(坏瓜)*p(青绿,蜷缩,浊响,清晰,凹陷,硬滑|坏瓜)+p(好瓜)*p(青绿,蜷缩,浊响,清晰,凹陷,硬滑|好瓜)
    #由于分母相同，则不用考虑，只需要比较分子即可
    def bayes_prob(self, arr): # 计算每个样本arr属于好瓜和坏瓜的概率
        plist = []
        for i in self.labels:
            idx = 0
            p = self.prior_prob[i]  #prior_prob{}存放的是好瓜和坏瓜的概率
            for j in self.feature_classes:
                p *= self.condi_prob[i][j][arr[idx]] #p=p(好瓜)*p(青绿|好瓜)*p(蜷缩|好瓜)....
                idx += 1
            plist.append(p)  #添加到列表的概率是p(好瓜)*p(青绿,蜷缩,浊响,清晰,凹陷,硬滑|好瓜)   及  p(坏瓜)*p(青绿,蜷缩,浊响,清晰,凹陷,硬滑|坏瓜) 只需要分子比较就行
        return plist

    def train(self, X, Y): #训练数据   X为特征,Y为标签 ,都为列表
        rows, cols = X.shape
        #_statistic:统计所有可能瓜的数量{'好瓜':10,'好瓜.色泽.青绿':3,'好瓜.色泽.乌黑':1,....‘坏瓜’:5,'坏瓜.色泽.青绿':1....}
        #统计数量，如好瓜：10个，好瓜.青绿=3个，好瓜.蜷缩=4个...
        for i in range(rows):  #遍历每个样本，将每个样本的特征数量计算出来，如好瓜.青绿=10,好瓜.蜷缩=4...
            self._statistic[Y[i]] += 1  #好瓜、坏瓜计数{'好瓜':13,'好瓜.色泽.青绿':0,'好瓜.色泽.乌黑':0,....‘坏瓜’:7...}
            for j in range(cols):
                self._statistic['.'.join([Y[i], self.feature_classes[j], X[i, j]])] += 1# ['好瓜.色泽.青绿']+=1、['好瓜.根蒂.蜷缩']+=1
            self._samples += 1 #总的样本数量
        #数量计算后，开始算概率,如好瓜：0.2，好瓜.青绿=0.001，好瓜.蜷缩=0.014...
        for i in self.labels:  #prior_prob{}:计算好瓜和坏瓜的概率
            self.prior_prob[i] = (self._statistic[i] + 1) / (self._samples+len(self.labels)) #好瓜、坏瓜数量/总的样本数量
            for j in self.feature_classes: # 色泽,根蒂,敲击,纹理,脐部,触感, 好坏
                for k in self.features[j]:#['青绿', '乌黑', '浅白']...
                    self.condi_prob[i][j][k] = (self._statistic['.'.join([i, j, k])] + 1) / (self._statistic[i] + len(self.features[j]))
                    #condi_prob{}: {'好瓜':{'色泽':{'青绿':0.2,'乌黑':0.13,'浅白':0.23},'根蒂':{...}...},'坏瓜':{'色泽':{}}}
    def predic(self, X): #模型推理 测试每个样本所属的类别是否与先前给出的类别一致
        rows, cols = X.shape
        res = [] #存放的是每个样本属于好瓜和坏瓜的概率，最后转化成0或者1表示
        for i in range(rows):
            y = self.bayes_prob(X[i]) #计算['青绿' '蜷缩' '浊响' '清晰' '凹陷' '硬滑']在好瓜和坏瓜的情况下概率，['乌黑' '蜷缩' '沉闷' '清晰' '凹陷' '硬滑']在好瓜和坏瓜的情况下概率
            res.append(y)
        res = np.argmax(res, axis=1) #如果第一个样本属于好瓜概率是0.5，而属于坏瓜概率0.1，则认为是好瓜，取好瓜所在的下标0
        res = [self.labels[x] for x in res] #将0,1变成好瓜和坏瓜['好瓜','好瓜','好瓜','好瓜','好瓜',......]
        return np.array(res)

    def show_params(self) -> str: #辅助函数，观察模型内部
        pprint(self.prior_prob)
        pprint(self.condi_prob , sort_dicts=False)
        # pprint(self._statistic)


if __name__ == "__main__":
    X = dataset[:, :6]  #特征与标签拆分
    Y = dataset[:, 6]
    print(X)
    print(Y)

    clf = Bayes(features, labels) #初试化分类器
    clf.show_params()

    clf.train(X, Y) #训练数据，将所有涉及到的概率求出来
    clf.show_params()

    Yp = clf.predic(X) #根据概率求出的每个样本的类别，如['好瓜','好瓜','好瓜','好瓜','好瓜','好瓜',,,,,,]
    print(f"原始:{Y}\n预测:{Yp}\n准确率:{np.sum(Y==Yp)/len(Y)}") #测试预测的Yp与Y相等的概率  np.sum(Y==Yp)：求两个列表对应位相同值的数量


#步骤：1.初始化模型，好瓜、坏瓜概率初始化、各种瓜不同特征概率初始化：好瓜.色泽.青绿=0.3
#2.训练数据，得出好瓜、坏瓜的数量，各种瓜不同特征对应数量，再计算好瓜和坏瓜概率，不同特征的概率
#3.利用已知的概率，测试数据集，采用朴素贝叶斯公式计算每个样本对应的类别
#4.将预测的结果与真实结果对比，计算准确率