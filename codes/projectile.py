import pygame
import parametres as p

# Classe du projectile
class Projectile(pygame.sprite.Sprite):

    # Définition du constructeur de la classe
    def __init__(self, player, game):
        super().__init__()
        self.velocity = 2
        self.player = player
        self.image = pygame.image.load('images\Projectile.png')
        self.size = 50
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + player.size/4
        self.rect.y = player.rect.y + player.size/4
        self.origin_image = self.image
        self.angle = 0
    
    def rotate(self):
        self.angle += 1
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
    def remove(self):
        self.player.all_projectiles.remove(self)
        print("projectile supprimé")

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # Verification pour savoir si le projectile à atteint sa cible
        if self.player.game.collisions(self, self.player.game.all_ennemis):
            #Suprimer le méchant projectile
            self.remove()

        # Tuer le méchant projectile si il est partit trop loin
        if self.rect.x > p.screen_x or self.rect.x < 0:
            self.remove()
        elif self.rect.y > p.screen_y or self.rect.y < 0:
            self.remove()