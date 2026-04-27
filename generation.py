from regle_propagation_continue import *
import init_forest 
import numpy as np

#generation est une fonction qui applique les règle à toutes les cellules de la forêt

def genereation_continue(forest,p_card,v_vent,dt):
    L=len(forest)
    forest = np.array(forest)
    new_forest=np.zeros((L,L),dtype=float)
    for col in range(L):
        for row in range(L):
            new_forest[col][row]=regles_continue(p_card,forest,col,row,v_vent,dt)
    return new_forest



