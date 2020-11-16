#!/usr/bin/python3
# coding: utf-8


n = int(input(“Entrez le nombre dont on veut la somme avec tous ses précédents : “))


i = n
calcul_correspondant = “La somme des chiffres de 1 à ”  + str(n) + “ est  “
while (i > 1):
  n += (i -1)
  calcul_correspondant = calcul_correspondant + str(i)  + “+”
  i += - 1
print (calcul_correspondant + “1 soit : ”+str(n)+”.”)




# ------------------------------------------------------------------- Résultat -----------------------------------------------------------------------------