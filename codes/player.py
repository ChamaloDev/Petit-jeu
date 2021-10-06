import pygame
import parametres as p
from projectile import Projectile

# Classe du joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.atk = 1
        self.speed = p.speed
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('images\Babale.png')
        self.size = 100
        self.image = self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.rect = self.image.get_rect()
        self.rect.x = p.screen_x/2 - self.size/2
        self.rect.y = p.screen_y/2 - self.size/2

    def launch_projectile(self, game):
        # Créer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self, game))

    def move_right(self):
        self.rect.x += self.speed
        if self.game.collisions(self, self.game.all_ennemis):
            self.rect.x -= self.speed
    
    def move_left(self):
        self.rect.x -= self.speed
        if self.game.collisions(self, self.game.all_ennemis):
            self.rect.x += self.speed
    
    def move_down(self):
        self.rect.y += self.speed
        if self.game.collisions(self, self.game.all_ennemis):
            self.rect.y -= self.speed

    def move_up(self):
        self.rect.y -= self.speed
        if self.game.collisions(self, self.game.all_ennemis):
            self.rect.y += self.speed