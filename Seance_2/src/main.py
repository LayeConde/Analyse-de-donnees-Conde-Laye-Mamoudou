# Codage collectif de la s&ance 2 : Laye Mamoudou Condé et Remi Hellemot

#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def listedesterritoires(territoiretest, exportationUSD, importationUSD):
    listedesterritoires = [[territoiretest[0], 0]]
    pos = 0
    for element in range(0,len(territoiretest)):
        if territoiretest[element] != listedesterritoires[pos][0]:
            listedesterritoires.append([territoiretest[element], element])
            pos += 1
    lignes = []
    for element in range(1,len(listedesterritoires)):
        lignes.append(listedesterritoires[element][1] - 1)
    lignes.append(len(territoiretest))
    liste = []
    for element in range(0,len(listedesterritoires)):
        liste.append([listedesterritoires[element][0], listedesterritoires[element][1], lignes[element]])
    totalparterritoire = []
    for element in range(0,len(liste)):
        totalparterritoire.append([liste[element][0], exportationUSD[liste[element][1]:liste[element][2]].sum(), importationUSD[liste[element][1]:liste[element][2]].sum()])
    return totalparterritoire

def nettoyage(colonne):
    colonne2 = []
    for element in colonne:
        if element == 'Sans objet' or element =='-':
            colonne2.append(float(0))
        else:
            colonne2.append(float(element))
    return colonne2

def getliste(territoiretest):
    listedesterritoires = [[territoiretest[0], 0]]
    pos = 0
    for element in range(0,len(territoiretest)):
        if territoiretest[element] != listedesterritoires[pos][0]:
            listedesterritoires.append([territoiretest[element], element])
            pos += 1
    lignes = []
    for element in range(1,len(listedesterritoires)):
        lignes.append(listedesterritoires[element][1] - 1)
    lignes.append(len(territoiretest))
    liste = []
    for element in range(0,len(listedesterritoires)):
        liste.append([listedesterritoires[element][0], listedesterritoires[element][1], lignes[element]])
    return liste

# Question 4
print("Question 4")
# Source des données : https://www.cepii.fr/CEPII/en/bdd_modele/bdd_modele_item.asp?id=37
with open("C:/Users/DELL/Desktop/CONDE_M1_Anna_donnees/Seance_2/src/data/Afrique-2024.csv", "r", encoding="utf-8") as fichier:
    contenu = pd.read_csv(fichier, sep=",")
    print(contenu)
    


# Question 5
print("Question 5")
print("Nombre de lignes :", len(contenu))
print("Nombre de colonnes :", len(contenu.columns))

# Question 6
print("Question 6")
print(contenu.head())

# Question 7
print("Question 7")
print(contenu.columns)

# Question 8
print("Question 8")
print(contenu.dtypes)

# Contenu des colonnes
# "year" : année
# "origin_id" : territoire de référence
# "dest_id" : territoire partenaire
# "Dist_VO (km)" : distance intercentroïde entre les deux territoires
# "hs92_Section_id" : code Section du produit
# "hs92_HS02_id" : code 2-digit du produit
# "hs92_HS04_id" : code 4-digit du produit
# "hs92_HS06_id" : code 6-digit du produit
# "export_val" : valeur des exportations du territoire de référence vers le territoire partenaire en dollars courants
# "import_val" : valeur des importations du territoire partenaire vers le territoire de référence en dollars courants
# "export_ton" : valeur des exportations du territoire de référence vers le territoire partenaire en tonnes
# "import_ton" : valeur des importations du territoire partenaire vers le territoire de référence en tonnes

# Question 9
print("Question 9")
export_ton = contenu["export_ton"]
import_ton = contenu["import_ton"]

print("Exportations en tonnes :")
print(export_ton)

print("Importations en tonnes :")
print(import_ton)

# Question 10
print("Question 10")
export_ton_nettoye = nettoyage(export_ton)
import_ton_nettoye = nettoyage(import_ton)

total_exportations = sum(export_ton_nettoye)
total_importations = sum(import_ton_nettoye)

print("Total des exportations en tonnes :", total_exportations)
print("Total des importations en tonnes :", total_importations)

# Question 11
print("Question 11")
# Appliquer la fonction listedesterritoires(...) sur vos colonnes ici

territoires=contenu["origin_id"]
exportations = contenu["export_val"]
importations = contenu["import_val"]

total_par_territoire = listedesterritoires(territoires, exportations, importations)
print("total_par_territoire :", total_par_territoire)

print(total_par_territoire)

