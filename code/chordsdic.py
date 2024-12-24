# -*- coding: utf-8 -*-
"""chordsDic.ipynb
"""

#https://jguitar.com/chorddictionary.jsp

import re
import pandas as pd
import numpy as np

# Carregar a base
cols = ['id', 'chords', 'emotion']
df = pd.read_excel('/content/chords.xlsx', usecols=cols)
df

# Dicionário de acordes
chord_types = {'C':'triadeMaior',
               'C#':'triadeMaior',
               'Db':'triadeMaior',
               'D':'triadeMaior',
               'D#':'triadeMaior',
               'Eb':'triadeMaior',
               'E':'triadeMaior',
               'F':'triadeMaior',
               'F#':'triadeMaior',
               'Gb':'triadeMaior',
               'G':'triadeMaior',
               'G#':'triadeMaior',
               'Ab':'triadeMaior',
               'A':'triadeMaior',
               'A#':'triadeMaior',
               'Bb':'triadeMaior',
               'B':'triadeMaior',
               'Cm':'triadeMenor',
               'C#m':'triadeMenor',
               'Dbm':'triadeMenor',
               'Dm':'triadeMenor',
               'D#m':'triadeMenor',
               'Ebm':'triadeMenor',
               'Em':'triadeMenor',
               'Fm':'triadeMenor',
               'F#m':'triadeMenor',
               'Gbm':'triadeMenor',
               'Gm':'triadeMenor',
               'G#m':'triadeMenor',
               'Abm':'triadeMenor',
               'Am':'triadeMenor',
               'A#m':'triadeMenor',
               'Bbm':'triadeMenor',
               'Bm':'triadeMenor',
               'Cdim':'triadeDiminuta',
               'C#dim':'triadeDiminuta',
               'Dbdim':'triadeDiminuta',
               'Ddim':'triadeDiminuta',
               'D#dim':'triadeDiminuta',
               'Ebdim':'triadeDiminuta',
               'Edim':'triadeDiminuta',
               'Fdim':'triadeDiminuta',
               'F#dim':'triadeDiminuta',
               'Gbdim':'triadeDiminuta',
               'Gdim':'triadeDiminuta',
               'G#dim':'triadeDiminuta',
               'Abdim':'triadeDiminuta',
               'Adim':'triadeDiminuta',
               'A#dim':'triadeDiminuta',
               'Bbdim':'triadeDiminuta',
               'Bdim':'triadeDiminuta',
               'Caug':'triadeAumentada',
               'C#aug':'triadeAumentada',
               'Dbaug':'triadeAumentada',
               'Daug':'triadeAumentada',
               'D#aug':'triadeAumentada',
               'Ebaug':'triadeAumentada',
               'Eaug':'triadeAumentada',
               'Faug':'triadeAumentada',
               'F#aug':'triadeAumentada',
               'Gbaug':'triadeAumentada',
               'Gaug':'triadeAumentada',
               'G#aug':'triadeAumentada',
               'Abaug':'triadeAumentada',
               'Aaug':'triadeAumentada',
               'A#aug':'triadeAumentada',
               'Bbaug':'triadeAumentada',
               'Baug':'triadeAumentada',
               'C7':'setima',
               'C#7':'setima',
               'Db7':'setima',
               'D7':'setima',
               'D#7':'setima',
               'Eb7':'setima',
               'E7':'setima',
               'F7':'setima',
               'F#7':'setima',
               'Gb7':'setima',
               'G7':'setima',
               'G#7':'setima',
               'Ab7':'setima',
               'A7':'setima',
               'A#7':'setima',
               'Bb7':'setima',
               'B7':'setima',
               'Cm7':'setimaMenor',
               'C#m7':'setimaMenor',
               'Dbm7':'setimaMenor',
               'Dm7':'setimaMenor',
               'D#m7':'setimaMenor',
               'Ebm7':'setimaMenor',
               'Em7':'setimaMenor',
               'Fm7':'setimaMenor',
               'F#m7':'setimaMenor',
               'Gbm7':'setimaMenor',
               'Gm7':'setimaMenor',
               'G#m7':'setimaMenor',
               'Abm7':'setimaMenor',
               'Am7':'setimaMenor',
               'A#m7':'setimaMenor',
               'Bbm7':'setimaMenor',
               'Bm7':'setimaMenor',
               'Cmaj7':'setimaMaior',
               'C#maj7':'setimaMaior',
               'Dbmaj7':'setimaMaior',
               'Dmaj7':'setimaMaior',
               'D#maj7':'setimaMaior',
               'Ebmaj7':'setimaMaior',
               'Emaj7':'setimaMaior',
               'Fmaj7':'setimaMaior',
               'F#maj7':'setimaMaior',
               'Gbmaj7':'setimaMaior',
               'Gmaj7':'setimaMaior',
               'G#maj7':'setimaMaior',
               'Abmaj7':'setimaMaior',
               'Amaj7':'setimaMaior',
               'A#maj7':'setimaMaior',
               'Bbmaj7':'setimaMaior',
               'Bmaj7':'setimaMaior',
               'Cm7b5':'setimaMenorQuinta',
               'C#m7b5':'setimaMenorQuinta',
               'Dbm7b5':'setimaMenorQuinta',
               'Dm7b5':'setimaMenorQuinta',
               'D#m7b5':'setimaMenorQuinta',
               'Ebm7b5':'setimaMenorQuinta',
               'Em7b5':'setimaMenorQuinta',
               'Fm7b5':'setimaMenorQuinta',
               'F#m7b5':'setimaMenorQuinta',
               'Gbm7b5':'setimaMenorQuinta',
               'Gm7b5':'setimaMenorQuinta',
               'G#m7b5':'setimaMenorQuinta',
               'Abm7b5':'setimaMenorQuinta',
               'Am7b5':'setimaMenorQuinta',
               'A#m7b5':'setimaMenorQuinta',
               'Bbm7b5':'setimaMenorQuinta',
               'Bm7b5':'setimaMenorQuinta',
               'C6':'sexta',
               'C#6':'sexta',
               'Db6':'sexta',
               'D6':'sexta',
               'D#6':'sexta',
               'Eb6':'sexta',
               'E6':'sexta',
               'F6':'sexta',
               'F#6':'sexta',
               'Gb6':'sexta',
               'G6':'sexta',
               'G#6':'sexta',
               'Ab6':'sexta',
               'A6':'sexta',
               'A#6':'sexta',
               'Bb6':'sexta',
               'B6':'sexta',
               'Cm6':'sextaMenor',
               'C#m6':'sextaMenor',
               'Dbm6':'sextaMenor',
               'Dm6':'sextaMenor',
               'D#m6':'sextaMenor',
               'Ebm6':'sextaMenor',
               'Em6':'sextaMenor',
               'Fm6':'sextaMenor',
               'F#m6':'sextaMenor',
               'Gbm6':'sextaMenor',
               'Gm6':'sextaMenor',
               'G#m6':'sextaMenor',
               'Abm6':'sextaMenor',
               'Am6':'sextaMenor',
               'A#m6':'sextaMenor',
               'Bbm6':'sextaMenor',
               'Bm6':'sextaMenor'
}

