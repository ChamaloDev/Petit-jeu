import pygame

# Classe de l'ennemi
class Ennemi(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.pv = 100
        self.max_pv = 100
        self.dommages = 10
        self.size = 100
        self.image = pygame.image.load('images\Mechant.png')
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.rect = self.image.get_rect()