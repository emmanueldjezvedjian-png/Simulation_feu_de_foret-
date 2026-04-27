from PIL import Image
import numpy as np
import colorsys
import random

#reconnaissance_image prend une image en argument et renvoie une matrice associé à cette image 
#où tout les pixels vert sont associé à des arbres (0) et les autres pixel à du vide (3)

def reconnaissance_image(image, densité):
    
    image = image.convert("RGB")  # Convertir l'image en mode RGB
    pixels = np.array(image)      # Convertir en tableau numpy pour manipuler les pixels

    # Définir les seuils pour le vert
    def is_green(pixel):
        r, g, b = [x / 255.0 for x in pixel]  # Normaliser les valeurs entre 0 et 1 car colorsys attend une valeur entre O et 1
        h, s, v = colorsys.rgb_to_hsv(r, g, b)# conversion RGB -> HSV (Teinte,saturation,valeur)
        return 40 / 360 <= h <= 180 / 360 and s > 0.10 and v > 0.20#Critères permetant de détecter le vert
    
    height, width, _ = pixels.shape
    matrix = np.zeros((height, width), dtype=int)
    for i in range(height):
        for j in range(width):
            if is_green(pixels[i, j]) and random.random() < densité:
                matrix[i, j] = 0  # Pixel vert
            else:
                matrix[i, j] = 3  # Autres pixels

    return matrix


if __name__ == "__main__":
    np.set_printoptions(threshold=np.inf)
    image_path = "pygame/cartes/cartes_test.jpg"  
    densité = 0.6 # Remplacez par votre densité
    matrice = reconnaissance_image(image_path,densité)
    print("Matrice générée :")
    print(matrice)