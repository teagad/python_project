import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        image_coords = (700, 700)
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, image_coords)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
