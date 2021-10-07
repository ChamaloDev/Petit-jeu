import pygame
import parametres as p

# Classe du projectile
class Projectile(pygame.sprite.Sprite):

    # Définition du constructeur de la classe
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = p.speed*4
        self.image = pygame.image.load('images\Eau.png')
        self.size = 100
        self.size2 = 2
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.rect = self.image.get_rect()
        self.origin_image = self.image
        self.angle = 0
        self.life_spawn = 0
    
    def rotate(self):
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, self.size2)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        if self.life_spawn == 0:
            self.rect.x = self.player.rect.x + (self.player.size - self.size)/4
            self.rect.y = self.player.rect.y + (self.player.size - self.size)/4
        if self.player.dash == "left":
            self.rect.x -= self.velocity
        elif self.player.dash == "right":
            self.rect.x += self.velocity
        elif self.player.dash == "up":
            self.rect.y -= self.velocity
        elif self.player.dash == "down":
            self.rect.y += self.velocity
        self.rotate()
        self.life_spawn += 0.05
        if self.life_spawn >= 1:
            self.size2 = 4 - self.life_spawn*2
            self.velocity = 0
        if self.life_spawn >= 2:
            # Suprimer le méchant projectile
            self.remove()

        # Verification pour savoir si le projectile à atteint sa cible
        for ennemi in self.player.game.collisions(self, self.player.game.all_ennemis):
            # Taper le méchant
            ennemi.damage(self.player.atk, self.player.dash)