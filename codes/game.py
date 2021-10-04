import pygame
from player import Player
from monster import Ennemi

# Classe du jeu
class Game:

    def __init__(self):
        # Génération du joueur
        self.player = Player()
        # Groupe de méchants
        self.all_ennemis = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_ennemi()

    def spawn_ennemi(self):
        ennemi = Ennemi()
        self.all_ennemis.add(ennemi)