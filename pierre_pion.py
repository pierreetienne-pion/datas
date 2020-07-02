# -*- coding: utf-8 -*-
"""pierre_pion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/162W5i5zCbYiB_CGA-f6RA-dDNy6NdEZC
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math import *

! git clone --recursive https://github.com/pierreetienne-pion/data.git

df = pd.read_csv("/content/data/bdd_159nucleons.csv")
df.head(10)

df.shape

df['sigma'] = df['f1']*df['E']*3*10*(pi*197.3269805)**2

df.head()

"""*VISUALISATION DE L'ÉVOLUTION DE LA VALEUR MAXIMALE DE SIGMA EN FONCTION DU NOMBRE ATOMIQUE Z*"""

Xprime=[]
liste=df["Z"]
for i in range(len(liste)):
    Xprime.append(liste[i])
    
X = list(set(Xprime))

g = df.groupby("Z")

Y=[]
for i in X:
    Y.append(g.get_group(i)["sigma"].max())

plt.plot(X,Y)
plt.title("Valeur maximale sigma en fonction de Z")
plt.xlabel("Z")
plt.ylabel("Sigma (mb)")
plt.show()

"""*VISUALISATION DE L'ÉVOLUTION DE LA VALEUR MOYENNE DE SIGMA EN FONCTION DU NOMBRE ATOMIQUE Z*"""

Xprime=[]
liste=df["Z"]
for i in range(len(liste)):
    Xprime.append(liste[i])
    
X = list(set(Xprime))

g = df.groupby("Z")

Y=[]
for i in X:
    Y.append(g.get_group(i)["sigma"].mean())

plt.plot(X,Y)
plt.title("Valeur moyenne sigma en fonction de Z")
plt.xlabel("Z")
plt.ylabel("Sigma (mb)")
plt.show()

"""COMPILATION DES DEUX DONNÉES"""

Xprime=[]
liste=df["Z"]
for i in range(len(liste)):
    Xprime.append(liste[i])
    
X = list(set(Xprime))

g = df.groupby("Z")

Y=[]
for i in X:
    Y.append(g.get_group(i)["sigma"].mean())

Y2=[]
for i in X:
    Y2.append(g.get_group(i)["sigma"].max())

plt.plot(X,Y)
plt.plot(X,Y2)
plt.title("Valeur sigma en fonction de Z")
plt.xlabel("Z")
plt.ylabel("Sigma (mb)")
plt.legend(['mean', 'max'], loc='upper left')
plt.show()

"""VISUALISATION DU NOMBRE DE VALEURS DES ÉNERGIES DISPONIBLE POUR CRITIQUER LES RÉSULTATS PRÉCÉDENTS"""

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

Y=[]

Xessai=X
while len(Xessai)>=32:
    a=Xessai[0]
    i=0
    while Xessai[i]==a:
        i=i+1
    Y.append(i)
    del Xessai[0:i]

Y.append(len(Xessai)+1)

Y2=sorted(Y)

Y3=[]

p1=0 #nombre de donnée inférieur à 20
p2=0 #nombre de données entre 20 et 50
p3=0 #nombre de données entre 50 et 100
p4=0 #nombre de données 100 et plus

for i in range(len(Y2)):
    if Y2[i]<=20:
        p1=p1+1
    if Y2[i]<=50 and Y2[i]>20:
        p2=p2+1
    if Y2[i]<=100 and Y2[i]>50:
        p3=p3+1
    if Y2[i]>100:
        p4=p4+1
Y3.append(p1)
Y3.append(p2)
Y3.append(p3)
Y3.append(p4)

name = ['0-20', '20-50', '50-100', '100+']
data = Y3

explode=(0, 0, 0, 0)
plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
plt.axis('equal')
plt.title('Répartition de la quantité de donnée disponible')
plt.show()

"""On voit que environ 4O% des données ne disposent pas de plus de 50 valeurs d'énergies différentes, ce qui suppose que la moyenne réalisée plus tôt (ou les maximums ) pour un Z ou le nombre de données est insuffisant est une mauvaise représentation globale (d'ou les pics et les variations soudaines)"""

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

Y=[]
Z=[]

Xessai=X
while len(Xessai)>=32:
    a=Xessai[0]
    Z.append(a)
    i=0
    while Xessai[i]==a:
        i=i+1
    Y.append(i)
    del Xessai[0:i]

