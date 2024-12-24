# -*- coding: utf-8 -*-
"""Audio
"""

# Instalar as bibliotecas, se necessário
!pip install essentia

# Importar as bibliotecas
import pandas as pd
import numpy as np
import librosa
import essentia
import essentia.standard as es
import os
import re
import warnings
warnings.filterwarnings("ignore", message="PySoundFile failed")

# Indicar o local das músicas
path = #yourPath

# Características Essentia
def extract_featuresEssentia(path):

  files = os.listdir(path)
  files.sort(key=lambda f: int(re.sub('\D', '', f))) # ordenar os arquivos

  featuresEssentia = []

  for f in files:
    audio = es.MonoLoader(filename= path+'/'+f)()

    # bpm
    rhythm_extractor = es.RhythmExtractor2013(method="multifeature")
    bpm = rhythm_extractor(audio)

    # predominant melody
    run_predominant_melody = es.PitchMelodia()
    pitchMelodia, confidence = run_predominant_melody(audio)

    # loudness
    run_loudness = es.Loudness()
    loud = es.Loudness()
    audio = es.EqualLoudness()(audio)
    loudness = loud(audio)

    # pitch salience
    run_pitch_salience = es.PitchSalience()
    pitchSalience = run_pitch_salience(audio)

    # danceability
    run_danceability = es.Danceability()
    danceability = run_danceability(audio)

    # flux
    run_flux = es.Flux()
    flux = run_flux(audio)

    # key - scale
    run_key = es.KeyExtractor(profileType='krumhansl')
    key, scale, strength = run_key(audio)

    # dicionário para armazenar os valores/características
    essentia_audio = {
      "title": f,
      "loudness": loudness,
      "scale": scale,
      "key": key,
      "salience": pitchSalience,
      "melodiaMean": np.mean(pitchMelodia),
      "melodiaSTD":  np.std(pitchMelodia),
      "bpm": bpm[0],
      "danceability": danceability[0],
      "flux": flux,
    }


    featuresEssentia.append(essentia_audio)
    df2  = pd.json_normalize(featuresEssentia)  # salvar os valores em um data frame (df)
  return df2

# Características librosa
def extract_featuresLibrosa(path):

  files = os.listdir(path)
  files.sort(key=lambda f: int(re.sub('\D', '', f))) # ordenar os arquivos

  features = []

  for f in files:
    y, sr = librosa.load(path+'/'+f)

    rms       = librosa.feature.rms(y=y) # rms
    chroma    = librosa.feature.chroma_stft(y=y, sr=sr) # cromagrama - 12
    onset_env = librosa.onset.onset_strength(y=y, sr=sr) # onset (necessário para plp)
    pulse     = librosa.beat.plp(onset_envelope=onset_env, sr=sr) # plp
    mfcc      = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13) # mfcc - 13
    centroid  = librosa.feature.spectral_centroid(y=y, sr=sr) # spectral centroid
    rollof    = librosa.feature.spectral_rolloff(y=y, sr=sr) # rollof - 0,85
    zcr       = librosa.feature.zero_crossing_rate(y) # zcr

    # dicionário para armazenar os valores/características
    audio_features = {
        "title": f,
        "rmsMean": np.mean(rms),
        "rmsSTD":  np.std(rms),
        "chromaMean1": np.mean(chroma[0]),
        "chromaSTD1": np.std(chroma[0]),
        "chromaMean2": np.mean(chroma[1]),
        "chromaSTD2": np.std(chroma[1]),
        "chromaMean3": np.mean(chroma[2]),
        "chromaSTD3": np.std(chroma[2]),
        "chromaMean4": np.mean(chroma[3]),
        "chromaSTD4": np.std(chroma[3]),
        "chromaMean5": np.mean(chroma[4]),
        "chromaSTD5": np.std(chroma[4]),
        "chromaMean6": np.mean(chroma[5]),
        "chromaSTD6": np.std(chroma[5]),
        "chromaMean7": np.mean(chroma[6]),
        "chromaSTD7": np.std(chroma[6]),
        "chromaMean8": np.mean(chroma[7]),
        "chromaSTD8": np.std(chroma[7]),
        "chromaMean9": np.mean(chroma[8]),
        "chromaSTD9": np.std(chroma[8]),
        "chromaMean10": np.mean(chroma[9]),
        "chromaSTD10": np.std(chroma[9]),
        "chromaMean11": np.mean(chroma[10]),
        "chromaSTD11": np.std(chroma[10]),
        "chromaMean12": np.mean(chroma[11]),
        "chromaSTD12": np.std(chroma[11]),
        "pulseMean": np.mean(pulse),
        "pulseSTD": np.std(pulse),
        "mfcc1Mean": np.mean(mfcc[0]),
        "mfcc1STD": np.std(mfcc[0]),
        "mfcc2Mean": np.mean(mfcc[1]),
        "mfcc2STD": np.std(mfcc[1]),
        "mfcc3Mean": np.mean(mfcc[2]),
        "mfcc3STD": np.std(mfcc[2]),
        "mfcc4Mean": np.mean(mfcc[3]),
        "mfcc4STD": np.std(mfcc[3]),
        "mfcc5Mean": np.mean(mfcc[4]),
        "mfcc5STD": np.std(mfcc[4]),
        "mfcc6Mean": np.mean(mfcc[5]),
        "mfcc6STD": np.std(mfcc[5]),
        "mfcc7Mean": np.mean(mfcc[6]),
        "mfcc7STD": np.std(mfcc[6]),
        "mfcc8Mean": np.mean(mfcc[7]),
        "mfcc8STD": np.std(mfcc[7]),
        "mfcc9Mean": np.mean(mfcc[8]),
        "mfcc9STD": np.std(mfcc[8]),
        "mfcc10Mean": np.mean(mfcc[9]),
        "mfcc10STD": np.std(mfcc[9]),
        "mfcc11Mean": np.mean(mfcc[10]),
        "mfcc11STD": np.std(mfcc[10]),
        "mfcc12Mean": np.mean(mfcc[11]),
        "mfcc12STD": np.std(mfcc[11]),
        "mfcc13Mean": np.mean(mfcc[12]),
        "mfcc13STD": np.std(mfcc[12]),
        "centroidMean": np.mean(centroid),
        "centroidSTD": np.std(centroid),
        "rollofMean": np.mean(rollof),
        "rollofSTD": np.std(rollof),
        "zcrMean": np.mean(zcr),
        "zcrSTD": np.std(zcr),
    }

    features.append(audio_features)
  df  = pd.json_normalize(features)   # salvar os valores em um data frame (df)
  return df

# Criar os dfs a partir das funções de extração
df1  = extract_featuresLibrosa(path)
df2 = extract_featuresEssentia(path)

# Unir os dfs e gerar a base final
df = pd.concat([df1, df2], axis=1, join='inner')
df.head(3)
