import pygame

# Classe du projectile
class Projectile(pygame.sprite.Sprite):

    # Définition du constructeur de la classe
    def __init__(self):
        super().__init__()
        self.velocity = 1
        self.image = pygame.image.load('images/Babale.png')
        self.rect = self.image.get_rect()