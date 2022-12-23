import pygame
from pygame.math import Vector2
from pygame.image import load
from pygame.transform import rotozoom
from entity import Entity
from methods import _get_sprite
import logging
import logmanager

class Planet(Entity):
    def __init__(self, position):
        logging.debug('entering planet ctor')
        self.damage = 3
        super().__init__(
			position, _get_sprite("planet"), 0, 0
		)