# -*- coding: utf-8 -*-
"""Symbolic

"""

!pip install music21

!pip install -U pip
!pip install git+https://github.com/Music-and-Culture-Technology-Lab/omnizart.git
!omnizart download-checkpoints
!apt install fluidsynth
!pip install pyfluidsynth
!curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
!chmod a+rx /usr/local/bin/yt-dlp
!pip install tensorflow

# Importar as bibliotecas
import pandas as pd
import numpy as np
import os
import re
import music21
from music21 import *

"""### Criar arquivos MIDI"""

# múltiplos arquivos
# carregar o arquivo process.bat para o ambiente
!bash process.bat '/content/drive/MyDrive/aug/3/3.2' # identificar a pasta com os áudios

import re
import shutil

path = '/content/'
newPath = '/content/midi'
files = os.listdir(path)

for f in files:
  if f.endswith("mid"):
    shutil.copy(path + f, newPath)

for f in files:
    if f.endswith(".mid"):
        os.remove(path+f)

"""### Extrair as características"""

# Indicar o local das músicas
path = '/content/drive/MyDrive/midi6'

files = os.listdir(path)
files.sort(key=lambda f: int(re.sub('\D', '', f))) # ordenar os arquivos

midiFeatures = []

for f in files:
  midi = converter.parse(path+'/'+f)
  parts = instrument.partitionByInstrument(midi)

  averageNoteDuration                   = music21.features.jSymbolic.AverageNoteDurationFeature(parts)
  maximumNoteDuration                   = music21.features.jSymbolic.MaximumNoteDurationFeature(parts)
  minimumNoteDuration                   = music21.features.jSymbolic.MinimumNoteDurationFeature(parts)
  variabilityOfNoteDuration             = music21.features.jSymbolic.VariabilityOfNoteDurationFeature(parts)
  noteDensity                           = music21.features.jSymbolic.NoteDensityFeature(parts)
  importanceOfBassRegister              = music21.features.jSymbolic.ImportanceOfBassRegisterFeature(parts)
  importanceOfMiddleRegister            = music21.features.jSymbolic.ImportanceOfMiddleRegisterFeature(parts)
  importanceOfHighRegister              = music21.features.jSymbolic.ImportanceOfHighRegisterFeature(parts)
  mostCommonPitchClassPrevalence        = music21.features.jSymbolic.MostCommonPitchClassPrevalenceFeature(parts)
  primaryRegister                       = music21.features.jSymbolic.PrimaryRegisterFeature(parts)
  pitchClassVariety                     = music21.features.jSymbolic.PitchClassVarietyFeature(parts)
  range                                 = music21.features.jSymbolic.RangeFeature(parts)

  averageNoteDuration                   = averageNoteDuration.extract()
  maximumNoteDuration                   = maximumNoteDuration.extract()
  minimumNoteDuration                   = minimumNoteDuration.extract()
  variabilityOfNoteDuration             = variabilityOfNoteDuration.extract()
  noteDensity                           = noteDensity.extract()
  importanceOfBassRegister              = importanceOfBassRegister.extract()
  importanceOfMiddleRegister            = importanceOfMiddleRegister.extract()
  importanceOfHighRegister              = importanceOfHighRegister.extract()
  mostCommonPitchClassPrevalence        = mostCommonPitchClassPrevalence.extract()
  primaryRegister                       = primaryRegister.extract()
  pitchClassVariety                     = pitchClassVariety.extract()
  range                                 = range.extract()

  # dicionário para armazenar os valores
  audio_features = {
        "title": f,
        "averageNoteDuration":  averageNoteDuration.vector,
        "maximumNoteDuration":  maximumNoteDuration.vector,
        "minimumNoteDuration":  minimumNoteDuration.vector,
        "variabilityOfNoteDuration": variabilityOfNoteDuration.vector,
        "noteDensity": noteDensity.vector,
        "importanceOfBassRegister": importanceOfBassRegister.vector,
        "importanceOfMiddleRegister": importanceOfMiddleRegister.vector,
        "importanceOfHighRegister": importanceOfHighRegister.vector,
        "mostCommonPitchClassPrevalence": mostCommonPitchClassPrevalence.vector,
        "primaryRegister ": primaryRegister.vector,
        "pitchClassVariety": pitchClassVariety.vector,
        "range": range.vector,
    }

  midiFeatures.append(audio_features)
  df  = pd.json_normalize(midiFeatures) # criar data frame (df)

df.to_excel('midi6.xlsx')
