from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.math import Vector2
from pygame.image import load
from pygame.transform import rotozoom
from math import atan2, pi

import logging
class Spaceship:

    def __init__(self,position, velocity, angle, player):
        logging.debug(f'init start player {player}')
        self.psx, self.psy = Vector2(position)
        self.angle = angle
        self.sprite = _get_sprite("player" + str(player))
        self.radius = self.sprite.get_width() / 2
        #self.velocity = Vector2(velocity)
        self.direction = None
        logging.debug(f'init done player {player}')

    def draw(self, surface, x, y):
		#angolo
        #angle = atan2(self.psy - y,x - self.psx) * 180 / pi
        angle = self.angle * 15 / pi
		#rotazione immagine
        rotated_image = rotozoom(self.sprite, angle, 1.0)
		#coordinate immagine ruotata
        blit_position = Vector2(self.psx, self.psy) - (Vector2(rotated_image.get_size())/2)

        surface.blit(rotated_image, blit_position)

    def change_angle(self, value):
        self.angle = self.angle + value

def _get_sprite(name, with_alpha=True):
    logging.debug(f'loading sprite {name}')
    try:
        path = f"./sprites/{name}.png"
        loaded_sprite = load(path)
        if with_alpha:
            return loaded_sprite.convert_alpha()
        else:
            return loaded_sprite
    except Exception as e:
        logging.exception(f'error loading sprite {name}')
        return None