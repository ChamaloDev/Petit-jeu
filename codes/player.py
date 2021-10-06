import pygame
import parametres as p
from projectile import Projectile

# Classe du joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.projectile = Projectile(self)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.atk = 1
        self.speed = 0
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('images\Babale.png')
        self.size = 100
        self.image = self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.rect = self.image.get_rect()
        self.rect.x = p.screen_x/2 - self.size/2
        self.rect.y = p.screen_y/2 - self.size/2
        self.dash = "no"
        self.cold_down = 0

    def launch_projectile(self):
        # Créer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))

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

    def attack(self):
    # Taper ou ne pas taper, telle est la question...
        if self.dash != "no":
            if self.dash == "left":
                if self.rect.x <= 0:
                    self.rect.x = 0
                    self.cold_down = 100
                elif self.cold_down <= 20:
                    self.rect.x -= p.speed*4
            if self.dash == "right":
                if self.rect.x + self.size >= p.screen_x:
                    self.rect.x = p.screen_x - self.size
                    self.cold_down = 100
                elif self.cold_down <= 20:
                    self.rect.x += p.speed*4
            if self.dash == "up":
                if self.rect.y <= 0:
                    self.rect.y = 0
                    self.cold_down = 100
                elif self.cold_down <= 20:
                    self.rect.y -= p.speed*4
            if self.dash == "down":
                if self.rect.y + self.size >= p.screen_y:
                    self.rect.y = p.screen_y - self.size
                    self.cold_down = 100
                elif self.cold_down <= 20:
                    self.rect.y += p.speed*4
            if self.cold_down < 100:
                self.cold_down += 1
            else:
                self.dash = "no"
                self.cold_down = 0