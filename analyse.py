# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 17:38:33 2019
Recherche de valeur maximale de production
@author: renaud.depradel sylvain.chaillou ...
"""
import csv
#Récupération des données dans le fichier csv
liste_des_donnees=[]  #liste_des_donnees est la variable qui varecevoir les données sous forme de liste
#ouverture du fichier csv
with open('prod-region-annuelle-filiere.csv' , encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    #parcours de chaque ligne du fichier
    for row in reader:
        #ajoute à la liste des Production bioénergies (GWh) si le code INSEE est celui des Pays de Loire
       if (row['Code INSEE région']=='52'): #teste le code INSEE
           liste_des_donnees.append (float(row['Production bioénergies (GWh)']))   #ajoute à la liste des données
 
maximum=0
for i in range (0,len(liste_des_donnees)) :
    
    #      a compléter
    
    
    

print ("la production annuelle maximum a été de ",maximum )
