import pygame
import sys
from random import randint, random
from fire import func_fire
from init_forest import *
import random as rd
from generation import *
#import tkinter as tk
#from tkinter import filedialog
#from PIL import Image
from reconnaissance_image import *

#import Wind_effect
#import feux_forets_simulation

# Couleurs
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)  # Arbre vivant
RED = (255, 0, 0)      # Feu
DARK_GRAY = (105, 105, 105)  # Cendres
SANDY_YELLOW = (244, 164, 96)  # Vide

#Affiche une boîte de saisie pour récupérer une valeur de l'utilisateur.
def input_box(screen, prompt, x, y):
    
    font = pygame.font.Font(None, 36)
    input_text = ""
    input_rect = pygame.Rect(x, y, 200, 50)
    active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:  # Valider
                        return input_text
                    elif event.key == pygame.K_BACKSPACE:  # Effacer
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

        screen.fill((255, 255, 255))  # Effacer l'écran
        pygame.draw.rect(screen, (0, 0, 0), input_rect, 2 if active else 1)  # Dessiner la boîte
        text_surface = font.render(prompt + input_text, True, (0, 0, 0))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        pygame.display.flip()
import math as m

def draw_input_box(screen, box, text, font, active_color, inactive_color, is_focused):
    
    # Couleur en fonction de l'état (focalisée ou non)
    color = active_color if is_focused else inactive_color

    # Dessiner la boîte
    pygame.draw.rect(screen, color, box, border_radius=5)

    # Ajouter un halo (facultatif)
    if is_focused:
        halo_rect = box.inflate(10, 10)  # Agrandir légèrement
        pygame.draw.rect(screen, color, halo_rect, width=2, border_radius=8)

    # Texte dans la boîte
    text_surface = font.render(text, True, (255, 255, 255))  # Blanc pour le texte
    screen.blit(text_surface, (box.x + 10, box.y + 5))
#Dessine un bouton rectangulaire avec texte.
def draw_button(screen, text, rect, color=(70, 130, 180)):
    
    pygame.draw.rect(screen, color, rect)
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (rect.x + 10, rect.y + 10))

def draw_3d_button(screen, rect, text, color, hover_color, shadow_color, font, is_hovered=False):
    
    shadow_offset = 4  # Décalage de l'ombre
    if is_hovered:
        button_color = hover_color
    else:
        button_color = color

    # Ombre
    shadow_rect = rect.move(shadow_offset, shadow_offset)
    pygame.draw.rect(screen, shadow_color, shadow_rect, border_radius=8)

    # Bouton principal
    pygame.draw.rect(screen, button_color, rect, border_radius=8)

    # Texte centré
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)


