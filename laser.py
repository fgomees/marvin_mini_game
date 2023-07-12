import pygame
import main

class Laser(pygame.sprite.Sprite):
    def __init__(self, player_rect):
        super().__init__()
        laser_image = pygame.image.load('graphics/osso.png').convert_alpha()
        self.image = pygame.transform.scale(laser_image, (120, 50))
        self.rect = self.image.get_rect(midleft=player_rect.midright)
        self.alive = True

    def update(self):
        if self.alive:
            self.rect.x += 10
            if self.rect.x > 800:
                self.kill()
                if pygame.sprite.spritecollide(self, obstacle_group, True):
                    self.alive = False
                    laser_group.remove(self)
                else:
                    self.kill()