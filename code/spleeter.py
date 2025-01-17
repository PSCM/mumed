# -*- coding: utf-8 -*-
"""Spleeter.ipynb

"""

# Instalar as bibliotecas
!apt install ffmpeg
!pip install spleeter

#Importar bibliotecas
import os
from os import path
import re
import shutil

"""### Separar múltiplos arquivos"""

# múltiplos arquivos por linha de comando
# !spleeter separate -p spleeter:2stems ./*.wav -o output

from google.colab import drive
drive.mount('/content/drive')

#path = '/content/music/' # criar a pasta, caso utilize o Colab
path = '/content/drive/MyDrive/4/'
files = os.listdir(path)
files.sort(key=lambda f: int(re.sub('\D', '', f)))

# Separar o arquivo (áudio e acompanhamentos)
from spleeter.separator import Separator
separator = Separator('spleeter:2stems')

for file in files:
  separator.separate_to_file(path+file, destination='/content/music/',synchronous=False, codec='wav')

# Remover as músicas "soltas"
for f in files:
    if f.endswith(".wav"):
        os.remove(path+f)

# Alterar o nome dos arquivos (ex: 1_vocal; 1_audio)
path = '/content/music/'
files = os.listdir(path)

for f in files:
  newPath = path+f+'/'
  newFiles = os.listdir(newPath)
  for file in newFiles:
    if file.startswith("vocals"):
      os.rename(os.path.join(newPath, file), os.path.join(newPath, ''.join([str(f+ "_vocal"), '.wav'])))
    else:
      os.rename(os.path.join(newPath, file), os.path.join(newPath, ''.join([str(f+ "_audio"), '.wav'])))

# Mover cada arquivo para a respectiva pasta
stringVocal = 'vocal'
stringAudio  = 'audio'

vocal = '/content/vocal'
audio = '/content/audio'

for f in files:
  newPath2 = path+f+'/'
  newFiles2 = os.listdir(newPath2)
  for file in newFiles2:
    if stringVocal in file:
      shutil.copy(newPath2 + file, vocal)
      os.remove(newPath2 + file)
    else:
      shutil.copy(newPath2 + file, audio)
      os.remove(newPath2 + file)

#Criar arquivo .zip para baixar os arquivos
!zip -r /content/audio.zip /content/audio

!zip -r /content/vocal.zip /content/vocal

# Baixar os arquivos
from google.colab import files
files.download("/content/audio.zip")
files.download("/content/vocal.zip")
