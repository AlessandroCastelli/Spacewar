from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.math import Vector2
from pygame.image import load
from pygame.transform import rotozoom
from math import atan2, pi

import logging
class Spaceship:

    def __init__(self, position, angle, player):
        logging.debug(f'init start player {player}')
        self.position = Vector2(position)
        self.psx, self.psy = Vector2(self.position)
        self.angle = angle
        self.speed = 3
        self.sprite = _get_sprite("player" + str(player))
        self.radius = self.sprite.get_width() / 2
        self.velocity = Vector2(self.speed, 0).rotate(self.angle)
        logging.debug(f'init done player {player}')

    def draw(self, surface):
        self.psx, self.psy = self.position
		#rotazione immagine
        rotated_image = rotozoom(self.sprite, self.angle, 1.0)
		#coordinate immagine ruotata
        blit_position = Vector2(self.psx, self.psy) - (Vector2(rotated_image.get_size())/2)

        surface.blit(rotated_image, blit_position)

    def change_angle(self, value):
        self.angle = self.angle + value
        self.velocity = self.velocity.rotate(self.angle)

    def move(self):
        self.position = self.position + self.velocity

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