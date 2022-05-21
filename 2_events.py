import pygame

SIZE = WIDTH, HEIGHT = 1024, 720
WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("TALP - Pygame")


def event_capture():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        else:
            print(event)


def main():
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        event_capture()
    pygame.quit()


run = True
if __name__ == "__main__":
    main()
