import pygame
import parametres as p

# Classe du projectile
class Projectile(pygame.sprite.Sprite):

    # Définition du constructeur de la classe
    def __init__(self, player, game):
        super().__init__()
        self.player = player
        self.velocity = 2
        self.image = pygame.image.load('images\Eau.png')
        self.size = 100
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + (player.size - self.size)/4
        self.rect.y = player.rect.y + (player.size - self.size)/4
        self.origin_image = self.image
        self.angle = 0
        self.life_spawn = 0
    
    def rotate(self):
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 2)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rotate()
        self.life_spawn += 0.01
        if self.life_spawn > 1:
            # Suprimer le méchant projectile
            self.remove()

        # Verification pour savoir si le projectile à atteint sa cible
        for ennemi in self.player.game.collisions(self, self.player.game.all_ennemis):
            # Taper le méchant
            ennemi.damage(self.player.atk)