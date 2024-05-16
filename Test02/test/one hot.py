import os
import numpy as np

strs=['我 喜欢 旅行',
     '你 好 中国 我 爱 你',
     '原来 你 还 在 这里 等 我',
     '中国 运动 健儿 胜利 在 望',
     '春天 已经 来 了 ，万物 复苏 '
    ]
new=[]#1.存放所有的关键词
for item in strs:  #遍历列表中所有元素
    new.extend(item.split())  #将元素按空格分割，添加到列表中
new=list(set(new)) #元素去重
#print(new)
dict={}  #2.创建字典,作为词表
for index,val in enumerate(new): #将列表转换为字典，列表中元素变成字典内的key
    dict[val]=index
#print(dict)
def get_onehot(index): #3.将每篇文章的关键字与词表进行对照，定位到相应的索引上，置为1
    one_hot=[0 for _ in range(len(dict))]
    one_hot[index]=1
    return np.array(one_hot)

print(get_onehot(1))
print(strs[0].split())
print(dict)
##实现
indexs=[dict[word] for word in strs[0].split()] #取第一篇文章，进行拆分，遍历取词在字典中获取对应的索引值
re=[get_onehot(index) for index in indexs] #将词所对应的索引上值置为1
print(np.array(re))
