import os
import jieba
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB  # 采用多项式贝叶斯算法
from sklearn import metrics  # 检测模型准确率的函数
warnings.filterwarnings('ignore')


# 1.文档分词，jieba库
def cut_word(file_path):
    text = open(file_path, 'r',encoding='utf-8').read()  # 读取文档     ‘今天的天气很好’
    text_cut = jieba.cut(text)  # 利用jieba对文档进行分词  ['今天'，’的‘，’天气‘，’很‘，’好‘]
    text_with_space = ''  # 分词之后，各词之间用空格连接
    for word in text_cut:
        text_with_space += word + ' '  # '今天 的 天气 很 好'
    return text_with_space


# 加载文本数据
def loadfile(file_dir, label):
    file_list = os.listdir(file_dir)  # 将目录下面所有文档放入列表中
    word_list = []
    label_list = []
    for file in file_list:  # 遍历所有文档
        file_path = file_dir + '/' + file  # 获取每个文档的详细路径
        word_list.append(cut_word(file_path))  # 对文档进行分词操作，并将所有单词放入列表中
        label_list.append(label)
    return word_list, label_list


# 训练数据
train_list1, train_label1 = loadfile("data/train/体育", "体育")  # 对所有训练集数据进行分类标记
train_list2, train_label2 = loadfile("data/train/学习", "学习")
train_list3, train_label3 = loadfile("data/train/旅行", "旅行")
train_list = train_list1 + train_list2 + train_list3
train_label = train_label1 + train_label2 + train_label3
# 测试数据
test_list1, test_label1 = loadfile("data/test/体育", "体育")  # 对所有测试集数据进行分类标记
test_list2, test_label2 = loadfile("data/test/学习", "学习")
test_list3, test_label3 = loadfile("data/test/旅行", "旅行")
test_list = test_list1 + test_list2 + test_list3
test_label = test_label1 + test_label2 + test_label3
# 加载停用词
stop_words = open('data/stop/stopwords.txt', 'r',encoding='utf-8').read()
stop_words=stop_words.encode("utf-8").decode('utf-8-sig')
stop_words = stop_words.split('\n')

# 特征提取，采用tf-idf特征提取方法，评估某个单词对整个文档的重要程度
tf = TfidfVectorizer(stop_words=stop_words, max_df=0.5)  # 将一些停用词去掉
train_feature = tf.fit_transform(train_list)  # 将训练集的文本数据转换成特征向量
print(tf.get_feature_names_out())
print(train_feature.toarray())
test_feature = tf.transform(test_list)  # 将测试集的文本数据转换成特征向量
print("----------------------------------")
print(test_feature.toarray())

# 模型训练  采用朴素贝叶斯算法训练数据得到分类模型
ml = MultinomialNB(alpha=0.001)  # 实例化分类器
ml.fit(train_feature, train_label)  # 训练数据集
predict_label = ml.predict(test_feature)  # 预测测试集中的文章所属类别
# 计算准确率
print("准确率", metrics.accuracy_score(test_label, predict_label))  # 比对测试集的标签和预测标签
