# -*- coding: utf-8 -*-
"""Neural_network_159nucleis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UKwdrhrdLEFZShi4h0UFZVaDdFjp-ed7
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.wrappers.scikit_learn import KerasRegressor

from sklearn.preprocessing import RobustScaler


from math import *

! git clone --recursive https://github.com/pierreetienne-pion/datas.git

df = pd.read_csv("/content/datas/bdd_159nucleons.csv")
df.head(10)

df['sigma'] = df['f1']*df['E']*3*10*(pi*197.3269805)**2
df.head()
df.shape

df1 = df
dataset = df1.values
x=dataset[:,1:5]
y=dataset[:,7]
print(x)

y=np.reshape(y, (-1,1))
scaler_x = StandardScaler()
scaler_y = StandardScaler()
print(scaler_x.fit(x))
xscale=scaler_x.transform(x)
print(scaler_y.fit(y))
yscale=scaler_y.transform(y)

X_train, X_test, y_train, y_test = train_test_split(xscale, yscale)
print( 'X_train apercu  ')

print(scaler_x.inverse_transform(X_train))

import numpy as np
from sklearn import datasets, linear_model
from sklearn.model_selection import cross_val_score, KFold
from keras.models import Sequential
from sklearn.metrics import accuracy_score
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor

X=[]
for i in range(len(df[(df.Z == 6) & (df.A == 12)])):
    L=[]
    L.append(df.loc[(df['A']==12) & (df['Z']==6),:]['Z'].iloc[i])
    L.append(df.loc[(df['A']==12) & (df['Z']==6),:]['A'].iloc[i])
    L.append(df.loc[(df['A']==12) & (df['Z']==6),:]['E'].iloc[i])
    L.append(df.loc[(df['A']==12) & (df['Z']==6),:]['dE'].iloc[i])
    X.append(L)
Xnew=np.array(X)



model = Sequential()
model.add(Dense(100, input_dim=4, kernel_initializer='normal', activation='relu'))
model.add(Dense(90, activation='relu'))
model.add(Dense(75, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(25, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='linear'))  
model.compile(loss='mean_squared_error', optimizer='adam')

n_batch=round(df.shape[0]/159)


history=model.fit(X_train, y_train, epochs=730, batch_size=72,  verbose=0, validation_split=0.001)

Xnew= scaler_x.transform(Xnew)
ynew= model.predict(Xnew)
ynew = scaler_y.inverse_transform(ynew) 
Xnew = scaler_x.inverse_transform(Xnew)

plt.plot(df[(df.Z == 6) & (df.A == 12)].E, df[(df.Z == 6) & (df.A == 12)].sigma)
plt.plot(df[(df.Z == 6) & (df.A == 12)].E, ynew)
plt.title('Z=6, A=12')
plt.ylabel('Sigma')
plt.xlabel('E')
plt.legend(['Expé', 'Prédiction'], loc='upper left')

plt.show()

print(history.history.keys())
# "Loss"
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()

y_pred= model.predict(X_test)
y_predinv = scaler_y.inverse_transform(y_pred) 
y_testinv = scaler_y.inverse_transform(y_test)

plt.scatter(y_testinv, y_predinv,s=1)

x = np.linspace(0,1000)

plt.title('Répartition des prédictions par rapport à la valeur exactes (f(x)=x)')
plt.plot(x,x,'g',linewidth=2.5)

Xprime=[]
liste=df["Z"]
for i in range(len(liste)):
    Xprime.append(liste[i])

Xprimeprime=[]
liste2=df["A"]
for i in range(len(liste)):
    Xprimeprime.append(liste2[i])

X=[]
for i in range(len(liste)):
    X.append((liste[i],liste2[i]))


Z=[]
Ztext=[]


Xessai=X
while len(Xessai)>=32:
    a=Xessai[0]
    Z.append(a)
    i=0
    while Xessai[i]==a:
        i=i+1
    del Xessai[0:i]

Z.append((94,239))

for i in range(len(Z)):
    Ztext.append(str(Z[i]))

fig = plt.figure(1, figsize=(20,20))

def graph(Zbarre,Abarre):
    sigma=[]
    E=[]
    for j in range(len(df.loc[(df['Z']==Zbarre) & (df['A']==Abarre),:]['sigma'])):
        sigma.append(df.loc[(df['Z']==Zbarre) & (df['A']==Abarre),:]['sigma'].iloc[j])
        E.append(df.loc[(df['Z']==Zbarre) & (df['A']==Abarre),:]['E'].iloc[j])
    plt.plot(E,sigma, color="blue", linewidth=1, linestyle="-")
    a=(Zbarre,Abarre)
    plt.title(a)

def plusprochecarré(a):
    if a==1:
        return(1,1)
    if a==2:
        return(2,1)
    if 1<a<=4:
        return(2,2)
    if 4<a<=16:
        return(4,4)
    if 16<a<=25:
        return(5,5)
    if 25<a<=35:
        return(5,7)
    if a>35:
        return('non')

def predictionsurbase(Z,A):
    X=[]
    for i in range(len(df[(df.Z == Z) & (df.A == A)])):
      L=[]
      L.append(df.loc[(df['A']==A) & (df['Z']==Z),:]['Z'].iloc[i])
      L.append(df.loc[(df['A']==A) & (df['Z']==Z),:]['A'].iloc[i])
      L.append(df.loc[(df['A']==A) & (df['Z']==Z),:]['E'].iloc[i])
      L.append(df.loc[(df['A']==A) & (df['Z']==Z),:]['dE'].iloc[i])
      X.append(L)
    Xnewa=np.array(X)
    Xnewa= scaler_x.transform(Xnewa)
    ynewa= model.predict(Xnewa)
    ynewfi = scaler_y.inverse_transform(ynewa) 
    Xnewfi = scaler_x.inverse_transform(Xnewa)
    plt.plot(Xnewfi, ynewfi)


def predictionsurbaseid(Z,A):
    X=[]
    abcisses=[]
    for i in range(110):
      L=[]
      L.append(Z)
      L.append(A)
      L.append(7+i*0.2)
      L.append(0)
      X.append(L)
      abcisses.append(7+i*0.2)
    Xnewa=np.array(X)
    Xnewa= scaler_x.transform(Xnewa)
    ynewa= model.predict(Xnewa)
    ynewfi = scaler_y.inverse_transform(ynewa) 
    Xnewfi = scaler_x.inverse_transform(Xnewa)
    plt.plot(abcisses, ynewfi,color="green", linewidth=1.5, linestyle="-")
      
    
    
def panel(Zdébut,Zfin):
    plt.figure(1, figsize=(20,20))
    Zspon=Z
    while Zspon[0][0]<Zdébut:
        Zspon.pop(0)
    while Zspon[-1][0]>Zfin:
        Zspon.pop()
    print(Zspon)
    n=len(Zspon)
    m=plusprochecarré(n)
    if m=='non':
        return('trop de figures      ')
    else:
        graph(Zspon[0][0],Zspon[0][1])
        predictionsurbaseid(Zspon[0][0],Zspon[0][1])
        plt.subplot(m[0],m[1],1)
        for i in range(n):
            Zbarre=Zspon[i][0]
            Abarre=Zspon[i][1]
            graph(Zbarre,Abarre)
            predictionsurbaseid(Zbarre,Abarre)
            plt.subplot(m[0],m[1],i+2)

plt.show()

print(panel(40,50))

def predictionsurbaseid(Z,A):
    X=[]
    abcisses=[]
    for i in range(151):
      L=[]
      L.append(Z)
      L.append(A)
      L.append(5+i*0.2)
      L.append(0)
      X.append(L)
      abcisses.append(5+i*0.2)
    Xnewa=np.array(X)
    Xnewa= scaler_x.transform(Xnewa)
    ynewa= model.predict(Xnewa)
    ynewfi = scaler_y.inverse_transform(ynewa) 
    Xnewfi = scaler_x.inverse_transform(Xnewa)
    plt.plot(abcisses, ynewfi)
    plt.show()

print(predictionsurbaseid(85,220))

"""Tentative d'optimisation par recherche naïve