Y.append(len(Xessai)+1)
Z.append((94,239))

Zprime=[]
for i in range(len(Z)):
    Zprime.append(str(Z[i]))


plt.plot(Zprime, Y)
plt.title("Nombre de donnée par Z,A")
plt.xlabel("(Z,A)")
plt.ylabel("nombre de données")
plt.show()

"""Ce graph est valable pour chaque (Z,A), il est utile pour comprendre ou se situent les manques de données. Seulement pour mieux comparer avec les graph précédents, on va étudier le nombre de valeurs seulement pour chaque Z, en faisant la moyenne du nombre de données pour chaque A du même Z."""

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

Y=[]
Z=[]

Xessai=X
while len(Xessai)>=32:
    a=Xessai[0]
    Z.append(a)
    i=0
    while Xessai[i]==a:
        i=i+1
    Y.append(i)
    del Xessai[0:i]

Y.append(len(Xessai)+1)
Z.append((94,239))

N=[]
M=[]

while len(Y)>1:
    a=Z[0][0]
    N.append(a)
    i=0
    s=0
    m=0
    while Z[i][0]==a:
        s=Y[i]+s
        i=i+1
    m=s/i
    M.append(m)
    del Z[0:i]
    del Y[0:i]

N.append(94)
M.append(32)

plt.plot(N,M)
plt.title("Nombre de donnée par Z")
plt.xlabel("Z")
plt.ylabel("nombre de données")
plt.show()

"""On peut donc comparer maintenant avec la courbe que l'on a tracée au début pour voir l'influence du nombre de valeurs sur la moyenne"""

Xeprime=[]
listee=df["Z"]
for i in range(len(listee)):
    Xeprime.append(listee[i])
    
Xe = list(set(Xeprime))

g = df.groupby("Z")

Ye=[]
for i in Xe:
    Ye.append(g.get_group(i)["sigma"].mean())

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

Y=[]
Z=[]

Xessai=X
while len(Xessai)>=32:
    a=Xessai[0]
    Z.append(a)
    i=0
    while Xessai[i]==a:
        i=i+1
    Y.append(i)
    del Xessai[0:i]

Y.append(len(Xessai)+1)
Z.append((94,239))

N=[]
M=[]

while len(Y)>1:
    a=Z[0][0]
    N.append(a)
    i=0
    s=0
    m=0
    while Z[i][0]==a:
        s=Y[i]+s
        i=i+1
    m=s/i
    M.append(m)
    del Z[0:i]
    del Y[0:i]

N.append(94)
M.append(32)

fig, axs = plt.subplots(2)
fig.suptitle('Comparaison entre l évolution moyenne de sigma en fonction de Z et la quantité de données en fonction de Z')
axs[0].plot(N, Ye)
axs[1].plot(N, M)

plt.show()

"""C'est assez clair ici que plus la quantité de donnée est faible, plus la valeur de la moyenne est élevée (on le voit surtout pour des Z importants) **cela montre que nos échantillons de données se situent surtout au niveau du pic de sigmaE1.**

Il est donc pertinent ici de savoir ou se situe le pic de sigmaE1 pour chaque Z (avec les données que l'on a)
"""

Xprime=[]
liste=df["Z"]
for i in range(len(liste)):
    Xprime.append(liste[i])
    
X = list(set(Xprime))

g = df.groupby("Z")

Y=[]
for i in X:
    Y.append(g.get_group(i)["sigma"].max())

Z=[]

for i in range(len(X)):
    Z.append(df.loc[(df['sigma']==Y[i]) & (df['Z'] == X[i]),:]['E'].max())
    
plt.plot(X,Z)
plt.title("Valeur en énergie du maximum du pic de sigma par Z")
plt.xlabel("Z")
plt.ylabel("énergie correspondant au max du pic en MeV")
plt.show()

"""On remarque que l'énergie correspondant au sigma max est en décroissance plus le Z augmente. Etant donné les conclusions que l'on a tiré au dessus. Cette courbe peut etre considérée comme complète vu ou se situent les données.

On peut maintenant essayer de voir la relation entre la valeur de l'énergie correspondant au sigma max et les isotopes d'un numero atomique Z
"""

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

Y=[]
Z=[]

