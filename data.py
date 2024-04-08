#!/usr/bin/env python
# coding: utf-8

# In[15]:


import os
import matplotlib.pyplot as plt
from collections import Counter
import jieba
import re

def clean_text(text):
    #去除文本标点符号
    chinese_punctuation = '’，。！？；：”""“（）、【】《》‘'
    cleaned_text = re.sub(r'[%s]+'%re.escape(chinese_punctuation), '', text)
    return cleaned_text


def read_corpus(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        corpus = f.read()
    return corpus

def tokenize(corpus):
    corpus = clean_text(corpus)
    tokens = jieba.lcut(corpus)
    return tokens

def zipfs_law(tokens):
    token_counts = Counter(tokens)
    sorted_counts = sorted(token_counts.items(), key=lambda x: x[1], reverse=True)
    #输出按照频数从高到低排序的词语
    sorted_tokens = [token for token, count in sorted_counts]
    ranks =[i+1 for i in range(len(sorted_counts))]
    frequencies =[count for token, count in sorted_counts]
    
    plt.figure(figsize=(10, 6))
    plt.plot(ranks, frequencies, marker='o')
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.title('Zipf\'s Law')
    plt.show()
    
    return sorted_tokens
    
if __name__ == '__main__':
    corpus_path = r'C:\Users\86159\data\sanguo.txt'
    corpus = read_corpus(corpus_path)
    tokens = tokenize(corpus)
    sorted_tokens = zipfs_law(tokens)
    print(sorted_tokens)


# In[18]:


import os
import matplotlib.pyplot as plt
from collections import Counter
import jieba
import re
import math

def clean_text(text):
    #去除文本标点符号
    chinese_punctuation = '’，。！？；：”""“（）、【】《》‘'
    cleaned_text = re.sub(r'[%s]+'%re.escape(chinese_punctuation), '', text)
    return cleaned_text


def read_corpus(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        corpus = f.read()
    return corpus

def tokenize(corpus):
    corpus = clean_text(corpus)
    tokens = jieba.lcut(corpus)
    return tokens

def zipfs_law(tokens):
    token_counts = Counter(tokens)
    sorted_counts = sorted(token_counts.items(), key=lambda x: x[1], reverse=True)
    #输出按照频数从高到低排序的词语
    sorted_tokens = [token for token, count in sorted_counts]
    ranks =[i+1 for i in range(len(sorted_counts))]
    frequencies =[count for token, count in sorted_counts]
    
    plt.figure(figsize=(10, 6))
    plt.plot(ranks, frequencies, marker='o')
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.title('Zipf\'s Law')
    plt.show()
    
    return sorted_tokens

def calculate_entropy(tokens):
    token_counts = Counter(tokens)
    total_tokens =sum(token_counts.values())
    
    entropy = 0
    for count in token_counts.values():
        probability = count / total_tokens
        entropy -= probability * math.log2(probability) 
        
    return entropy
    
if __name__ == '__main__':
    corpus_path = r'C:\Users\86159\data\sanguo.txt'
    corpus = read_corpus(corpus_path)
    tokens = tokenize(corpus)
    sorted_tokens = zipfs_law(tokens)
    entropy = calculate_entropy(tokens)
    print(f'Average Entropy: {entropy}')
    print(sorted_tokens)


# In[ ]:




