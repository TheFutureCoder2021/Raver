import pygame 

pygame.init()

WIDTH , HEIGHT = 1200, 600
pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Raver')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            pygame.quit()


