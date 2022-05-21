import pygame

SIZE = WIDTH, HEIGHT = 1024, 720
WIN = pygame.display.set_mode(SIZE)
SCREENRECT = pygame.Rect(0, 0, WIDTH, HEIGHT)
pygame.display.set_caption("TALP - Pygame")


class Player(pygame.sprite.Sprite):
    speed = 10
    images = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.facing = 1

    def move(self, direction):
        if direction:
            self.facing = direction
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(SCREENRECT)
        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]


def draw_window():
    WIN.fill((255, 255, 255))
    # atualizações aqui
    all.draw(WIN)
    pygame.display.update()


def event_capture():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # else:
        #     print(event)

    keystate = pygame.key.get_pressed()
    direction = keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
    player.move(direction)


def main():
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        event_capture()
        draw_window()
    pygame.quit()


img = pygame.image.load("./player.png")
Player.images = [
    img,
    pygame.transform.flip(img, 1, 0),
]
all = pygame.sprite.RenderUpdates()
Player.containers = all

player = Player()

run = True
if __name__ == "__main__":
    main()