Xessai=X
while len(Xessai)>=32:
    a=Xessai[0]
    Z.append(a)
    i=0
    while Xessai[i]==a:
        i=i+1
    Y.append(i)
    del Xessai[0:i]

Y.append(len(Xessai)+1)
Z.append((94,239))

def rechercheisotope(z):
    lis=[]
    for j in range(len(Z)):
        if z==Z[j][0]:
            for i in range(len(Z)):
                a=z
                if Z[i][0]==a:
                    lis.append(Z[i][1])
    lisprime= list(set(lis))
    lisprime=sorted(lisprime)
    return(lisprime)

def caractisotopes(z):
    a=rechercheisotope(z)
    SIGMA=[]
    E=[]
    for i in a:
        SIGMA.append(df.loc[(df['Z']==z) & (df['A'] == i),:]['sigma'].max())
        E.append(df.loc[(df['Z']==z) & (df['A'] == i) & (df['sigma']==df.loc[(df['Z']==z) & (df['A'] == i),:]['sigma'].max()),:]['E'].max())
    aprime=[]
    for i in range(len(a)):
        aprime.append(str(a[i]))
    figure = plt.figure(figsize = (5, 5))
    plt.gcf().subplots_adjust(left = 0.1, bottom = 0.1,
                       right = 0.9, top = 0.9, wspace = 0, hspace = 0.5)
    axes = figure.add_subplot(2, 1, 1)
    axes.set_xlabel('différents isotopes du Z entré')
    axes.set_ylabel('E (MeV)')
    axes.set_title('Évolution de l energie atteinte à sigmamax pour les différents isotopes')
    axes.plot(aprime, E, color = 'blue')
    axes = figure.add_subplot(2, 1, 2)
    axes.set_xlabel('différents isotopes du Z entré')
    axes.set_ylabel('Sigmamax (mb)')
    axes.set_title('evolution de sigmamax pour les différents isotopes')
    axes.plot(aprime, SIGMA, color = 'red')
    plt.show()

print(caractisotopes(60))

"""On peut tester pour plusieurs valeurs de Z, et on remarquera des comportements des fois étranges des évolutions.

On peut maintenant s'attaquer à la représentation des énergies centroides. Comme on peut le voir sur https://arxiv.org/pdf/1607.08483.pdf figure6. En partant de l'équation 7 pour la modélisation
"""

def centroid(A):
    omegan=[]
    n=df.loc[df['A']==A,:]['E'].shape[0]
    for i in range(n):
        omegan.append(df.loc[df['A']==A,:]['E'].iloc[i])
    BE1=[]
    for j in range(n):
        BE1.append(df.loc[(df['A']==A) & (df['E']==omegan[j]),:]['f1'].iloc[0])
    numerateur=0
    denominateur=0
    for k in range(n):
        numerateur=numerateur+omegan[k]*BE1[k]
        denominateur=denominateur+BE1[k]
    return(numerateur/denominateur)
    

Xprime=[]
liste=df["A"]
for i in range(len(liste)):
    Xprime.append(liste[i])
    
X = list(set(Xprime))
Y=[]
for i in range(len(X)):
    Y.append(centroid(X[i]))

plt.scatter(X,Y)
plt.title("centroid energies of the yamma distributions")
plt.xlabel("Mass number A")
plt.ylabel("Centroid energy (MeV) ")
plt.show()

"""On peut remarquer la forte ressemblance avec la courbe du document figure 6.

Et on peut maintenant essayer de représenter la figure 7 de ce même document en intégrant f_gamme*E sur l'energie
"""

def E1EWSR(A):
    Z=df.loc[df['A']==A,:]['Z'].iloc[0]
    N=A-Z
    omegan=[]
    a=df.loc[df['A']==A,:]['E'].min()
    b=df.loc[df['A']==A,:]['E'].max()
    n=df.loc[df['A']==A,:]['E'].shape[0]
    for i in range(n):
        omegan.append(df.loc[df['A']==A,:]['E'].iloc[i])
    BE1=[]
    for j in range(n):
        BE1.append(df.loc[(df['A']==A) & (df['E']==omegan[j]),:]['f1'].iloc[0])
    h=(b-a)/float(n)
    z=0.5*(omegan[n-1]*BE1[n-1]+omegan[0]*BE1[0])
    for i in range(1,n):
        z=z+omegan[i]*BE1[i]
    return (h*z)
    
