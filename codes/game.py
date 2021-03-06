import pygame
from player import Player
from monster import Ennemi

# Classe du jeu
class Game:

    def __init__(self):
        # Génération du joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # Groupe de méchants
        self.all_ennemis = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_ennemi()
        self.spawn_ennemi()

    def collisions(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_ennemi(self):
        self.ennemi = Ennemi(self)
        self.all_ennemis.add(self.ennemi)