import pygame
import sys

pygame.init()
pygame.display.set_caption("TENKOVI!")

WINDOW_SIZE = (800, 600)

WINDOW = pygame.display.set_mode(WINDOW_SIZE)

TANK1_IMAGE = pygame.image.load('resources/tank1.png')
TANK1_IMAGE = pygame.transform.scale(TANK1_IMAGE, (int(TANK1_IMAGE.get_width() * 0.1), int(TANK1_IMAGE.get_height() * 0.1)))
TANK2_IMAGE = pygame.image.load('resources/tank2.png')
TANK2_IMAGE = pygame.transform.scale(TANK2_IMAGE, (int(TANK2_IMAGE.get_width() * 0.1), int(TANK2_IMAGE.get_height() * 0.1)))

GROUND_HEIGHT = 50
GROUND_COLOR = (160, 82, 45)
GROUND = pygame.Surface((WINDOW_SIZE[0], GROUND_HEIGHT))
GROUND.fill(GROUND_COLOR)


def draw_window():
    # Fill the window with sky blue color
    WINDOW.fill((135, 206, 235))
    # Draw the ground surface
    WINDOW.blit(GROUND, (0, WINDOW_SIZE[1] - GROUND_HEIGHT))
    # Draw the tanks
    WINDOW.blit(TANK1_IMAGE, (0, WINDOW_SIZE[1] - GROUND_HEIGHT - TANK1_IMAGE.get_height()))
    WINDOW.blit(TANK2_IMAGE, (WINDOW_SIZE[0] - TANK2_IMAGE.get_width(), WINDOW_SIZE[1] - GROUND_HEIGHT - TANK2_IMAGE.get_height()))


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        draw_window()
        pygame.display.update()


if __name__ == "__main__":
    main()
