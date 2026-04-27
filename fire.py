
import random 


#func_fire créer le départ de feu

def func_fire(fire,forest):
    L = len(forest)
    if fire == "vertical":
        fire = [[0 for i in range(L)] for j in range(L)]
        for k in range(L):
            fire[k][0] = 1
    if fire == "horizontal":
        fire = [[0 for i in range(L)] for j in range(L)]
        for k in range(L):
            fire[0][k] = 1
    if fire == "cube":
        fire = [[1,1],[1,1]]
    if fire == "solo":
        fire = [[1]]
    return fire 




        

