# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 01:28:53 2021

@author: adria
"""


import librosa
import librosa.display
import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np
from winsound import *



plt.close('all')

audio_file1 = "Cafe_P3.wav"

signal1, sr = librosa.load(audio_file1)
mfccs1 = librosa.feature.mfcc(y=signal1, n_mfcc=13, sr=sr)
plt.figure(1)
plt.scatter(mfccs1[0,:],mfccs1[1,:])

long=len(mfccs1[0])
Id_P=0
Id_E=0
for i in range(0,long):
    if -750<mfccs1[0,i]<-550  and 0<mfccs1[1,i]<110:
        Id_P=Id_P+1
    if -550<mfccs1[0,i]<-400  and 0<mfccs1[1,i]<110:
        Id_E=Id_E+1

print("Coincidencias con tono de voz de Adrian: :",Id_P)
print("Coincidencias con tono de voz de Elvin: :",Id_E)
if Id_E>Id_P:
    print("El audio analizado tiene la voz de Elvin")
if Id_E<Id_P:
    print("El audio analizado tiene la voz de Adrian")
    