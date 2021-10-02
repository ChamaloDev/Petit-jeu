import pygame
from projectile import Projectile

# Classe du joueur
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.speed = 2
        self.image = pygame.image.load('images/Babale.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.size = 100
        self.image = self.image = pygame.transform.scale(self.image,(self.size,self.size))

    def launch_projectile(self):
        # Créer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile())

    def move_right(self):
        self.rect.x += self.speed
    
    def move_left(self):
        self.rect.x -= self.speed
    
    def move_down(self):
        self.rect.y += self.speed

    def move_up(self):
        self.rect.y -= self.speed