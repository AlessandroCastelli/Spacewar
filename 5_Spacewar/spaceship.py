from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.math import Vector2
from pygame.image import load
from pygame.transform import rotozoom
from entity import Entity
from math import atan2, pi
from methods import _get_sprite

import logging
class Spaceship(Entity):
    def __init__(self, position, angle, player):
        logging.debug(f'init start player {player}')
        self.life = 3
        self.energy = 50
        self.energy_missle = 100
        self.energy_laser = 400
        super().__init__(
			position, _get_sprite("player" + str(player)), 3, angle
		)

        logging.debug(f'init done player {player}')

    def change_angle(self, sign=True):
        direction = 1 if sign else -1
        self.new_angle += 4 * direction

    