from random import randint

X=[]
for i in range(len(df[(df.Z == 6) & (df.A == 12)])):
    L=[]
    L.append(df.loc[(df['A']==12) & (df['Z']==6),:]['Z'].iloc[i])
    L.append(df.loc[(df['A']==12) & (df['Z']==6),:]['A'].iloc[i])
    L.append(df.loc[(df['A']==12) & (df['Z']==6),:]['E'].iloc[i])
    L.append(df.loc[(df['A']==12) & (df['Z']==6),:]['dE'].iloc[i])
    X.append(L)
Xnew=np.array(X)

Y=[]
for i in range(len(df[(df.Z == 6) & (df.A == 12)])):
    Y.append(df.loc[(df['A']==12) & (df['Z']==6),:]['sigma'].iloc[i])

def generational(i):
    L=[]
    for i in range(i):
        L.append(randint(1,10))
    return(L)

def transfoliste(X):
  N=[]
  for i in range(len(X)):
    N.append(X[i][0])
  return(N)

#construction apprentissage réseau neurone

model = Sequential()
model.add(Dense(100, input_dim=4, kernel_initializer='uniform', activation='relu'))
model.add(Dense(75, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(25, activation='relu'))
model.add(Dense(15, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(5, activation='relu'))
model.add(Dense(3, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])


for i in range(1,6):
  a=100*i
  model.fit(X_train, y_train, epochs=1000, batch_size=a,  verbose=1, validation_split=0.001)

Xnew= scaler_x.transform(Xnew)
ynew= model.predict(Xnew)
ynew = scaler_y.inverse_transform(ynew) 
Xnew = scaler_x.inverse_transform(Xnew)
plt.plot(df[(df.Z == 6) & (df.A == 12)].E, df[(df.Z == 6) & (df.A == 12)].sigma)
plt.plot(df[(df.Z == 6) & (df.A == 12)].E, ynew)
plt.show()

LA MEILLEURE OPTION EST DE PRENDRE ENVIRON LA MOITIÉ EN DENSITÉ DU RÉSEAU PRÉCÉDENT
"""

noy50 = pd.read_csv("/content/datas/QRPA50.csv", sep=';')

noy50.head(10)

noy50['sigma_000'] = noy50['U=000MeV']*noy50['E[MeV]']*3*10*(pi*197.3269805)**2
noy50['sigma_002'] = noy50['U=000MeV']*noy50['E[MeV]']*3*10*(pi*197.3269805)**2
noy50['sigma_005'] = noy50['U=000MeV']*noy50['E[MeV]']*3*10*(pi*197.3269805)**2
noy50['sigma_008'] = noy50['U=000MeV']*noy50['E[MeV]']*3*10*(pi*197.3269805)**2
noy50['sigma_010'] = noy50['U=000MeV']*noy50['E[MeV]']*3*10*(pi*197.3269805)**2
noy50['sigma_020'] = noy50['U=000MeV']*noy50['E[MeV]']*3*10*(pi*197.3269805)**2
noy50['sigma_030'] = noy50['U=000MeV']*noy50['E[MeV]']*3*10*(pi*197.3269805)**2
noy50['sigma_050'] = noy50['U=000MeV']*noy50['E[MeV]']*3*10*(pi*197.3269805)**2
noy50['sigma_070'] = noy50['U=000MeV']*noy50['E[MeV]']*3*10*(pi*197.3269805)**2
noy50['sigma_100'] = noy50['U=000MeV']*noy50['E[MeV]']*3*10*(pi*197.3269805)**2

noy50.tail(10)

def quelU(U):
  if U==0 or U==00 or U==000:
    return('sigma_000')
  if U==2:
    return('sigma_002')
  if U==5:
    return('sigma_005')
  if U==8:
    return('sigma_008')
  if U==10:
    return('sigma_010')
  if U==20:
    return('sigma_020')
  if U==30:
    return('sigma_030')
  if U==50:
    return('sigma_050')
  if U==70:
    return('sigma_070')
  if U==100:
    return('sigma_100')


def traçageisotopetheo(U,maxoumin):
  plt.figure(1, figsize=(15,15))
  if maxoumin=='min':
    L=[112,114,116,117,118,119,120,122,124]
  if maxoumin=='max':
    L=[126,128,130,132,134,136,138,140,142,144,146,148,150,152,154,156]
  if maxoumin=='minmax':
     L=[112,114,116,117,118,119,120,122,124,126,128,130,132,134,136,138,140,142,144,146,148,150,152,154,156]
  f1=quelU(U)
  for i in range(len(L)):
    A=L[i]
    plt.plot(noy50.loc[(noy50['Z']==50) & (noy50['A']==A),:]['E[MeV]'],noy50.loc[(noy50['Z']==50) & (noy50['A']==A),:][f1])
  plt.xlabel('E en MeV')
  plt.ylabel('Sigma en mb')
  plt.title('isotopes de Z=50')

print(traçageisotopetheo(0,'min'))

Xprime=[]
liste=df["Z"]
for i in range(len(liste)):
    Xprime.append(liste[i])

Xprimeprime=[]
liste2=df["A"]
for i in range(len(liste)):
    Xprimeprime.append(liste2[i])

X=[]
for i in range(len(liste)):
    X.append((liste[i],liste2[i]))


Z=[]
Ztext=[]


Xessai=X
while len(Xessai)>=32:
    a=Xessai[0]
    Z.append(a)
    i=0
    while Xessai[i]==a:
        i=i+1
    del Xessai[0:i]

Z.append((94,239))

def traçageisotopebdd(Ubs):
  plt.figure(1, figsize=(15,15))
  L=[]
  U=float(Ubs)
  for i in range(len(Z)):
    if Z[i][0]==U:
      L.append(Z[i])
  L=sorted(L)
  for j in range(len(L)):
    A=L[j]
    plt.plot(df.loc[(df['Z']==L[j][0]) & (df['A']==L[j][1]),:]['E'],df.loc[(df['Z']==L[j][0]) & (df['A']==L[j][1]),:]['sigma'],linewidth=1)
  plt.xlabel('E en MeV')
  plt.ylabel('Sigma en mb')
  plt.title(Ubs)

print(traçageisotopebdd(50))

Xprime=[]
liste=df["Z"]
for i in range(len(liste)):
    Xprime.append(liste[i])

Xprimeprime=[]
liste2=df["A"]
for i in range(len(liste)):
    Xprimeprime.append(liste2[i])

X=[]
for i in range(len(liste)):
    X.append((liste[i],liste2[i]))


Z=[]
Ztext=[]


Xessai=X
while len(Xessai)>=32:
    a=Xessai[0]
    Z.append(a)
    i=0
    while Xessai[i]==a:
        i=i+1
    del Xessai[0:i]

Z.append((94,239))

def predictionsurbaseid(Z,A):
    X=[]
    abcisses=[]
    for i in range(101):
      L=[]
      L.append(Z)
      L.append(A)
      L.append(5+i*0.2)
      L.append(0)
      X.append(L)
      abcisses.append(5+i*0.2)
    Xnewa=np.array(X)
    Xnewa= scaler_x.transform(Xnewa)
    ynewa= model.predict(Xnewa)
    ynewfi = scaler_y.inverse_transform(ynewa) 
    Xnewfi = scaler_x.inverse_transform(Xnewa)
    return(abcisses,ynewfi)
    """plt.plot(abcisses, ynewfi,color="green", linewidth=1.5, linestyle="-")"""

def traçageisotopeneuro(Ubs):
  plt.figure(1, figsize=(15,15))
  L=[]
  U=float(Ubs)
  for i in range(len(Z)):
    if Z[i][0]==U:
      L.append(Z[i])
  L=sorted(L)
  for j in range(len(L)):
    A=L[j]
    X=predictionsurbaseid(L[j][0],L[j][1])[0]
    Y=predictionsurbaseid(L[j][0],L[j][1])[1]
    plt.plot(X,Y)
    plt.xlabel('E en MeV')
    plt.ylabel('Sigma en mb')
    plt.title(Ubs)

print(traçageisotopeneuro(50))

plt.figure(1, figsize=(30,10))
plt.suptitle('Courbes de Sigma en fonction de E pour les 3 modèles :   Théorique, Expérimental, Neuronal    pour les isotopes de Sn (Z=50) ')
plt.subplot(131)
plt.text(13, 50, 'A=112', horizontalalignment = 'center', verticalalignment = 'center')
traçageisotopetheo(0,'min')
plt.title('QRPA')
plt.subplot(132)
traçageisotopebdd(50)
plt.title('Données')
plt.text(13, 50, 'A=112', horizontalalignment = 'center', verticalalignment = 'center')
plt.text(13, 250, 'A=124', horizontalalignment = 'center', verticalalignment = 'center')
plt.subplot(133)
traçageisotopeneuro(50)
plt.title('Modèle Neuronal')
plt.text(13, 50, 'A=112', horizontalalignment = 'center', verticalalignment = 'center')
plt.text(13, 250, 'A=124', horizontalalignment = 'center', verticalalignment = 'center')
plt.show()

plt.figure(1, figsize=(30,10))
plt.suptitle('Résultats expérimentaux pour les isotopes de Sn')
plt.subplot(131)
traçageisotopebdd(40)
plt.subplot(132)
traçageisotopebdd(50)
plt.subplot(133)
traçageisotopebdd(60)
plt.show()

plt.figure(1, figsize=(30,10))
plt.suptitle('Résultats des prédictions par le réseau de neurone pour les isotopes de Sn')
plt.subplot(131)
traçageisotopeneuro(40)
plt.subplot(132)
traçageisotopeneuro(50)
plt.subplot(133)
traçageisotopeneuro(60)
plt.show()

M=[]
for i in range(17):
  M.append((50,124+2*i))


def traçageisotopeneuro(Ubs):
  plt.figure(1, figsize=(15,15))
  L=[]
  U=float(Ubs)
  for i in range(len(Z)):
    if Z[i][0]==U:
      L.append(Z[i])
  L=sorted(L)
  for i in range(17):
    L.append((50,124+2*i))
  print(L)
  for j in range(len(M)):
    A=M[j]
    X=predictionsurbaseid(50,L[j][1])[0]
    Y=predictionsurbaseid(50,L[j][1])[1]
    plt.plot(X,Y)
    plt.xlabel('E en MeV')
    plt.ylabel('Sigma en mb')
    plt.title(Ubs)

traçageisotopeneuro(50)

plt.figure(1, figsize=(20,10))
plt.subplot(121)
plt.text(13, 50, 'A=126', horizontalalignment = 'center', verticalalignment = 'center')
plt.text(13, 250, 'A=156', horizontalalignment = 'center', verticalalignment = 'center')
traçageisotopetheo(0,'max')
plt.subplot(122)
traçageisotopeneuro(50)
plt.text(13, 50, 'A=126', horizontalalignment = 'center', verticalalignment = 'center')
plt.text(13, 280, 'A=156', horizontalalignment = 'center', verticalalignment = 'center')
plt.show()