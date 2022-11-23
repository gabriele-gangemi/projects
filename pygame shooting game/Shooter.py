import pygame
import random
import sys


def fill(path, xsize, ysize):
    obj = pygame.image.load(path)
    for x in range(0, xsize, obj.get_size()[0]):
        for y in range(0, ysize, obj.get_size()[1]):
            Screen.blit(obj, (x, y))


# crosshair sprite
class Crosshair(pygame.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(path), (30, 30))
        self.rect = self.image.get_rect()
        self.sound = pygame.mixer.Sound("Shootsound.mp3")

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def shoot(self):
        pygame.sprite.spritecollide(crosshair, target_group, True)
        self.sound.play()


class Target(pygame.sprite.Sprite):
    def __init__(self, path, xpos, ypos):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(path), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [xpos, ypos]


# pygame init
pygame.init()
clock = pygame.time.Clock()

# game screen
# pygame.display.set_caption("Shooter","target.png")
w_size = (800, 800)
Screen = pygame.display.set_mode(w_size)
pygame.mouse.set_visible(False)

# crosshair
crosshair = Crosshair("crosshair.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

# target
target_group = pygame.sprite.Group()
for i in range(20):
    target = Target("target.png", random.randrange(w_size[0]), random.randrange(w_size[1]))
    target_group.add(target)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()
        #if pygame.sprite.spritecollide(crosshair,target_group,True):
        #    crosshair.shoot()

    pygame.display.flip()
    fill("Blue.png", w_size[0], w_size[1])
    target_group.draw(Screen)
    target_group.update()
    crosshair_group.draw(Screen)
    crosshair_group.update()

    clock.tick(60)
