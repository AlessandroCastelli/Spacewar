from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.math import Vector2
from pygame.image import load
from pygame.transform import rotozoom
from math import atan2, pi

class Spaceship:

    def __init__(self,position, velocity, player):
        self.psx, self.psy = Vector2(position)
        self.sprite = _get_sprite("Player" + str(player))
        self.radius = self.sprite.get_width() / 2
        #self.velocity = Vector2(velocity)
        self.direction = None

    def draw(self, surface, x, y):
		#angolo
        angle = atan2(self.psy - y,x - self.psx) * 180 / pi
		#rotazione immagine
        rotated_image = rotozoom(self.sprite, angle, 1.0)
		#coordinate immagine ruotata
        blit_position = self.position - (Vector2(rotated_image.get_size())/2)

        surface.blit(rotated_image, blit_position)


def _get_sprite(name, with_alpha=True):
    path = f"/sprites/{name}.png"
    loaded_sprite = load(path)
    return loaded_sprite.convert_alpha()