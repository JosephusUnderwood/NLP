#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import matplotlib.pyplot as plt
from collections import Counter
import jieba
import re
import math

#载入停用词列表
def load_stopwords(file_path):
    with open(stopwords_file_path, 'r', encoding='utf-8') as f:
        stopwords = set(f.read().splitlines())
        return stopwords
    
def read_corpus(corpus_dir):
    corpus_text = ""
    for filename in os.listdir(corpus_dir):
        if filename.endswith(".txt"):
            filepath = os.path.join(corpus_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                corpus_text += f.read()
    return corpus_text

def zipf_law_analysis(text, max_rank=1000, max_frequency=100):
        words = jieba.lcut(text)
        #使用正则表达式只保留中文字符
        words_cleaned = [word for word in words if re.match(r'[^\u4e00-\u9fff]+$', word)]
        word_counts = Counter(words_cleaned)
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:max_rank]
        word_freqs = [(word, count) for word, count in sorted_word_counts if count<=max_frequency]
        ranks = range(1, len(word_freqs) + 1)
        frequencies =[freq for _, freq in word_freqs]
        plt.loglog(ranks, frequencies, 'o', markersize=3, alpha=0.5)
        plt.xlabel('Rank', fontsize=14)
        plt.ylabel('Frequency', fontsize=14)
        plt.title('Zipf\'s Law Analysis (Words)', fontsize=16)
        plt.grid(True)
        plt.show()

stopwords_file_path = r'C:\Users\86159\data\cn_stopwords.txt'
corpus_dir = r'C:\Users\86159\corpus\datasets'

stopwords = load_stopwords(stopwords_file_path)
corpus_text = read_corpus(corpus_dir)

zipf_law_analysis(corpus_text, max_rank=1000, max_frequency=100)

def preprocess_text(text, unit='word'):
    if unit == 'word':
        words = list(jieba.cut(text))
    elif unit == 'char':
        words = list(text)
    else:
        raise ValueError("Invalid unit. Choose either 'word' or 'char'.")
    return words

def calculate_entropy(words):
    word_counts = Counter(words)
    total_words = sum(word_counts.values())
    entropy = -sum(count / total_words * math.log2(count / total_words) for count in word_counts.values())
    average_entropy = entropy/ len(word_counts)
    return average_entropy

if __name__ == '__main__':
    book_titles_list = "白马啸西风,碧血剑,飞狐外传,连城诀,鹿鼎记,三十三剑客图,射雕英雄传,神雕侠侣,书剑恩仇录,天龙八部,侠客行,笑傲江湖,雪山飞狐,倚天屠龙记,鸳鸯刀,越女剑"
    
    #遍历语料库中每一个文件
    for book_title in book_titles_list.split(','):
        book_title = book_title.strip()
        file_path = os.path.join(corpus_dir, f"{book_title}.txt")
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        words_word = preprocess_text(text, unit='word')
        average_entropy_word = calculate_entropy(words_word)
        print(f"Average entropy (word level) for {book_title}: {average_entropy_word:.4f} bits")
        
        words_char = preprocess_text(text, unit='char')
        average_entropy_char = calculate_entropy(words_char)
        print(f"Average entropy (character level) for {book_title}: {average_entropy_char:.4f} bits")
        
        stopwords_file_path = r'C:\Users\86159\data\cn_stopwords.txt'
        corpus_dir = r'C:\Users\86159\corpus\datasets'

        stopwords = load_stopwords(stopwords_file_path)
        corpus_text = read_corpus(corpus_dir)

        zipf_law_analysis(corpus_text, max_rank=1000, max_frequency=100)


# In[ ]:





# In[ ]:




