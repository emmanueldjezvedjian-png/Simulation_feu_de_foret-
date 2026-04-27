import random as rd
import pytest 

def init_forest_2(x,y,density=0.6): # L représente la largeur du carré qui représente l'univers foret 
    forest=[[3 for i in range(x)] for j in range(y)]  # l'entier 2 représente un espace vide sur l'espace
    for i in range(x):
        for j in range(y):
            if rd.random()<density:
                forest[i][j]=0 # la valeur 0 représente un arbre sain (qui ne brule pas)
    return forest
 
def compt_arbre(forest): #fonction qui compte le nombre d'arbre dans une forêt
        compt=0
        t=len(forest)
        for i in range(t):
            for j in range(t):
                if forest[i][j]==1: compt+=1
        return compt