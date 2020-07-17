#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:43:20 2020

@author: pierre-etiennepion
"""
#POUR FAIRE TOURNER L'ALGO, PLACER LE FICHIER .PY DANS LE DOSSIER PHOTONUCLEAR, PUIS REMPLACER LE CHEMIN DU DOSSIER PHOTONUCLEAR PAR CELUI DE VOTRE PC
#https://www-nds.iaea.org/PSFdatabase/ BDD 159 nucleis SEULEMENT!


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np  
import csv
import glob

#CRÉATION D'UN FICHIER .CSV À PARTIR D'UN .DAT DANS LA BASE DE DONNÉES https://www-nds.iaea.org/PSFdatabase/

def creationcsv(fichiersdat):
    remodelage = [i.strip().split() for i in open(fichiersdat).readlines()]
    if len(remodelage)>15:

        entetes=['Z','A','E','dE','f1','df1','type of reaction','year','author_3']

        Aprime=remodelage[2][-1]

        if Aprime[0]=='=':
            A=Aprime[1:len(Aprime)]

        if Aprime[0]!='=':
            A=Aprime

        Zprime=remodelage[2][3]

        if Zprime[-1]==',':
            Z=Zprime[0:len(Zprime)-1]
        if Zprime[-1]!=',':
            Z=Zprime
        
        liste=[]
        anneeli=[]
        author=[]
        typereact=[]
        for i in range(len(remodelage[0][1])):
            liste.append(remodelage[0][1][i])

        for i in range(16):
            del liste[0]
    

        while liste[0]!='_':
            typereact.append(liste[0])
            del liste[0]

        for i in range(4):
            anneeli.append(liste[i+1])
        
        for i in range(3):
            author.append(liste[i+5])
        
        autheur=author[0]+author[1]+author[2]
        
        typereaction=0
        
        if len(typereact)==9:
            typereaction='photoneut'
        
        if len(typereact)==8:
            typereaction='photoabs'
        
        if len(typereact)!=8 or len(typereact)!=9:
            if typereact[-1]=='r':
                typereaction='photoneut'
            if typereact[0]=='a':
                typereaction='photoabs'
        
        if len(typereact)==7:
            typereaction='photoabs'
        
        typereaction2=typereaction
        
        if typereaction==0:
            print(remodelage)
            print(typereact)
 
        année=anneeli[0]+anneeli[1]+anneeli[2]+anneeli[3]
        
        final=remodelage[0][1]
        finale=final+".csv"
        f = open(finale, 'w')

        ligneEntete = ";".join(entetes) + "\n"
        f.write(ligneEntete)

        valeurs=[]
        for i in range(len(remodelage)-11):
            if len(remodelage[-1])>0:
                petite=[]
                petite.append(Z)
                petite.append(A)
                petite.append(remodelage[11+i][0])
                petite.append(remodelage[11+i][1])
                petite.append(remodelage[11+i][2])
                petite.append(remodelage[11+i][3])
                petite.append(typereaction2)
                petite.append(année)
                petite.append(autheur)
                valeurs.append(petite)
            else:
                b=0

        for valeur in valeurs:
            ligne = ";".join(valeur) + "\n"
            f.write(ligne)
            
    else :
        print('fichier avec 2 données ou moins')
        print(fichiersdat)
        


 
# CONVERTIR TOUS LES FICHIERS DE LA BDD EN .CSV

chemin = r'/Users/pierre-etiennepion/Desktop/photonuclear-4'
tous_fichiers = glob.glob(chemin+"/*.dat")

for fichiers in tous_fichiers:
        creationcsv(fichiers)

    
"""
filin = open("list_to_predict.txt", "r")
lignes = filin.readlines()

def reformater(a):
    b=''
    for i in range(len(fichier)-49):
        b=b+fichier[49+i]
    return(b)


def reformater_slashn(a):
    b=''
    long=len(a)-1
    for i in range(long):
        b=b+a[-2-i]
    return("".join(reversed(b)))
        

compteur=0
for ligne in lignes:
    a=reformater_slashn(ligne)
    for fichier in tous_fichiers:
        niquel=reformater(fichier)
        if a==niquel:
            creationcsv(fichier)
            compteur=compteur+1

"""




        
    
