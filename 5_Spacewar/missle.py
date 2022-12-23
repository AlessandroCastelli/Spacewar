from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.math import Vector2
from pygame.image import load
from pygame.transform import rotozoom
from entity import Entity
from methods import _get_sprite
import logging
import logmanager

class Missle(Entity):
    def __init__(self, position, angle):
        logging.debug('entering missle ctor')
        self.damage = 1
        super().__init__(
			position, _get_sprite("bullet"), 8, angle
		)
