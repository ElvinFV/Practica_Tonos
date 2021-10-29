

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from winsound import *



plt.close('all')

audio_file1 = "Agua_P.wav"

signal1, sr = librosa.load(audio_file1)

PlaySound(r"Agua_P.wav", SND_FILENAME | SND_ASYNC)

#ESPECTROGRAMA
S = librosa.feature.melspectrogram(signal1)
S_DB = librosa.power_to_db(S, ref=np.max)
librosa.display.specshow(S_DB,x_axis='time', y_axis='mel');
plt.colorbar(format='%+2.0f dB');

#Coeﬁcientes Cepstrales en las Frecuencias de Mel
plt.figure(2)
mfccs1 = librosa.feature.mfcc(y=signal1, n_mfcc=13, sr=sr)
librosa.display.specshow(mfccs1,x_axis="time",sr=sr)
plt.colorbar(format="%+2.f")
plt.show()
#Signal->DFT->log (spectrum)->IDFT (cepstrum)->MFCCs
#discrete cosine Transform
#MFCCS 0 VS 1

plt.figure(3)
plt.scatter(mfccs1[0,:],mfccs1[1,:])

long=len(mfccs1[0])
Id_P=0
Id_E=0
Id_A=0
Id_G=0

for i in range(0,long):
    if -450<mfccs1[0,i]<-200  and 100<mfccs1[1,i]<260:
        Id_P=Id_P+1
    if -400<mfccs1[0,i]<0  and 50<mfccs1[1,i]<200:
        Id_E=Id_E+1
    # if -350<mfccs1[0,i]<-100  and -36<mfccs1[1,i]<125:
    #     Id_A=Id_A+1
    # if -500<mfccs1[0,i]<-250  and 50<mfccs1[1,i]<200:
    #     Id_G=Id_G+1


if Id_E==max(Id_P,Id_E,Id_A,Id_G):
    print("El audio analizado tiene la voz de Elvin")
if Id_P==max(Id_P,Id_E,Id_A,Id_G):
    print("El audio analizado tiene la voz de Adrian")
# if Id_A==max(Id_P,Id_E,Id_A,Id_G):
#     print("El audio analizado tiene la voz de Adele")
# if Id_G==max(Id_P,Id_E,Id_A,Id_G):
#     print("El audio analizado tiene la voz de Gotye")
    
    

# print("Coincidencias con tono de voz de Adrian: :",Id_P)
# print("Coincidencias con tono de voz de Elvin: :",Id_E)