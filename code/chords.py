# -*- coding: utf-8 -*-
"""Chords
### Separação considerado o Chordino
"""

# Instalar a biblioteca
!pip install chord-extractor

# Importar as bibliotecas necessárias
import os
import re
import pandas as pd
from chord_extractor.extractors import Chordino
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import warnings
warnings.filterwarnings("ignore", message="PySoundFile failed")

# Indicar o local das músicas
path = #yourPath
files = os.listdir(path)
files.sort(key=lambda f: int(re.sub('\D', '', f)))

# Extração de múltiplos arquivos
# Fonte dos parâmetros: http://www.isophonics.net/nnls-chroma

chordino = Chordino(roll_on=1, use_nnls= True, spectral_shape=0.7,spectral_whitening= 1)

chords = []
fi = []

for f in files:
 chord = chordino.extract(path+'/'+f)
 fi.append(f)
 chords.append(chord)

df = pd.DataFrame(zip(fi, chords), columns=['music', 'chords']) # criar data frame (df)

# Deixar apenas o acordes (remover N)
df['chords'] = df['chords'].map(lambda lst: ", ".join(tup[0] for tup in lst))
df['chords'] = [(x.strip(', N')) for x in df['chords']]
df.head(3)

df.to_excel('chords.xlsx')
