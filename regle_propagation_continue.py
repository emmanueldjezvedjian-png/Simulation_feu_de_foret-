import random as rd
from Wind_effect import sens_vent

def regles_continue(pt_card,forest, x, y, v_vent,dt):
    t = len(forest)-1
    compteur=0
    cell = forest[x][y]  # Utilisez forest[x][y] pour accéder à l'élément
    
    if 2<=cell:  # Si il n'y  a pas d'arbre, la cellule reste vide
        return cell
    if 0< cell <=1:
        cell+=dt
        return cell
    if 1< cell <2:
        cell+=2*dt
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
    

    def f_poly_1(x): #fonction polynomiale qui vaut 0 pour x=0 et x=2 et un maximum de 1 pour x=1
        if 0<=x<=2:
            return -x**2+2*x
        if x>2: 
            return 0
    def f_poly_06(x): #fonction polynomiale qui vaut 0 pour x=0 et x=2 et un maximum de 0,6 pour x=1
        if 0<=x<=2: return -0.6*x**2+1.2*x
        if x>2:
            return 0
    def f_poly_O2(x):#fonction polynomiale qui vaut 0 pour x=0 et x=2 et un maximum de 0.2 pour x=1
        if 0<=x<=2: return -0.2*x**2+0.4*x
        if x>2:
            return 0

    Cibles = sens_vent(pt_card,forest,x,y)
    
    for i in Voisins:                                
        compteur+=f_poly_1(i)       #Compte le nombre de voisins en feu
    
    if len(Cibles)!=0: 
        if len(Cibles) == 1:
            if 0<Cibles[0] <2:
                compteur +=f_poly_06(Cibles[0])  #On rajoute moins que 1 car son importance est moins significative que les "vrais" voisins
        if len(Cibles) == 2:
            if 0<Cibles[0] <2:
                compteur += f_poly_06(Cibles[0])# Nouvelle proba prenant en compte les nouveaux voisins causés par le vent

            if 0<Cibles[1] <2:
                compteur += f_poly_O2(Cibles[1])    

        p= 0.8**(8.8-compteur)
        p = 1 - (1-p)**((1+v_vent/10))
    else:
        p= 0.8  **(8.6-compteur)
        p = 1 - (1-p)**((1+v_vent/100))
    
    if compteur==0: 
        p = 0
        
    if rd.random() < p:
        cell +=dt
    else: 
        cell = 0
    return cell
