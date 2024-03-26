""" Exemple 1 """

""" nb_etudiant = input("Entrer le nombre d'étudiants : ")
print(type(nb_etudiant))
nb_etudiant=int(nb_etudiant)
f1 = input("\nEntrez un flottant : ")
f1 = float(f1)
f2 = float(input("Entrez un autre flottant : "))
print(type(f2)) """

""" Exemple 2 """
"""Remplace simple"""
print("{} {} {}".format("zéro", "un", "deux"))
print("{2} {0} {1}".format("zéro", "un", "deux"))
print("Je m'appelle {}".format("El Mahdi"))
print("{}".format("-" * 10))

"""Remplace avec champs nommés"""
a,b =5,3
print("the stroy of {c} and {d}".format(c=a+b, d=a-b))

"""formatages a l'aide de liste"""
stock = ['papier', 'eveloppe', 'chemise', 'encre', 'buvard']
print("Nous avons de l'{0[3]} et du {0[0]} en stock \n".format(stock))

"""formatage a l'aide de dictionnaire"""
print("My name is {0[name]}".format(dict(name= "el mahdi")))
d=dict(animal = 'elephant', poids = 12000)
print("L'{0[animal]} pèse {0[poids]} kg\n".format(d))

"""Remplacement avec attributs nommées"""
import math 
import sys
print("math.pi = {.pi}, epsilon = {.float_info.epsilon}".format(math, sys))

""""""
print("{0} {0:b} {0:o} {O:x}".format(179)) 
n = 100
pi = 3.1415926535897931
print ("{}, et {}", format (n, pi)) 
print ("{}, et {}". format (n, pi)) 
print ("{0}, {1} et {0}", format (n, pi)) 
print (" {:.4e}", format (pi)) 
print (" {:g}". format (pi)) 
msg = "Résultat sur {:d} échantillons : {:. 21}". format (n, pi)
print (msg) 