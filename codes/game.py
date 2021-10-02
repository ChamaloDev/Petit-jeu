import pygame
from player import Player

# Classe du jeu
class Game:

    def __init__(self):
        # Génération du joueur
        self.player = Player()
        self.pressed = {}