for element in total_par_territoire:

    code = element[0]
    exportation = element[1]
    importation = element[2]

    valeurs = [exportation, importation]
    etiquettes = ["Exportations", "Importations"]

    plt.figure()
    plt.pie(valeurs, labels=etiquettes, autopct="%1.1f%%")
    plt.title(code)

    plt.savefig("C:/Users/DELL/Desktop/CONDE_M1_Anna_donnees/Seance_2/src/img/" + code + ".png")
    plt.close()

# Questions 12 et 14
print("Questions 12 et 14")
# Application la fonction nettoyage(...) sur vos colonnes ici

distance = nettoyage(contenu["Dist_VO (km)"])
export_val_2 = nettoyage(contenu["export_val"])
import_val_2 = nettoyage(contenu["import_val"])
export_ton_2 = nettoyage(contenu["export_ton"])
import_ton_2 = nettoyage(contenu["import_ton"])

# Appliquer la fonction :
#liste = getliste(contenu["origin_id"])

# Mettre le code nouveau DataFrame ici et appeler la liste donnees2

donnees_2 = pd.DataFrame({
    "distance": distance,
    "exort_val_2": export_val_2,
    "import_val_2": import_val_2,
    "export_ton_2": export_ton_2,
    "import_ton_2": import_ton_2
})
    

# Compléter la boucle à partir des différents éléments précédents. Le nom des listes est celle proposée dans les commentaires.
 
liste = getliste(contenu["origin_id"])
parametres = []
quartiles = []
deciles = []

for element in range(0,len(donnees_2.columns)):
     
 parametres2 = []
distanceinterquartile = []
distanceinterdecile = []

for element2 in range(0,len(liste)):

 codeiso = liste[element2][0]

data2 =donnees_2.iloc[liste[element2][1]:liste[element2][2],element]
 
moyenne = data2.mean().round(decimals=2)
mediane = data2.median().round(decimals=2)
mode = data2.mode().iloc[0].round(decimals=2)
ecarttype = data2.std().round(decimals=2)
ecartabsolumoyen =(data2 - data2.mean()).abs().mean().round(decimals=2) 
etendue = (data2.max() - data2.min()).round(decimals=2)


parametres2.append([codeiso, moyenne, mediane, mode, ecarttype, ecartabsolumoyen, etendue])

quartile = data2.quantile([0.25, 0.5, 0.75])
distanceinterquartile.append([codeiso, (quartile[0.75] - quartile[0.25]).round(decimals=2)])
decile = data2.quantile([0.1, 0.9])
distanceinterdecile.append([codeiso, (decile[0.9] - decile[0.1]).round(decimals=2)])

parametres.append(parametres2)
quartiles.append(distanceinterquartile)
deciles.append(distanceinterdecile)



# Question 13
print("Question 13")

q1 = donnees_2["distance"].quantile(0.25)
q3 = donnees_2["distance"].quantile(0.75)

distance_interquartile = q3 - q1

print("Premier quartile :" , round(q1, 2))
print("Troisième quartile :" , round(q3, 2))
print("Distance interquartile :" , round(distance_interquartile, 2))

# Question 14
# print("Question 14")

d1 = donnees_2["distance"].quantile(0.10)
d9 = donnees_2["distance"].quantile(0.90)

distance_interdecile = d9 - d1

print("Premier décile :" , round(d1, 2))
print("Neuvième décile :" , round(d9, 2))
print("Distance interdécile :" , round(distance_interdecile, 2))

# Boxplots à partir des données quantitatives

for colonne in donnees_2.columns:
    plt.figure()
    plt.boxplot(donnees_2[colonne])
    plt.title("Boxplot - " + colonne)
    plt.ylabel(colonne)
    plt.savefig("C:/Users/DELL/Desktop/CONDE_M1_Anna_donnees/Seance_2/src/img/boxplot_" + colonne + ".png")
    plt.close()

# Question 15
print("Question 15")

classe_distance = [0, 2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000]

etiquettes_distance = ["0-2500", "2500-5000", "5000-7500", "7500-10000", "10000-12500", "12500-15000", "15000-17500", "17500-20000"]

donnees_2["classe_distance"] = pd.cut(donnees_2["distance"], bins=classe_distance, labels=etiquettes_distance, include_lowest=True)

print(donnees_2["classe_distance"])

# Question 16
print("Question 16")

repartition = donnees_2["classe_distance"].value_counts().sort_index()

plt.figure()

repartition.plot(kind="bar")

plt.title("Répartition des distances")
plt.xlabel("Classe de distance (km)")
plt.ylabel("Nombre de observations")

plt.savefig("C:/Users/DELL/Desktop/CONDE_M1_Anna_donnees/Seance_2/src/img/repartition_distances.png")
plt.close()

print(repartition)


# Question bonus
print("Question bonus")

noms_pays = pd.read_excel("./country_names.xls")

print(noms_pays)
print(noms_pays.columns)