# Renomear os acordes, de acordo com o dicionário
map_fn = lambda cs: ', '.join((chord_types.get(c, 'outros') for c in cs))
df['chordType'] = df['chords'].str.replace(' ', '').str.split(',').apply(map_fn)
df

# Quantidade de acordes
df['quantidadeAcordes'] =  df['chords'].apply(lambda x: len(str(x).split(" ")))

# Criar colunas com a quantidade de acordes observados, de acordo com cada linha
df2 = pd.concat([df, df["chordType"].str.split(", ").explode().reset_index().groupby(["index", "chordType"]).size().unstack().fillna(0)], axis=1)
df2.head(5)

df2.reset_index(inplace = True)
df2['uniqueChords'] = pd.Series(np.arange(len(df)))

current = 0
for row in df.itertuples():
    df2['uniqueChords'][current] = len(np.unique(df2['chords'].str.split(',')[current]))
    current = current + 1

df2['proporcaoUnicos'] = df2['uniqueChords']/df2['quantidadeAcordes']
df2['proporcaoTriadeMenor'] = df2['triadeMenor']/df2['quantidadeAcordes']
df2['proporcaoTriadeMaior'] = df2['triadeMaior']/df2['quantidadeAcordes']
df2['proporcaoTriadeDiminuta'] = df2['triadeDiminuta']/df2['quantidadeAcordes']
df2['proporcaoTriadeAumentada'] = df2['triadeAumentada']/df2['quantidadeAcordes']
df2['proporcaoSextaMenor'] = df2['sextaMenor']/df2['quantidadeAcordes']
df2['proporcaoSexta'] = df2['sexta']/df2['quantidadeAcordes']
df2['proporcaoSetima'] = df2['setima']/df2['quantidadeAcordes']
df2['proporcaoSetimaMaior'] = df2['setimaMaior']/df2['quantidadeAcordes']
df2['proporcaoSetimaMenor'] = df2['setimaMenor']/df2['quantidadeAcordes']
df2['proporcaoSetimaMenorQuinta'] = df2['setimaMenorQuinta']/df2['quantidadeAcordes']
df2['proporcaoOutros'] = df2['outros']/df2['quantidadeAcordes']

df2.head(5)

df2.describe()

df2.to_excel("file")
