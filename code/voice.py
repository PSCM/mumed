# -*- coding: utf-8 -*-
"""Voice
"""

# Instalar bibliotecas
!pip install opensmile
!pip install sox
!pip install essentia
!pip install librosa

# Importar bibliotecas
import pandas as pd
import numpy as np
import os
import re
import opensmile
import essentia
import essentia.standard as es
import librosa

# Indicar o local das músicas
path = #yourPath

def featuresSmile(path):

  files = os.listdir(path)
  files.sort(key=lambda f: int(re.sub('\D', '', f)))

  featuresSmile = []

  for f in files:

     smile = opensmile.Smile(
      feature_set=opensmile.FeatureSet.eGeMAPSv02
     )

     y = smile.process_file(path+'/'+f)

     f1Mean     =  y.F1frequency_sma3nz_amean
     f1STD      =  y.F1frequency_sma3nz_stddevNorm
     f1BandMean =  y.F1bandwidth_sma3nz_amean
     f1BandSTD  =  y.F1bandwidth_sma3nz_stddevNorm
     f2Mean     =  y.F2frequency_sma3nz_amean
     f2STD      =  y.F2frequency_sma3nz_stddevNorm
     f2BandMean =  y.F2bandwidth_sma3nz_amean
     f2BandSTD  =  y.F2bandwidth_sma3nz_stddevNorm
     f3Mean     =  y.F3frequency_sma3nz_amean
     f3STD      =  y.F3frequency_sma3nz_stddevNorm
     f3BandMean =  y.F3bandwidth_sma3nz_amean
     f3BandSTD  =  y.F3bandwidth_sma3nz_stddevNorm
     voicedMean =  y.MeanVoicedSegmentLengthSec
     voicedSTD  =  y.StddevVoicedSegmentLengthSec
     unvoicedMean = y.MeanUnvoicedSegmentLength
     unvoicedSTD  = y.StddevUnvoicedSegmentLength
     f0Mean =       y['F0semitoneFrom27.5Hz_sma3nz_amean']
     f0STD  =       y['F0semitoneFrom27.5Hz_sma3nz_stddevNorm']
     hnrMean =      y.HNRdBACF_sma3nz_amean
     hnrSTD =       y.HNRdBACF_sma3nz_stddevNorm
     jitterMean =   y.jitterLocal_sma3nz_amean
     jitterSTD =    y.jitterLocal_sma3nz_stddevNorm
     shitterMean =  y.shimmerLocaldB_sma3nz_amean
     shitterSTD =   y.shimmerLocaldB_sma3nz_stddevNorm

     features_smile ={
      "title":        f,
      "f1Mean":       f1Mean[0],
      "f1STD":        f1STD[0],
      "f1BandMean":   f1BandMean[0],
      "f1BandSTD":    f1BandSTD[0],
      "f2Mean":       f2Mean[0],
      "f2STD":        f2STD[0],
      "f2BandMean":   f2BandMean[0],
      "f2BandSTD":    f2BandSTD[0],
      "f3Mean":       f3Mean[0],
      "f3STD":        f3STD[0],
      "f3BandMean":   f3BandMean[0],
      "f3BandSTD":    f3BandSTD[0],
      "voicedMean":   voicedMean[0],
      "voiceSTD":     voicedSTD[0],
      "unvoicedMean": unvoicedMean[0],
      "unvoicedSTD":  unvoicedSTD[0],
      "f0Mean":       f0Mean[0],
      "f0STD":        f0STD[0],
      "hnrMean":      hnrMean[0],
      "hnrSTD":       hnrSTD[0],
      "jitterMean":   jitterMean[0],
      "jitterSTD":    jitterSTD[0],
      "shitterMean":  shitterMean[0],
      "shitterSTD":   shitterSTD[0],
     }

     featuresSmile.append(features_smile)
     dfSmile  = pd.json_normalize(featuresSmile)

  return dfSmile

'''
files = os.listdir(path)
files.sort(key=lambda f: int(re.sub('\D', '', f)))

for f in files[3000:4390]:
  print(f)
'''

def extractMFCC(path):

  files = os.listdir(path)
  files.sort(key=lambda f: int(re.sub('\D', '', f)))

  featureMFCC = []

  for f in files:

    y_, sr = librosa.load(path+'/'+f)

    mfcc      =     librosa.feature.mfcc(y=y_, sr=sr, n_mfcc=16) # mfcc - 16

    feature_MFCC ={
      "title":        f,
      "mfcc1Mean":    np.mean(mfcc[0]),
      "mfcc1STD":     np.std(mfcc[0]),
      "mfcc2Mean":    np.mean(mfcc[1]),
      "mfcc2STD":     np.std(mfcc[1]),
      "mfcc3Mean":    np.mean(mfcc[2]),
      "mfcc3STD":     np.std(mfcc[2]),
      "mfcc4Mean":    np.mean(mfcc[3]),
      "mfcc4STD":     np.std(mfcc[3]),
      "mfcc5Mean":    np.mean(mfcc[4]),
      "mfcc5STD":     np.std(mfcc[4]),
      "mfcc6Mean":    np.mean(mfcc[5]),
      "mfcc6STD":     np.std(mfcc[5]),
      "mfcc7Mean":    np.mean(mfcc[6]),
      "mfcc7STD":     np.std(mfcc[6]),
      "mfcc8Mean":    np.mean(mfcc[7]),
      "mfcc8STD":     np.std(mfcc[7]),
      "mfcc9Mean":    np.mean(mfcc[8]),
      "mfcc9STD":     np.std(mfcc[8]),
      "mfcc10Mean":   np.mean(mfcc[9]),
      "mfcc10STD":    np.std(mfcc[9]),
      "mfcc11Mean":   np.mean(mfcc[10]),
      "mfcc11STD":    np.std(mfcc[10]),
      "mfcc12Mean":   np.mean(mfcc[11]),
      "mfcc12STD":    np.std(mfcc[11]),
      "mfcc13Mean":   np.mean(mfcc[12]),
      "mfcc13STD":    np.std(mfcc[12]),
      "mfcc14Mean":   np.mean(mfcc[13]),
      "mfcc14STD":    np.std(mfcc[13]),
      "mfcc15Mean":   np.mean(mfcc[14]),
      "mfcc15STD":    np.std(mfcc[14]),
      "mfcc16Mean":   np.mean(mfcc[15]),
      "mfcc16STD":    np.std(mfcc[15]),
    }

    featureMFCC.append(feature_MFCC)
    dfMFCC  = pd.json_normalize(featureMFCC)

  return dfMFCC

def extractGFCC(path):

    files = os.listdir(path)
    files.sort(key=lambda f: int(re.sub('\D', '', f)))

    featureGFCC = []

    for f in files:
      audio = es.MonoLoader(filename= path+'/'+f)()

      run_gfcc = es.GFCC(numberCoefficients=12)
      gfccs = run_gfcc(audio)

      gfccsMean  =    np.mean(gfccs[1])
      gfccsSTD   =    np.std(gfccs[1])

      feature_GFCC ={
       "title":        f,
       "gfccsMean":    gfccsMean,
       "gfccsSTD":     gfccsSTD,
      }

      featureGFCC.append(feature_GFCC)
      dfGFCC  = pd.json_normalize(featureGFCC)

    return dfGFCC

dfSmile = featuresSmile(path)

dfMFCC = extractMFCC(path)

dfGFCC = extractGFCC(path)