#*(A/(14.8*N*Z)) pour convertir en TRK units??

Xprime=[]
liste=df["A"]
for i in range(len(liste)):
    Xprime.append(liste[i])
    
X = list(set(Xprime))
Y=[]
for i in range(len(X)):
    Y.append(E1EWSR(X[i]))

plt.scatter(X,Y)
plt.ylim(-0.00005,0.0004)
plt.show()

"""L'allure n'est pas exactement la même, même sil'on observe une croissance. Cela est du aux unités. Je vais essayer de convertir ce résultat avec les données du pdf."""

def E1EWSR(A):
    Z=df.loc[df['A']==A,:]['Z'].iloc[0]
    N=A-Z
    omegan=[]
    a=df.loc[df['A']==A,:]['E'].min()
    b=df.loc[df['A']==A,:]['E'].max()
    n=df.loc[df['A']==A,:]['E'].shape[0]
    for i in range(n):
        omegan.append(df.loc[df['A']==A,:]['E'].iloc[i])
    BE1=[]
    for j in range(n):
        BE1.append(df.loc[(df['A']==A) & (df['E']==omegan[j]),:]['f1'].iloc[0])
    h=(b-a)/float(n)
    z=0.5*(omegan[n-1]*BE1[n-1]+omegan[0]*BE1[0])
    for i in range(1,n):
        z=z+omegan[i]*BE1[i]
    return (h*z*A/(14.8*N*Z))

Xprime=[]
liste=df["A"]
for i in range(len(liste)):
    Xprime.append(liste[i])
    
X = list(set(Xprime))
Y=[]
for i in range(len(X)):
    Y.append(E1EWSR(X[i]))

plt.scatter(X,Y)
plt.ylim(-1e-7,6e-7)
plt.show()

"""Voir validité de la conversion??

MAPING des noyaux disponibles dans notre Database
"""

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

Xessai=X
while len(Xessai)>=32:
    a=Xessai[0]
    Z.append(a)
    i=0
    while Xessai[i]==a:
        i=i+1
    del Xessai[0:i]

Z.append((94,239))

N=[]
for i in range(len(Z)):
    N.append(Z[i][1]-Z[i][0])

Zprime=[]
for i in range(len(Z)):
    Zprime.append(Z[i][0])
    
fig = plt.figure(1, figsize=(10,10))
plt.scatter(N,Zprime,c='r',s=5,marker='s')
plt.title('Schematic overview of the different (N,Z) we have in our database')
plt.xlabel('Number of neutrons')
plt.ylabel('Number of protons')
plt.hlines(20,0,40,linestyles='dotted')
plt.hlines(28,0,55,linestyles='dotted')
plt.hlines(50,20,90,linestyles='dotted')
plt.hlines(82,85,140,linestyles='dotted')
plt.vlines(20,0,30,linestyles='dotted')
plt.vlines(28,0,50,linestyles='dotted')
plt.vlines(50,20,82,linestyles='dotted')
plt.vlines(82,28,82,linestyles='dotted')
plt.vlines(126,28,90,linestyles='dotted');
plt.show()

plt.scatter(df.A-df.Z,df.Z)
plt.hlines(20,0,40)
plt.hlines(28,0,55)
plt.hlines(50,20,90)
plt.hlines(82,85,140)
plt.vlines(20,0,30)
plt.vlines(28,0,50)
plt.vlines(50,20,82)
plt.vlines(82,28,82)
plt.vlines(126,28,90);

"""Algo pour représenter un panel de graph de sigma en fonction de E. 
pas très optimisé mais fonctionnel. PB au niveau d'un dernier graph qui décalle tout..
"""

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
    plt.plot(E,sigma)
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
        plt.subplot(m[0],m[1],1)
        for i in range(n):
            Zbarre=Zspon[i][0]
            Abarre=Zspon[i][1]
            graph(Zbarre,Abarre)
            plt.subplot(m[0],m[1],i+2)

plt.show()

plt.xlabel('Sigma en mb')
plt.ylabel('E en MeV')
a=panel(49,49)

print(a)

noy50 = pd.read_csv("/content/data/Z=50QRPAs.csv")
noy50.head(10)