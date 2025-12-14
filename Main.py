import pygame
from GameManager import GameManager

pygame.init()
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Rhythm Hero")

clock = pygame.time.Clock()
game = GameManager(screen)
game.start_game()

running = True
while running:
    screen.fill((0, 0, 0))

    running = game.handle_input()
    game.update_game()
    game.draw_ui()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
