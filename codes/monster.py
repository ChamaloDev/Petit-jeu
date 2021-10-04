import pygame
from random import random, randrange
import parametres as p

# Classe de l'ennemi
class Ennemi(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.max_pv = randrange(75, 125)
        self.pv = self.max_pv
        self.dommages = 10
        self.size = 100
        self.image = pygame.image.load('images\Mechant.png')
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.rect = self.image.get_rect()
        self.rect.x = p.screen_x
        self.rect.y = randrange(0-self.size, p.screen_y)
        self.speed = randrange(1, 100)/100

    def forward(self):
        if not self.game.collisions(self, self.game.all_players):
            self.rect.x -= self.speed
