#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import re
import gensim
import numpy as np
import jieba
from gensim.models import Word2Vec
#读取文件
file_path = 'C:/Users/86159/corpus/datasets/倚天屠龙记.txt'
corpus = []#存储分词后的文本

with open(file_path, 'r', encoding='utf-8') as f:
    file_read = f.readlines()
    all_text = " "
    for line in file_read:
        line = line.strip('\n')
        line = re.sub("[A-Za-z0-9\：\·\—\，\。\“\”\\n \《\》\！\？\、\...]", "", line)
        all_text += line
        con = jieba.cut(line, cut_all=False)
        corpus.append(list(con))

def content_deal(content):
    ad = ['本书来自www.cr173.com免费txt小说下载站\n更多更新免费电子书请关注www.cr173.com', '----〖新语丝电子文库(www.xys.org)〗', '新语丝电子文库',
          '\u3000', '\n', '。', '？', '！', '，', '；', '：', '、', '《', '》', '“', '”', '‘', '’', '［', '］', '....', '......',
          '『', '』', '（', '）', '…', '「', '」', '\ue41b', '＜', '＞', '+', '\x1a', '\ue42b']
    for a in ad:
        content = content.replace(a, '')
    return content

#建立Word2Vec模型，并构建词汇表
model = Word2Vec(vector_size=100, window=5, min_count=1, workers=4)
model.build_vocab(corpus)

#训练Word2Vec模型
model.train(corpus, total_examples=model.corpus_count, epochs=10)

#导出“杨过”的词向量
mingjiao_vector = model.wv['明教']

#导出与“杨过”最相关的前20个词语
similar_words = model.wv.most_similar('明教', topn=10)
print("明教的词向量:", mingjiao_vector)
print("\n与明教最相关的前20个词语")
for word, similarity in similar_words:
    print(f"{word}:{similarity}")


# In[4]:


import os
import re
import gensim
import numpy as np
import jieba
from gensim.models import Word2Vec
#读取文件
file_path = 'C:/Users/86159/corpus/datasets/天龙八部.txt'
corpus = []#存储分词后的文本

with open(file_path, 'r', encoding='utf-8') as f:
    file_read = f.readlines()
    all_text = " "
    for line in file_read:
        line = line.strip('\n')
        line = re.sub("[A-Za-z0-9\：\·\—\，\。\“\”\\n \《\》\！\？\、\...]", "", line)
        all_text += line
        con = jieba.cut(line, cut_all=False)
        corpus.append(list(con))

def content_deal(content):
    ad = ['本书来自www.cr173.com免费txt小说下载站\n更多更新免费电子书请关注www.cr173.com', '----〖新语丝电子文库(www.xys.org)〗', '新语丝电子文库',
          '\u3000', '\n', '。', '？', '！', '，', '；', '：', '、', '《', '》', '“', '”', '‘', '’', '［', '］', '....', '......',
          '『', '』', '（', '）', '…', '「', '」', '\ue41b', '＜', '＞', '+', '\x1a', '\ue42b']
    for a in ad:
        content = content.replace(a, '')
    return content

#建立Word2Vec模型，并构建词汇表
model = Word2Vec(vector_size=100, window=5, min_count=1, workers=4)
model.build_vocab(corpus)

#训练Word2Vec模型
model.train(corpus, total_examples=model.corpus_count, epochs=10)

#导出“杨过”的词向量
qiaofeng_vector = model.wv['乔峰']

#导出与“杨过”最相关的前20个词语
similar_words = model.wv.most_similar('乔峰', topn=10)
print("乔峰的词向量:", qiaofeng_vector)
print("\n与乔峰最相关的前10个词语")
for word, similarity in similar_words:
    print(f"{word}:{similarity}")


# In[ ]:




