# -*- coding: utf-8 -*-
"""Lyrics.ipynb

# Versão simples

## Bibliotecas
"""

#Adaptado de https://www.analyticsvidhya.com/blog/2018/02/the-different-methods-deal-text-data-predictive-python/
# Importar as bibliotecas
import pandas as pd
import numpy as np
import re
import nltk
import os
from nltk.tokenize import word_tokenize
from collections import defaultdict
from nltk.corpus import wordnet as wn
from nltk.sentiment.vader import SentimentIntensityAnalyzer

"""## Módulos"""

# Download dos elementos necessários para conduzir as análises
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('omw-1.4')
nltk.download('vader_lexicon')

"""## Pré-processamento"""

# Carregar os arquivos .txt com as letras
path = '/content/drive/MyDrive/lyrics/' # criar pasta, caso utilize o Colab
files = os.listdir(path)
files.sort(key=lambda f: int(re.sub('\D', '', f)))

text  = []
id = []

for line in files:
  with open(path+line, 'r') as f:
    txt = f.read()
    text.append(txt)
    id.append(line)

# Criar a base de dados (df)
df = pd.DataFrame(zip(id, text), columns = ['id','lyrics'])
df.head(3)

# Limpar as letras
replacer = {'\n':' ',"[\[].*?[\]]": "",'[!"#%\'()*+,-./:;<=>?@\[\]^_`{|}~1234567890’""′‘\\\]':" ", ' +': ' '}

df['cleanLyrics'] = df['lyrics'].replace(replacer, regex=True).apply(lambda x: x.strip()).apply(lambda x: " ".join(x.lower() for x in x.split()))
df.head(3)

"""## Características"""

# Número de caracteres
df['charCount'] = df['cleanLyrics'].str.len()
# Número de palavras por letras
df['wordCount'] = df['cleanLyrics'].str.split().str.len()
df.head(3)

# Média de palavras por letras
def avg_word(sentence):
  words = sentence.split()
  return (sum(len(word) for word in words)/len(words))

df['avgWord'] = df['cleanLyrics'].apply(lambda x: avg_word(x))
df.head(3)

df.reset_index(inplace = True)
df['uniqueWords'] = pd.Series(np.arange(len(df)))

current = 0
for row in df.itertuples():
    df['uniqueWords'][current] = len(np.unique(df['cleanLyrics'].str.split()[current]))
    current = current + 1
df.head(3)

df['uniqueWordsProp']  =  df['uniqueWords'] / df['wordCount']
df.head(3)

# Análise de sentimentos
sid = SentimentIntensityAnalyzer()

sentiments = df.apply(lambda r: sid.polarity_scores(r['lyrics']), axis=1)

d = pd.DataFrame(list(sentiments))
df = df.join(d)
df.dropna(inplace=True)

df.to_excel('lyrics.xlsx', index= False)
