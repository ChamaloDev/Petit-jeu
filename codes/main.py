import pygame
from game import Game
pygame.init()

# Génération de la fenêtre de jeu
pygame.display.set_caption("La babale contre le reste du monde")
screen = pygame.display.set_mode((1000, 1000))

# Arrière plan
background = pygame.image.load('images/Arriere_plan.png')

# Chargement du jeu
game = Game()

running = True
print("Lancement du jeu...")

# Boucle principale
while running:

    # Application délicate et soignée de l'arrière plan
    screen.blit(background, (0, 0))

    # Application du sprite du joueur
    screen.blit(game.player.image, game.player.rect)
    
    # Application de tous les projectiles
    game.player.all_projectiles.draw(screen)

    # Mouvements
    if game.pressed.get(pygame.K_d) and game.player.rect.x+game.player.rect.width*game.player.size/game.player.rect.width<1000:
        game.player.move_right()
    if game.pressed.get(pygame.K_q) and game.player.rect.x>0:
        game.player.move_left()
    if game.pressed.get(pygame.K_s) and game.player.rect.y+game.player.rect.width*game.player.size/game.player.rect.width<1000:
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

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        
