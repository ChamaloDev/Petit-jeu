import pygame
import parametres as p
from game import Game
from math import sqrt
pygame.init()

# Génération de la fenêtre de jeu
pygame.display.set_caption("La babale contre le reste du monde")
screen = pygame.display.set_mode((p.screen_x, p.screen_y))

# Arrière plan
background = pygame.image.load('images/Arriere_plan.png')
background = pygame.transform.scale(background,(p.screen_x, p.screen_y))

# Chargement du jeu
game = Game()

# Nombre de touches pressé en même temps
nb_touches_pressées = 0

running = True
print("Lancement du jeu...")

# Boucle principale
while running:
    # Frame rate
    p.clock.tick(p.frame_rate)

    # Application délicate et soignée de l'arrière plan
    screen.blit(background, (0, 0))

    # Application du sprite du joueur
    screen.blit(game.player.image, game.player.rect)
    
    # Faire bouger les projectiles
    for projectile in game.player.all_projectiles:
        projectile.move()

    # Faire bouger les ennemis
    for ennemi in game.all_ennemis:
        ennemi.forward()
        ennemi.barre_de_vie(screen)

    # Application de tous les projectiles
    game.player.all_projectiles.draw(screen)

    # Application des ennemis, toujours aussi délicatement
    game.all_ennemis.draw(screen)

    # Mouvements
    if game.pressed.get(pygame.K_d) and game.player.rect.x+game.player.rect.width*game.player.size/game.player.rect.width<p.screen_x:
        game.player.move_right()
    if game.pressed.get(pygame.K_q) and game.player.rect.x>0:
        game.player.move_left()
    if game.pressed.get(pygame.K_s) and game.player.rect.y+game.player.rect.width*game.player.size/game.player.rect.width<p.screen_y:
        game.player.move_down()
    if game.pressed.get(pygame.K_z) and game.player.rect.y>0:
        game.player.move_up()

    # Misse à jour de l'écran
    pygame.display.flip()

    # Evennement
    for event in pygame.event.get():

        # Arrêt du jeu
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu...")

        # Actions du joueur
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
            else:
                nb_touches_pressées += 1

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            if event.key != pygame.K_SPACE:
                nb_touches_pressées -= 1

        if nb_touches_pressées >= 2:
            game.player.speed = sqrt(p.speed)
        else:
            game.player.speed = p.speed