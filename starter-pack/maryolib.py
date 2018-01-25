import pygame

# RGB renk tanimlamalari
BLACK = (0, 0, 0)
GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)


class MaryoImageObject(pygame.sprite.Sprite):
    def __init__(self, width, height, image_path, x=0, y=0):
        super().__init__()
        self.width = width
        self.height = height

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect()

        self.weight = 50
        self.down_speed = 1

        self.is_jumped = True

        self.move_to(x,y)

    def apply_gravity(self):
        if self.is_jumped:
            self.move_down(self.down_speed)
            self.down_speed += 1

    def move_to(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def move_right(self, pixels=5):
        self.rect.x += pixels

    def move_left(self, pixels=5):
        self.rect.x -= pixels

    def move_down(self, pixels=5):
        self.rect.y += pixels

    def move_up(self, pixels=5):
        self.rect.y -= pixels
