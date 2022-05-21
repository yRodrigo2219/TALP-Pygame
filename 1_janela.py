import pygame

SIZE = WIDTH, HEIGHT = 1024, 720
WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("TALP - Pygame")


def main():
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
    pygame.quit()


run = True
if __name__ == "__main__":
    main()