#Fenêtre d'initialisation avec interface améliorée et chargement d'image.
def initialisation_window():
   
    pygame.init()
    
    # Dimensions et fenêtre
    screen_width = int(1000 * (1 + m.sqrt(5)) / 2)
    screen_height = 1000
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    # Image de fond
    background_image = pygame.image.load("images/img_fond.jpg").convert()
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
    
    pygame.display.set_caption("Initialisation du Feu de Forêt")
    font = pygame.font.Font(None, 36)

    # Champs de saisie
    input_boxes = [
        {"prompt": "Largeur de la grille : ", "value": "", "rect": pygame.Rect(300, 200, 300, 50)},
        {"prompt": "Hauteur de la grille : ", "value": "", "rect": pygame.Rect(300, 350, 300, 50)},
        {"prompt": "Densité d'arbres (0-1) : ", "value": "", "rect": pygame.Rect(300, 500, 300, 50)},
        {"prompt": "Départ de feu : ", "value": "", "rect": pygame.Rect(300, 650, 300, 50)},
        {"prompt": "Direction du vent : ", "value": "", "rect": pygame.Rect(screen_width - 600, 200, 300, 50)},
        {"prompt": "Intensité du vent (Km/h) : ", "value": "", "rect": pygame.Rect(screen_width - 600, 350, 300, 50)}
    ]
    active_box = None  # Boîte active
    image_path = None  # Chemin vers le fichier sélectionné

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Activer ou désactiver les boîtes
                for box in input_boxes:
                    if box["rect"].collidepoint(event.pos):
                        active_box = box
                        break
                else:
                    active_box = None

                # Bouton pour charger une image
                if load_button.collidepoint(event.pos):
                    # Boîte de dialogue pour charger un fichier
                  #  import tkinter as tk
                 #   from tkinter import filedialog
                    file_path = None
    
                    
                    if file_path:
                        image_path = file_path

                # Bouton de validation
                if launch_button.collidepoint(event.pos):
                    try:
                        width = int(input_boxes[0]["value"])
                        height = int(input_boxes[1]["value"])
                        density = float(input_boxes[2]["value"])
                        fire_type = str(input_boxes[3]["value"])
                        wind_direction = str(input_boxes[4]["value"])
                        wind_strength = int(input_boxes[5]["value"])

                        # Si une image a été chargée, la convertir en matrice
                        if image_path:
                            from PIL import Image
                            matrix = load_image_to_matrix(image_path, width, height, density)
                            return matrix, width, height, density, fire_type, wind_direction, wind_strength
                        else:
                            return None, width, height, density, fire_type, wind_direction, wind_strength
                    except ValueError:
                        print("Erreur : Veuillez entrer des valeurs valides.")

            if event.type == pygame.KEYDOWN and active_box:
                if event.key == pygame.K_RETURN:
                    active_box = None
                elif event.key == pygame.K_BACKSPACE:
                    active_box["value"] = active_box["value"][:-1]  # Supprimer le dernier caractère
                else:
                    active_box["value"] += event.unicode

        # Dessiner le fond
        screen.blit(background_image, (0, 0))

        # Titre
        title = pygame.font.Font(None, 48).render("Initialisation du Feu de Forêt", True, (60, 60, 100))
        screen.blit(title, (100, 30))

        # Dessiner les boîtes de saisie
        for box in input_boxes:
            # Couleur de bordure et texte en fonction de l'état actif
            border_color = (50, 168, 82) if box == active_box else (255, 255, 255)
            text_color = border_color

            # Dessiner la boîte et afficher le texte
            pygame.draw.rect(screen, border_color, box["rect"], 2)
            prompt = font.render(box["prompt"], True, (255, 255, 255))  # Label reste blanc
            value = font.render(box["value"], True, text_color)         # Texte prend la couleur dynamique
            screen.blit(prompt, (box["rect"].x - 100, box["rect"].y - 50))
            screen.blit(value, (box["rect"].x + 5, box["rect"].y + 10))

        # Bouton "Charger Image"
        load_button = pygame.Rect(screen_width // 2 + 150, screen_height - 250, 300, 50)
        pygame.draw.rect(screen, (70, 130, 180), load_button)
        load_text = font.render("Charger Image", True, (255, 255, 255))
        screen.blit(load_text, (load_button.x + 50, load_button.y + 10))

        # Bouton "Lancer"
        launch_button = pygame.Rect(screen_width // 2 - 150, screen_height - 150, 300, 50)
        pygame.draw.rect(screen, (34, 85, 34), launch_button)
        launch_text = font.render("Lancer", True, (255, 255, 255))
        screen.blit(launch_text, (launch_button.x + 100, launch_button.y + 10))

        pygame.display.flip()


def get_cell_color(cell):
    """
    Retourne la couleur correspondant à l'état de la cellule.
    """
    if cell < 1:  
                forest_green = (34, 139, 34)  # Vert forêt
                dark_red = (255, 0, 0)        # Rouge foncé

                # Interpolation linéaire pour chaque composante
                r = int(forest_green[0] + (dark_red[0] - forest_green[0]) * cell)
                g = int(forest_green[1] + (dark_red[1] - forest_green[1]) * cell)
                b = int(forest_green[2] + (dark_red[2] - forest_green[2]) * cell)

    elif cell < 2:  # Entre rouge (x=1) et gris (x=2)
                r = int(255 - (cell - 1) * 86)   # Le rouge passe de 255 à 169
                g = int((cell - 1) * 86)         # Le vert passe de 0 à 169
                b = int((cell - 1) * 86)         # Le bleu passe de 0 à 169
    elif cell >= 2:  # Pour x >= 2, on est à gris
                r = g = b = 169
    elif cell == 3: 
                r, g, b = SANDY_YELLOW
    #print(r,g,b)
    return (r,g,b)


def make_random_grid(x, y, density = 0.6):
    return init_forest_2(x, y, density)

#Charge une image et la convertit en une matrice en utilisant la reconnaissance des pixels verts.
def load_image_to_matrix(file_path, width, height, densité):
   
#    from PIL import Image  
    image = Image.open(file_path).convert("RGB")  # Convertir en RGB
    image = image.resize((width, height))  # Redimensionner à la taille souhaitée
    return reconnaissance_image(image, densité)

#load_fire ajoute le feu à la forest
def load_fire(forest,fire,x_start='a',y_start='a'):

    if x_start=='a':
         x_start=rd.randint(0,len(forest)-1)
    if y_start=='a':
         y_start=rd.randint(0,len(forest)-1)
    
    L = len(forest)
    W = len(forest[0])
    
    if fire == "verticale" :
        for k in range(0,W):
            if  forest[x_start][(k+y_start)%W] == 0:
                forest[x_start][(k+y_start)%W] = 1
   
    elif fire == "horizontale" :
        for k in range(0,L):
            if forest[(k+x_start)%L][y_start] == 0:
                forest[(k+x_start)%L][y_start] = 1
    
    elif fire == "solo" :
        forest[x_start][y_start] = 1
    
    elif fire == "cube" :
        for k in range(2):
            for j in range(2):
                forest[(j+x_start)%L][(k+y_start)%W] = 1
    
    return forest



def evolve_forest(grid,wind_direction="North",wind_strength=100,dt="0.1"):
    
    #Mets à jour la grille en utilisant les règles : 

    new_grid = genereation_continue(grid,wind_direction,wind_strength,dt)

    return new_grid


def main():
    """Programme principal."""
    # Initialisation des paramètres
    image, xlen, ylen, density, fire_type, wind_direction, wind_strength = initialisation_window()
    print(xlen, ylen, density, fire_type, wind_direction, wind_strength)
    pygame.init()
    clock = pygame.time.Clock()
    
    xlen = int(xlen)
    ylen = int(ylen)
    CELL_SIZE = max(1, min(800 // xlen, 800 // ylen))
    screen = pygame.display.set_mode((xlen * CELL_SIZE, ylen * CELL_SIZE))
    pygame.display.set_caption("Simulation de feu de forêt")

    # Création de la grille initiale
    if image is not None:
        world = image
    else:
        world = make_random_grid(xlen, ylen, density)

    world = load_fire(world, fire_type)
    
    # Boucle principale
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(SANDY_YELLOW)  
        for x in range(xlen):
            for y in range(ylen):
                cell = world[x][y]
                cell_color = get_cell_color(cell)
                pygame.draw.rect(screen, cell_color, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


        pygame.display.flip()
        world = evolve_forest(world,wind_direction,wind_strength,0.1)  
        clock.tick(1)

if __name__ == "__main__":
    main()
