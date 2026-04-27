import random as rd
import math

def sens_vent(pt_card, forest, x, y):
    Cibles = []
    
    # Vérification des limites de la grille (pour éviter des erreurs d'index)
    max_x = len(forest)
    max_y = len(forest[0])

    # Fonction pour ajouter un voisin si l'indice est valide
    def ajouter_voisin(i, j):
        if 0 <= i < max_x and 0 <= j < max_y:
            Cibles.append(forest[i][j])

    # Selon la direction du vent, ajouter les voisins
    if pt_card == "South":
        ajouter_voisin(x - 2, y)
        ajouter_voisin(x - 3, y)
    
    elif pt_card == "South_West":
        ajouter_voisin(x - 2, y + 2)
        ajouter_voisin(x - 3, y + 3)

    elif pt_card == "West":
        ajouter_voisin(x, y + 2)
        ajouter_voisin(x, y + 3)

    elif pt_card == "North_West":
        ajouter_voisin(x + 2, y + 2)
        ajouter_voisin(x + 3, y + 3)

    elif pt_card == "North":
        ajouter_voisin(x + 2, y)
        ajouter_voisin(x + 3, y)

    elif pt_card == "North_East":
        ajouter_voisin(x + 2, y - 2)
        ajouter_voisin(x + 3, y - 3)

    elif pt_card == "East":
        ajouter_voisin(x, y - 2)
        ajouter_voisin(x, y - 3)

    elif pt_card == "South_East":
        ajouter_voisin(x - 2, y - 2)
        ajouter_voisin(x - 3, y - 3)

    return Cibles

def f(v_vent):
    return (1/6000)*v_vent + (3/200)*v_vent + 5/6
 
def effet_vent(pt_card,forest, x, y, v_vent):
    t = len(forest)-1
    cell = forest[x][y]  # Utilisez forest[x][y] pour accéder à l'élément
    
    if cell == 2 or cell == 3:  # Si il n'y a pas d'arbre, la cellule reste vide
        return cell
    if cell == 1:  # Teste si la cellule est en train de brûler
        cell = 2
        return cell
    if x==0 and y!=0 and y!=t:
        Voisins=[forest[x][(y-1)],forest[x][(y+1)],forest[(x+1)][y],forest[x+1][y-1],forest[x+1][y+1]]
    elif x==t and y!=0 and y!=t:
        Voisins=[forest[(x-1)][y],forest[x][(y-1)],forest[x][(y+1)],forest[x-1][y-1],forest[x-1][y+1]]
    elif y==0 and x!=0 and x!=t:
        Voisins=[forest[(x-1)][y],forest[x][(y+1)],forest[(x+1)][y],forest[x-1][y+1],forest[x+1][y+1]]
    elif y==t and x!=0 and x!=t:
        Voisins=[forest[(x-1)][y],forest[x][(y-1)],forest[(x+1)][y],forest[x-1][y-1],forest[x+1][y-1]]
    elif y==t and x==t:
        Voisins=[forest[(x-1)][y],forest[x][(y-1)],forest[x-1][y-1]]
    elif y==t and x==0:
        Voisins=[forest[x][(y-1)],forest[(x+1)][y],forest[x+1][y-1]]
    elif x==t and y==0:
        Voisins=[forest[(x-1)][y],forest[x][(y+1)],forest[x-1][y+1]]
    elif x==0 and y==0:
        Voisins=[forest[x][(y+1)],forest[(x+1)][y],forest[x+1][y+1]]

    if x!=t and x!=0 and y!=0 and y!=t : Voisins=[forest[x][(y-1)],forest[x][y+1],forest[x+1][y],forest[x-1][y],forest[x-1][y-1],forest[x-1][y+1],forest[x+1][y-1],forest[x+1][y+1]]
    
    if cell==0: #test la condition : la cellule est un arbre sain
        compteur = 0  #Compte le nombre de voisins en feu
        for i in Voisins:
            if i==1:
                compteur = compteur + 1
    if compteur == 0:
            p = 0
    else :
        p = 0.9 ** (8-compteur)

    Cibles = sens_vent(pt_card,forest,x,y)

    """
    if v_vent < 10 : 
        p = p
    """
    
    if len(Cibles) == 1:
        if Cibles[0] == 1:
             compteur += 0.6 #On rajoute moins que 1 car son importance est moins significative que les "vrais" voisins
        if compteur == 0:
            p = 0
        else:
            p= 0.9**(8.6-compteur)
            p = 1 - (1-p)**(f(v_vent)) # Nouvelle proba prenant en compte les nouveaux voisins causés par le vent

    if len(Cibles) == 2:
        if Cibles[0] == 1:
            compteur += 0.6 
        if Cibles[1] == 1:
            compteur += 0.2
        if compteur == 0 :
            p=0
        else:
            p= 0.9**(8.8-compteur)
            p = 1 - (1-p)**(f(v_vent)) # Nouvelle proba prenant en compte les nouveaux voisins causés par le vent


    if rd.random() < p:
        cell =1
    else: 
        cell = 0
    return int(cell)
        
