import pygame
import sys

pygame.init()
pygame.display.set_caption("TENKOVI!")

WIDTH = 800
HEIGHT = 600

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

TANK1_IMAGE = pygame.image.load('resources/tank1.png')
TANK1_IMAGE = pygame.transform.scale(TANK1_IMAGE, (int(TANK1_IMAGE.get_width() * 0.1), int(TANK1_IMAGE.get_height() * 0.1)))
TANK2_IMAGE = pygame.image.load('resources/tank2.png')
TANK2_IMAGE = pygame.transform.scale(TANK2_IMAGE, (int(TANK2_IMAGE.get_width() * 0.1), int(TANK2_IMAGE.get_height() * 0.1)))
TANK1_POSITION = (0, 500)
TANK2_POSITION = (750, 500)

PROJECTILE_RADIUS = 5
PROJECTILE_COLOR = (255, 0, 0)

GROUND_HEIGHT = (HEIGHT // 6)
GROUND_COLOR = (160, 82, 45)
GROUND = pygame.Surface((WIDTH, GROUND_HEIGHT))
GROUND.fill(GROUND_COLOR)




def draw_window():
    # Fill the window with white color
    WINDOW.fill((135, 206, 235))
    WINDOW.blit(GROUND, (0, (WIDTH, HEIGHT)[1] - GROUND_HEIGHT))
    WINDOW.blit(TANK1_IMAGE, TANK1_POSITION)
    WINDOW.blit(TANK2_IMAGE, TANK2_POSITION)
    
 


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit           
        
        draw_window()    
        pygame.display.update()
            


if __name__ == "__main__":
    main()            