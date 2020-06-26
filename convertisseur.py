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
    if len(remodelage)>16:

        entetes=['Z','A','E','dE','f1','df1']

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
                valeurs.append(petite)
            else:
                print('listevide mais bdd adapatée au pb')

        for valeur in valeurs:
            ligne = ";".join(valeur) + "\n"
            f.write(ligne)

f.close()

# CONVERTIR TOUS LES FICHIERS DE LA BDD EN .CSV

chemin = r'/Users/pierre-etiennepion/Desktop/photonuclear'  """CHANGER LE CHEMIN"""
tous_fichiers = glob.glob(chemin + "/*.dat")

for fichiers in tous_fichiers:
    print(fichiers)
    creationcsv(fichiers)

