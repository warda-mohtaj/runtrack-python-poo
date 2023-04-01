import random

class Carte():
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu():
    def __init__(self):
        self.paquet = []
        self.valeurs = ["as", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valet", "dame", "roi"]
        self.couleurs = ["coeur", "carreau", "pique", "trefle"]