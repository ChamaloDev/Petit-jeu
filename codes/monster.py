import pygame
from random import random, randrange
import parametres as p

# Classe de l'ennemi
class Ennemi(pygame.sprite.Sprite):

    def stats(self):
        self.max_pv = randrange(50, 150)
        self.pv = self.max_pv
        self.size = self.max_pv
        self.dommages = randrange(1, 4)*self.size/100
        self.image = pygame.transform.scale(self.original_image,(self.size,self.size))
        self.rect.x = p.screen_x
        self.rect.y = randrange(0-self.size, p.screen_y)
        self.speed = randrange(2500, 15000)/self.size
        self.speed2 = randrange(500, 3500)/self.size
        self.wait = 0
        self.wait2 = 0
        self.gauche = 1
        self.haut = randrange(0, 1)

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('images\Mechant.png')
        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.stats()

    def damage(self, amount, dash):
        # Faire bobo au méchant
        self.pv -= amount
        # Le méchant est décédé ou pas
        if self.pv <= 0:
            # Méchant est mort, méchant disparait... ou pas
            self.stats()
        else:
            # Calcul du recul
            i = 10
            while self.game.collisions(self, self.game.all_players):
                x = randrange(-i,i)
                y = randrange(-i,i)
                self.rect.x += x
                self.rect.y += y
                print(x, y)
                if self.game.collisions(self, self.game.all_players):
                    self.rect.x -= x*2
                    self.rect.y -= y*2

    def barre_de_vie(self, surface):
        # Couleur bare de vie
        noir = (0, 0, 0)
        if self.pv > 0:
            couleur_pv = (255-self.pv/self.max_pv*255, self.pv/self.max_pv*255, 0)
        else:
            couleur_pv = (255, 0, 0)
        # Position et taille de la bare de vie
        fond_pv = [self.rect.x-2, self.rect.y-16, self.size+4, 12]
        if self.pv > 0:
            bar_position = [self.rect.x+(self.max_pv-self.pv)/self.max_pv*self.size/2, self.rect.y-14, self.pv/self.max_pv*self.size, 8]
        else:
            bar_position = [self.rect.x+self.size/2, self.rect.y+10, 0, 6]
        # Dessiner la bare de vie
        pygame.draw.rect(surface, noir, fond_pv)
        pygame.draw.rect(surface, couleur_pv, bar_position)

    def forward(self, all_projectiles):
        if not self.game.collisions(self, self.game.all_players) and not self.game.collisions(self, all_projectiles):
            while self.wait >= 100:
                self.wait -= 250 - 150*(self.pv/self.max_pv)
                if self.gauche == 1:
                    self.rect.x -= 1
                    if self.rect.x <= 0:
                        self.gauche = 0
                else:
                    self.rect.x += 1
                    if self.rect.x+self.size >= p.screen_x:
                        self.gauche = 1
            self.wait += self.speed
            while self.wait2 >= 100:
                self.wait2 -= 250 - 150*(self.pv/self.max_pv)
                if self.haut == 1:
                    self.rect.y -= 1
                    if self.rect.y <= 0:
                        self.haut = 0
                else:
                    self.rect.y += 1
                    if self.rect.y+self.size >= p.screen_y:
                        self.haut = 1
            self.wait2 += self.speed2